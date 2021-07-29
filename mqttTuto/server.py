import socket
import time


s= socket.socket()
print('Socket created')
s.bind(('localhost', 9876))

s.listen(5)
print('waiting for clients....')

t_end = time.time() + 10 * 1
c, addr = s.accept()
while time.time() < t_end:
    name = c.recv(1024).decode()
    print("connected with", addr, name)
    print(type(name))
    val = int(name)
    print(type(val))
    # if(name==1):
    #     c.send(bytes('Welcome to mqtt server for 1', 'utf-8'))
    # if(name==2):
    #     c.send(bytes('Welcome to mqtt server for 2', 'utf-8'))
    # else:
    #     c.send(bytes('Welcome to mqtt server for other', 'utf-8'))
    
c.close()