#encoding:utf-8
import argparse,os,sys,run,backup

if __name__=='__main__':
    parser=argparse.ArgumentParser(description="BackToDropboxTool")
    parser.add_argument('-c',action='store',dest='config_list_path',help='input the file path which stores the file list')
    parser.add_argument('-p',action='store',dest='path',help='input the file path which to be added or deleted')
    parser.add_argument('-o',action='store',dest='operation',help='decide the next opreation')
    result=parser.parse_args()
    if(result.operation=='backup_local'):
        backup.backup(result.config_list_path)
    elif(result.operation=='add_item'):
        backup.add_item(result.config_list_path,result.file_path)
    elif(result.operation=='del_item'):
        backup.del_item(result.config_list_path,result.file_path)
    elif(result.operation=='backup_cloud'):
        run.backup_cloud(result.config_list_path)
