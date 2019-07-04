import logging
import os

from auth import Auth

PHOTOS_DIRECTORY = 'photos/'
files = os.listdir(PHOTOS_DIRECTORY)
class DriveUploader(Auth):

    to_go = len(files)
    folder_id = os.environ.get('FOLDER_ID', '1LidWwVnAWy52syJiWJTwO_dcbpunxuUz')

    def __init__(self):
        super(Auth, self).__init__()

    def upload_to_drive(self, dryRun=True):
        if dryRun:
            return "Would upload {} items to drive".format(self.to_go)
        drive = Auth.authenticate(slack=False)
        for item in files:
            self.to_go -= 1
            logging.info("{} backfilled to drive. {} left to go".format(item, self.to_go))
            # Upload file to folder.
            f = drive.CreateFile({'title': item,
                                  'parents': [{'id': self.folder_id}]})
            # Make sure to add the path to the file to upload below.
            f.SetContentFile("{}{}".format(PHOTOS_DIRECTORY, item))
            f.Upload()
        logging.info("done")
