import paho.mqtt.publish as publish
import socket
import json
import time
from random import randrange, uniform 

s= socket.socket()
print('Socket created')
s.bind(('localhost', 9876))
s.listen(10)
print('waiting for clients....') 

# to publish data to mqtt topic
def mqtt_publisher(topicName,payload_json):
    payload = json.dumps(payload_json)
    # print("payload is: ",payload, type(payload))

    try:
        print(topicName, payload)
        publish.single(topicName,payload,hostname="mqtt.eclipseprojects.io")
    except Exception as e:
        print("error {0}".format(e))

# mqtt_publisher("CAT","meauu")


c, addr = s.accept()

t_end = time.time() + 60 * 1
while time.time() < t_end:
# while True:
    name = c.recv(8192).decode()
    y = json.loads(name)
    z=y["Topic"]
    val = y["Data"]
    c.send(bytes((str(val) +' added to '+str(z) ), 'utf-8'))
    mqtt_publisher(z,val)
    time.sleep(1)

c.close()