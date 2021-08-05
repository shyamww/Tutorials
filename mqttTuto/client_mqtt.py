import socket
import time
import random
import json
import string
from random import randrange, uniform, randint

# c = socket.socket()
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
udp_host = socket.gethostname()	
udp_port = 12345			    

# c.connect(('localhost',9876))

# name = "shyam"

def fn():
    x = randint(1,3)
    if(x==1):
        #temp
        val=uniform(273,373)
        return val
    elif(x==2):
        #humi
        val=randrange(30,60)
        return val
    else:
        #general
        val=uniform(0,10)
        return val



def fn_random_string():
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
    # res = "abcdefghijklmnopqrstuvwxyaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyaaabbbcccdddeeefffggghhhiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxyyyaaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyaaaaabbbbbcccccdddddeeeeefffffggggghhhhhiiiiijjjjjkkkkklllllmmmmmnnnnnooooopppppqqqqqrrrrrssssstttttuuuuuvvvvvwwwwwxxxxxyyyyyaaaaaabbbbbbccccccddddddeeeeeeffffffgggggghhhhhhiiiiiijjjjjjkkkkkkllllllmmmmmmnnnnnnooooooppppppqqqqqqrrrrrrssssssttttttuuuuuuvvvvvvwwwwwwxxxxxxyyyyyyaaaaaaabbbbbbbcccccccdddddddeeeeeeefffffffggggggghhhhhhhiiiiiiijjjjjjjkkkkkkklllllllmmmmmmmnnnnnnnooooooopppppppqqqqqqqrrrrrrrssssssstttttttuuuuuuuvvvvvvvwwwwwwwxxxxxxxyyyyyyyaaaaaaaabbbbbbbbccccccccddddddddeeeeeeeeffffffffgggggggghhhhhhhhiiiiiiiijjjjjjjjkkkkkkkkllllllllmmmmmmmmnnnnnnnnooooooooppppppppqqqqqqqqrrrrrrrrssssssssttttttttuuuuuuuuvvvvvvvvwwwwwwwwxxxxxxxxyyyyyyyyaaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeeeeeefffffffffggggggggghhhhhhhhhiiiiiiiiijjjjjjjjjkkkkkkkkklllllllllmmmmmmmmmnnnnnnnnnooooooooopppppppppqqqqqqqqqrrrrrrrrrssssssssstttttttttuuuuuuuuuvvvvvvvvvwwwwwwwwwxxxxxxxxxyyyyyyyyyaaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyy123456789112233445566778899111222333444555666777888999111122223333444455556666777788889999111112222233333444445555566666777778888899999111111222222333333444444555555666666777777888888999999111111122222223333333444444455555556666666777777788888889999999111111112222222233333333444444445555555566666666777777778888888899999999111111111222222222333333333444444444555555555666666666777777777888888888999999999111111111122222222223333333333444444444455555555556666666666777777777788888888889999999999"
    return res

def fn_d(name):
    switcher = {
        "TEMPERATURE": uniform(273,373),
        "HUMIDITY": {
            "name":"shyam",
            "age":30,
            "cars":["Ford", "BMW", "Fiat"]
            },
        "GENERAL": fn_random_string(),
        "": "testing default"
    }
    return switcher.get(name, "nothing")

def fn_topic():
    topic_list = ["TEMPERATURE", "HUMIDITY", "GENERAL", ""]
    return random.choice(topic_list)
    # return "GENERAL"


t_end = time.time() + 60 * 1
while time.time() < t_end:
# while True:
    # val = uniform(0, 15)
    topic_name=fn_topic()
    name = { 
        "Topic": topic_name,
        "Data": fn_d(topic_name)
    }
    # print(randrange(10))
    y=json.dumps(name) # json to string
    # c.send(bytes(y,'utf-8'))
    sock.sendto(y,(udp_host,udp_port))
    msgFromServer = sock.recvfrom(8192)
    msg = "Message from server {}".format(msgFromServer[0])
    # print(c.recv(8192).decode())
    print(msg)
    # time.sleep(1)




