#使用smtp协议发送邮件
from email import encoders
from email.header import Header 
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib

def format_addr(addrs):
	name,addr=parseaddr(addrs)
	return formataddr((Header(name,"utf-8").encode(),addr))
from_addr="youth_fly@163.com"
password="xxxxxxx"
to_addr="981257406@qq.com"
smpt_server="smtp.163.com"
msg=MIMEText("This email from 163 by python","plain","utf8")
msg["From"]=format_addr(from_addr)
msg["To"]=format_addr(to_addr)
msg["Subject"]=Header("From python test","utf-8").encode()
server=smtplib.SMTP(smpt_server,25)
# server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
