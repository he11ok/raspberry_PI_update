import socket
import sys

def transmit(reciver_IP,msg_content):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(msg_content.encode(),(reciver_IP,5000)) #the IP of the receiver
    s.close

reciver_IP = sys.argv[1]
msg_content = sys.argv[2]
transmit(reciver_IP,msg_content)