import os
import time
def getFile(path):
        files=os.listdir(path)
        for file in files:
            filename=file
            file=path+'\\'+file
            if os.path.isfile(file):
                attrs=os.stat(file)
                if attrs.st_mode==33206 and (not 'keep' in file):
                    file_list.append(filename+'\n')
            else:
                getFile(file)
print('正在查找checkout的文件...')
file_list=[]
path=r'D://0100060928_view//workspace//CXLCS//Java Source//com//cathay'
getFile(path)
path=r'D://0100060928_view//workspace//CXLCS//Web Content//html'
getFile(path)
path=r'D:\0100060928_view\workspace\usr\cxlcs\config\txbean'
getFile(path)
#文件名取当前的年月日时分秒
s_now=time.strftime('%Y%m%d%H%M%S')
file=open('D://logs//'+s_now+'.txt','w+')
if len(file_list)==0:
    file.write('empty set')
else:
    i=0
    for filename in file_list:
        i+=1
        print(str(i)+'\n')
        print(filename)
        file.write(filename)
file.close()
print('end')

  
