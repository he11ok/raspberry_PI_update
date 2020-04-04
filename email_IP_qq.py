#版权声明：本文为CSDN博主「微特程序员」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/qq_44636442/article/details/104874329
# -*- coding: utf-8 -*-
import socket
import smtplib
import os
import time
from email.mime.text import MIMEText
from datetime import datetime
from urllib.request import urlopen

def get_host_ip():
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
    finally:
        s.close()
    return ip

def get_public_ip():
    # 从该网站读取请求的IP地址
    return urlopen('http://ip.42.pl/raw').read()

def send_email():
    mail= MIMEText('时间：%s\n内网IP地址：' % datetime.now() + get_host_ip() + '\n公网IP地址：%s' % get_public_ip().decode())
    # 设置邮件主题
    mail["Subject"] = "树莓派定时任务-IP地址" 
    # 寄件者
    mail["From"]    = 'RaspberryPi'
    # 收件者
    mail["To"]      = 'Limu Han'
    # 邮箱账号
    from_addr = "52888796@qq.com"
    # 刚才复制的密钥字符串
    password = "wojsacgfidplcafc"
    # smtp服务器地址
    smtp_server = 'smtp.qq.com'
    # 收件人地址
    to_addr = "52888796@qq.com" 
    try:
        # smtp协议的默认端口是25，QQ邮箱smtp服务器端口是465
        # 参数分别是：smtp服务器地址、端口、超时设置
        server = smtplib.SMTP_SSL(smtp_server, 465, timeout = 20)
        # 登录邮箱
        server.login(from_addr, password)
        # 设置发件邮箱、收件地址和内容
        server.sendmail(from_addr, [to_addr], mail.as_string())
        server.quit()
        print('Mail Success！')
    except Exception as e:
        print('Mail Faild:%s'% e)
        

if __name__ == '__main__':
    send_email()
