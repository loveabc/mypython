#读取文件信息
import os
import stat
import time
fileName=r"d:/logs/20160831113836.txt"
fileState=os.stat(fileName)
print(fileState[stat.ST_SIZE])#文件大小
print(time.strftime("%Y/%m/%d %I:%M:%S",time.localtime(fileState[stat.ST_CTIME])))#创建时间
print(time.strftime("%Y/%m/%d %I:%M:%S",time.localtime(fileState[stat.ST_MTIME])))#修改时间
print(time.strftime("%Y/%m/%d %I:%M:%S",time.localtime(fileState[stat.ST_ATIME])))#最后访问时间,不知道是什么鬼?
print(stat.S_ISDIR(fileState[stat.ST_MODE]))#是否是文件夹