

# import smtplib

# from_add ='wwwwyiyinyiyangcom@gmail.com'
# to_add = '29098663@qq.com"

# message= str(input('輸入信件内容:'))

# server = smtplib.SMTP('smtp.gmail.com',587)
# server.starttls()
# server.login(from_add,'hbcqejwebvpsywfe')

# # message ="hell fangsheng i am from google"
# server.sendmail(from_add,to_add,message)

# server.quit()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
 
# 发件人邮箱账号
my_sender='fangsheng@yangyanghub.onexmail.com'  
# user登录邮箱的用户名，password登录邮箱的密码（授权码，即客户端密码，非网页版登录密码），但用腾讯邮箱的登录密码也能登录成功  
my_pass = 'xq2PZftQtJpLD4Ck' #1982密碼為虛擬的
# 收件人邮箱账号            
my_user='29098663@qq.com'      
def mail():
    ret=True
    try:
        # 邮件内容
        msg=MIMEText('我的心碎了','plain','utf-8')
        # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['From']=formataddr(["yangyanghub",my_sender])  
        # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['To']=formataddr(["beyourself",my_user])   
        # 邮件的主题           
        msg['Subject']="使用腾讯邮箱发送邮件测试"                
 
        # SMTP服务器，腾讯企业邮箱端口是465，腾讯邮箱支持SSL(不强制)， 不支持TLS
        # qq邮箱smtp服务器地址:smtp.qq.com,端口号：456
        # 163邮箱smtp服务器地址：smtp.163.com，端口号：25
        server=smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)  
        # 登录服务器，括号中对应的是发件人邮箱账号、邮箱密码
        server.login(my_sender, my_pass)  
        # 发送邮件，括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.sendmail(my_sender,[my_user,],msg.as_string())  
        # 关闭连接
        server.quit() 
        # 如果 try 中的语句没有执行，则会执行下面的 ret=False 
    except Exception:  
        ret=False
    return ret
 
ret=mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")