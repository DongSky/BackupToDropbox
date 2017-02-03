#encoding:utf-8
import dropbox,os,sys,commands,json,datetime

def backup(file_path):
    origin_path=os.getcwd()
    timestrap=datetime.datetime.now().strftime('%Y-%m-%d')
    with open(file_path,'r') as f:
        commands.getstatusoutput('mkdir '+timestrap)
        to_backup_dict=json.loads(f.read())
        print(to_backup_dict)
        dict_keys=to_backup_dict.keys()
        for key in dict_keys:
            cmd=""
            piece=to_backup_dict[key]
            piece_list=piece.split('/')
            if piece_list[-1]=="":
                piece_list=piece_list[:len(piece_list)-2]
            if os.path.isdir(piece):
                cmd="zip -r "+origin_path+'/'+timestrap+'/'+piece_list[-1]+".zip "+piece
            elif os.path.isfile(piece):
                cmd="zip "+origin_path+'/'+timestrap+'/'+piece_list[-1]+".zip "+piece
            a,b=commands.getstatusoutput(cmd)
    bag_path=origin_path+'/'+timestrap+'/'
    a,b=commands.getstatusoutput("zip -r "+timestrap+".zip "+bag_path)
    print(a)
    print(b)
    if(a==0):
        return origin_path,timestrap,bag_path,0
    else:
        print('packing process error')
        return origin_path,timestrap,bag_path,1

def add_item(config_list_path,file_path):
    fcontent=None
    with open(config_list_path,'r') as f:
        list_dict=json.loads(f.read(),encoding='utf-8')
        num=int(list_dict.keys()[-1])
        list_dict[str(num+1)]=file_path
        fcontent=json.dumps(list_dict)
        f.close()
    f=open(config_list_path,'w')
    f.write(fcontent)
    f.close()

def del_item(config_list_path,file_path):
    fcontent=None
    with open(config_list_path,'r') as f:
        list_dict=json.loads(f.read(),encoding='utf-8')
        lst=list_dict.keys()
        for key in lst:
            if(list_dict[key]==file_path):
                del list_dict[key]
                break
        fcontent=json.dumps(list_dict)
        f.close()
    f=open(config_list_path,'w')
    f.write(fcontent)
    f.close()
#
# if __name__=="__main__":
#     del_item('list.json','/Users/DongSky/course2.py')
