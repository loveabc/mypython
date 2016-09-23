#使用smtp协议发送邮件

from email import encoders
from email.header import Header 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr,formataddr
import smtplib

#格式化邮箱地址
def format_addr(addrs):
	name,addr=parseaddr(addrs)
	return formataddr((Header(name,"utf-8").encode(),addr))
#组织html
def read_html():
	data="""
		<!DOCTYPE html>
			<html>
				<head></head>
			<body>
				<h1>HTML5</h1>
			
			</body>
		</html>
	"""
	return data
msg=MIMEMultipart()#发送带有附件的邮件
from_addr="youth_fly@163.com"
password="123oopp123"
to_addr="981257406@qq.com"
smpt_server="smtp.163.com"
# msg=MIMEText("This email from 163 by python","plain","utf8")  #发送文本邮件
msg["From"]=format_addr(from_addr)
msg["To"]=format_addr(to_addr)
msg["Subject"]=Header("html email","utf-8").encode()

with open(r'D:/home/test.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'png', filename='test.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)
with open(r'D:/home/test.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'png', filename='test.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='cartoon.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server=smtplib.SMTP(smpt_server,25)
# server.set_debuglevel(1)#开启调试
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()

