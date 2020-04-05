#https://www.raspberrypi.org/forums/viewtopic.php?t=242699
import sys
import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
from urllib.request import urlopen
import datetime
from time import sleep


def get_host_ip():
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
    finally:
        s.close()
    return ip

def get_public_ip():
    # get pubilic network IP
    return urlopen('http://ip.42.pl/raw').read()

def send_email(receiver, sender_account, psk):
    #account info
    #sleep(15)
    to = receiver + '@gmail.com'
    #https://myaccount.google.com/u/1/lesssecureapps
    gmail_user = sender_account + '@gmail.com'
    gmail_password = psk
    smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.login(gmail_user, gmail_password)
    today = datetime.date.today()
    arg='ip route list'
    p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
    data=p.communicate()
    #split_data=data[0].split()
    #ipaddr=split_data[split_data.index('src')+1]
    inner_ip = get_host_ip()
    external_ip = get_public_ip()
    my_ip='Good day, human. This is your Pi No.1.\n\n My inner IP today is {0} and the external IP is {1}\n\n Best wishes,\n RPI #1'.format(inner_ip,external_ip.decode())
    msg=MIMEText(my_ip)
    msg['Subject']= 'Rpi No.1 Reporting in!'
    msg['From']= gmail_user
    msg['To'] = to
    smtpserver.sendmail(gmail_user, [to], msg.as_string())
    smtpserver.quit()

#sys.argv[0] is .py file name
receiver = sys.argv[1]
sender_account = sys.argv[2]
psk = sys.argv[3]

print('To :  ' + receiver + '@gmail.com\n')
print('From:  ' + sender_account + '@gmail.com\n')
print('Authority Password: ' + psk)
send_email(receiver,sender_account,psk)