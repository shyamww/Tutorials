import socket
import time
import random
import json
import string
from random import randrange, uniform, randint

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
udp_host = 'localhost'
udp_port = 12345			    

def fn_random_string():
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
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

while True:
    topic_name=fn_topic()
    name = { 
        "Topic": topic_name,
        "Data": fn_d(topic_name)
    }
    
    y=json.dumps(name) # json to string
    sock.sendto(y.encode(),(udp_host,udp_port))
    d = sock.recvfrom(8192)
    reply = d[0]
    addr = d[1]

    print ('Server reply : ' + reply.decode())




