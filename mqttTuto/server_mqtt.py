import paho.mqtt.client as mqtt
import socket

import time

from random import randrange, uniform
mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker)

s= socket.socket()
print('Socket created')
s.bind(('localhost', 9876))

s.listen(10)
print('waiting for clients....')

t_end = time.time() + 60 * 1
c, addr = s.accept()
while time.time() < t_end:
    name = c.recv(1024).decode()
    val = float(name)
    # print("connected with", addr, name)
    if(val <= 373 and val >= 273):
        c.send(bytes('Welcome to mqtt server for TEMPERATURE', 'utf-8'))
        client.publish("TEMPERATURE", val)
        print("Just published " + str(val) + " to Topic TEMPERATURE")
    elif(val <= 60 and val >=30):
        c.send(bytes('Welcome to mqtt server for HUMIDITY', 'utf-8'))
        client.publish("HUMIDITY", val)
        print("Just published " + str(val) + " to Topic HUMIDITY")
    else:
        c.send(bytes('Welcome to mqtt server for GENERAL', 'utf-8'))
        client.publish("GENERAL", val)
        print("Just published " + str(val) + " to Topic GENERAL")
    time.sleep(1)
    

c.close()