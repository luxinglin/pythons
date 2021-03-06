# -*- coding:UTF-8 -*-
import smtplib
from email.header import Header
from email.mime.text import MIMEText

# 第三方 SMTP 服务
mail_host = "smtp.exmail.qq.com"  # 设置服务器
mail_user = "dcim-admin@rightcloud.com.cn"  # 用户名
mail_pass = "Pioneertest@2016"  # 口令

sender = 'dcim-admin@rightcloud.com.cn'
# 接收邮件，可设置为你的QQ邮箱或者其他邮箱
receivers = ['luxinglin@pioneerservice.cn']

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    # 25 为 SMTP 端口号
    smtpObj.connect(mail_host, 465)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
