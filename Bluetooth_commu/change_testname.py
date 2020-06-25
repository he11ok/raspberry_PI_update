import os
import subprocess
import datetime
import time

f = open('adv_testname_ip.txt','r')
subprocess.Popen('sudo echo -e \'discoverable on\r\' | bluetoothctl', shell = True)
for line in f:
    adv_name = line
    cmd = 'sudo hciconfig hci0 name ' + adv_name
    subprocess.Popen(cmd, shell = True)
    #subprocess.Popen('sudo echo -e \'discoverable on\r\' | bluetoothctl', shell = True)
    time.sleep(2)
  
subprocess.Popen('sudo echo -e \'discoverable off\r\' | bluetoothctl', shell = True)
f.close()
