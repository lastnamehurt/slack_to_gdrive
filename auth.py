from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from slackclient import SlackClient
import os


class Auth(object):

    def __init__(self):
        self.slack = None
        self.drive = None

    @classmethod
    def authenticate(cls, slack=True, google=True):
        if slack:
            cls.slack = SlackClient(token=os.environ.get('POOKIE_SLACK_TOKEN'))
        if google and not slack:
            g_login = GoogleAuth()
            g_login.LocalWebserverAuth()
            cls.drive = GoogleDrive(g_login)
            return cls.drive
