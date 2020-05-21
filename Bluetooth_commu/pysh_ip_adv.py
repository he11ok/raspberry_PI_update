import os
import subprocess
import smtplib
import socket
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

def run_cmd2file(cmd):
    fout = open("cmd_out.log",'w')
    ferr = open("cmd_err.log",'a')
    # a for append, w for overwrite
    cmd_outf = subprocess.Popen(cmd, stdout=fout, stderr=ferr, shell=True)
    if cmd_outf.poll():
        return
    cmd_outf.wait()
    return

ip_addr = get_host_ip()
adv_name = 'RPI_' + ip_addr
cmd = 'sudo hciconfig hci0 name '+ adv_name
subprocess.Popen(cmd, shell = True)