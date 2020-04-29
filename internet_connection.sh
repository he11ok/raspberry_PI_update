#!/bin/bash
cd /home/pi/pycode/
while :
do
	ping -c 2 www.google.com  &>/dev/null
	[ $? -eq 0 ] && break
done	

a='ifconfig wlan0 | grep broadcast'
#python3 /home/pi/pycode/email_IP_Gmail.py "wlan0:$a"
bash /home/pi/self_update.sh "wlan0:$a"
echo "network connected"
