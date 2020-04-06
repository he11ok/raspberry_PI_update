import os
import socket

def self_update():
    print('self_update command reviced\n'\
          + 'The RPI is downloading the codes from Github and try to run them ...\n')
    #when try to modify the code remember to comment the self_update.sh
    status = os.system('bash ~/self_update.sh')
    print(status)
    
def random_walk():
    print('random_walk command is received\n'\
          + 'start random walk ...\n')
    
def state_report():
    print('state_report command received\n'\
          + 'report the state of the robot ...\n')
    
def command_exe(command):
    #command dictionary, use comma to seperate
    return\
    {
        'self_update':self_update,\
        'random_walk':random_walk,\
        'state_report':state_report
    }[command]()
    #here the () is very important to be outside,
    #or each funciton in the dict will be called when construct the dict



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('',5000))
while True:
    data, addr = s.recvfrom(1024)
    rcv_data = data.decode()
    print('received message:{0} from PORT {1} on {2}'\
          .format(data.decode(),addr[1],addr[0]))
    if rcv_data == 'close':
        print('close the receiver\n')
        break
    
    if ('CMD:bristol ' in rcv_data):
        #attention the CMD:bristol followed by a space
        command = rcv_data.lstrip('CMD:bristol')
        command = command.lstrip()
        command = command.rstrip()
        print('recive command level message---> Command: %s' % command)
        command_exe(command)
        continue
    
#self_update()
#random_walk()
#state_report()
s.close()

