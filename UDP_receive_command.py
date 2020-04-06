import socket

def self_update():
    print('self_update command reviced\n'\
          +'The RPI is downloading the codes from Github and try to run them ...\n')
    
def random_walk():
    print('random_walk command is received\n'\
          + 'start random walk ...\n')
    
def state_report():
    print('state_report command received\n'\
          + 'report the state of the robot ...\n')
    
def command_exe(command):
    #command dictionary, use comma to seperate
    {
        'self_update':self_update(),
        'random_walk':random_walk(),
        'state_report':state_report()
    }[command]


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
    
#self_update()
#random_walk()
#state_report()
s.close()