#导入库，建立邮箱的连接
import smtplib
#处理邮件内容的库
from email.mime.text import MIMEText
#处理邮件附件，导入库
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.base import MIMEBase
from email import encoders

#邮箱属性配置
mailserver = 'smtp.qq.com' #邮箱服务端URL
userName_SendMail = '996071627@qq.com' #发件人
userName_AuthCode = 'qpsicnscxvarbbci' #邮箱授权码
received_Mail = ['1612587726@qq.com','2865557993@qq.com','490196843@qq.com'] #定义邮件的接收者

#发送一封简单的邮件
# content = '这是一封简单的文本内容'
# email = MIMEText(content,'plain','utf-8') #纯文本形式的邮件内容的定义
# email['Subject'] = '邮件主题'  #定义邮件主题
# email['From'] = userName_SendMail   #发件人
# email['To'] = ','.join(received_Mail)  #收件人

#发送一封HTML内容的邮件
# content = """
# <p>这是一封HTML内容的邮件</p>
# <p><a href="http://www.baidu.com">点击这里跳转到百度</a></p>
# """
# email = MIMEText(content,'html','utf-8')
# email['Subject'] = '邮件主题_HTML'
# email['From'] = userName_SendMail
# email['To'] = ','.join(received_Mail)

#发送一封带附件的邮件
email = MIMEMultipart()
email['Subject'] = '药品管理系统测试报告'
email['From'] = userName_SendMail
email['To'] = ','.join(received_Mail)
#非图片附件
att = MIMEBase('application','octet-stream')
att.set_payload(open('20201113.html','rb').read())
att.add_header('content-Disposition','attachment',filename=Header('20201113.html','gbk').encode())
encoders.encode_base64(att)
email.attach(att)

#发送邮件
smtp = smtplib.SMTP_SSL(mailserver,port=465)  #连接服务器
smtp.login(userName_SendMail,userName_AuthCode)  #服务器上登录
for i in received_Mail:
    smtp.sendmail(userName_SendMail,i,email.as_string())

smtp.quit()
