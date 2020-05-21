from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class Auth(object):
    def __init__(self):
        self.auth = GoogleAuth()

    
    def connect_drive(self):
        self.auth.LoadCredentialsFile("credentials.txt")
        if self.auth.credentials is None:
            self.auth.LocalWebserverAuth()
        elif self.auth.access_token_expired:
            self.auth.Refresh()
        else:
            self.auth.Authorize()
        self.auth.SaveCredentialsFile("credentials.txt")
        return GoogleDrive(self.auth)
