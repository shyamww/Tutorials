import socket
import time
import random
import json
import string
from random import randrange, uniform, randint

c = socket.socket()

c.connect(('localhost',9876))

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
    return res

def fn_d(name):
    switcher = {
        "TEMPERATURE": uniform(273,373),
        "HUMIDITY": {
            "name":"John",
            "age":30,
            "cars":["Ford", "BMW", "Fiat"]
            },
        "GENERAL": fn_random_string()
    }
    return switcher.get(name, "nothing")
    # if(name == "TEMPERATURE"):
    #     y= {
    #         "T":"2121"
    #     }
    #     return y
    # else:
    #     y= {
    #         "name":"John",
    #         "age":30,
    #         "cars":["Ford", "BMW", "Fiat"]
    #         }
    #     return y

def fn_topic():
    topic_list = ["TEMPERATURE", "HUMIDITY", "GENERAL"]
    return random.choice(topic_list)

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

    c.send(bytes(y,'utf-8'))
    print(c.recv(8192).decode())
    time.sleep(1)




