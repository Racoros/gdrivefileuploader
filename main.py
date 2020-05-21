
import os
import glob
from auth import Auth

auth = Auth()
drive = auth.connect_drive()
filepath = #folder that contains the files need to be uploaded
folder_id = #<folder id>
query = {'q':f"'{folder_id}' in parents and trashed=false"}

def main():
    drive_files = list()
    drive_content = drive.ListFile(query).GetList()
    for content in drive_content:
        drive_files.append(content['title'])
    os.chdir(filepath)
    for file in glob.glob("*.pdf"):
        if (file not in drive_files):
            file_creds = {'title': file,'mimeType':'application/pdf','parents':[{"id": f"{folder_id}"}]}
            file_drive = drive.CreateFile(file_creds)  
            file_drive.Upload()
            print (f"The file: {file} has been uploaded")

if __name__ == "__main__":
    main()
