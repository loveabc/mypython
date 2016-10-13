import os
import time
#文件名取当前的年月日时分秒

def getFile(path):
        files=os.listdir(path)
        for file in files:
                filename=file
                file=path+'\\'+file
                if os.path.isfile(file):
                        attrs=os.stat(file)
                        modify_time=time.localtime(attrs.st_mtime)
                        s_latest=time.strftime('%Y%m%d%H%M%S',modify_time)
                        if s_latest>'20161008000000' and s_latest<'20161010000000' and (not file.endswith(".keep")):
                            print(s_latest)
                            file_list.append(filename+'\n')
                else:
                        getFile(file)
print('正在查找今日修改的文件...')
file_list=[]
path=r'D://0100060928_view//workspace//CXLCS//Java Source//com//cathay'
getFile(path)
path=r'D://0100060928_view//workspace//CXLCS//Web Content//html'
getFile(path)

s_now=time.strftime('%Y%m%d%H%M%S')
file=open('D://logs//latest'+s_now+'.txt','w+')
if len(file_list)==0:
    file.write('empty set')
else:
    i=0
    for filename in file_list:
        i+=1
        print(str(i)+'\n')
        file.write(filename)
file.close()
print('end')

  
