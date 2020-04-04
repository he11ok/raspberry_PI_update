import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('',5000))
while True:
    data, addr = s.recvfrom(1024)
    print('received message:{0} from PORT {1} on {2}'.format(data.decode(),addr[1],addr[0]))
    if data.decode() == 'close':
        print('close the receiver')
        break
s.close()
