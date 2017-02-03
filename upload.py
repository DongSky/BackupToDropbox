#encoding:utf-8
import dropbox
import os,sys,backup,token
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError

def upload(zip_path):
    dbx=dropbox.Dropbox(token.token)
    with open(zip_path,'rb') as f:
        print("uploading "+zip_path.split('/')[-1])
        backup_path='/backup/'+zip_path.split('/')[-1]
        try:
            dbx.files_upload(f.read(),backup_path,mode=WriteMode('overwrite'))
            print("success")
        except ApiError as err:
            if(err.error.is_path() and err.error.get_path().error.is_insuficient_space()):
                print("Error:Insufficient space")
            elif err.user_message_text:
                print(err.user_message_text)
