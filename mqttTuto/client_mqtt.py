import socket
import time
from random import randrange, uniform, randint
c = socket.socket()

c.connect(('localhost',9876))
t_end = time.time() + 60 * 1
# name = "shyam"

def fn():
    x = randint(1,3)
    if(x==1):
        #temp
        val=uniform(273,373)
        return val
    elif(x==2):
        #humi
        val=uniform(30,60)
        return val
    else:
        #general
        val=uniform(0,10)
        return val



while time.time() < t_end:
    # val = uniform(0, 15)
    name = str(fn())
    # print(randrange(10))
    c.send(bytes(name,'utf-8'))
    print(c.recv(1024).decode())
    time.sleep(1)
