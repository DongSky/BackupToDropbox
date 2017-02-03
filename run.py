#encoding:utf-8
import os,sys,upload,backup
config_list_path='list.json'
def backup_cloud(config_list_path):
    origin_path,timestrap,bag_path,status=backup.backup(config_list_path)
    if(status==0):
        upload.upload(timestrap+'.zip')
    else:
        print("process stoped because of backup error")

if __name__=="__main__":
    backup_cloud(config_list_path)
