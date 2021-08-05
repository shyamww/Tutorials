import paho.mqtt.publish as publish
import socket
import json
import time

UDP_MQTT_PUBLISH_PORT = 12345
UDP_SERVER_IP = 'localhost'

# s= socket.socket()
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      # For UDP

print('Socket created')
sock.bind((UDP_SERVER_IP , UDP_MQTT_PUBLISH_PORT))

print('waiting for clients....') 

# to publish data to mqtt topic
def mqtt_publisher(received_data,payload_json):
    payload = json.dumps(payload_json)
    try:
        print("Just published: "+ received_data, payload)
        publish.single(received_data,payload,hostname="mqtt.eclipseprojects.io")
    except Exception as e:
        print("error {0}".format(e))

# c, addr = s.accept()
 
while True:
    # name = c.recv(8192).decode()
    # received_data = json.loads(name)

    data,addr = sock.recvfrom(8192)	
    received_data = json.loads(data)
    topic_name=received_data["Topic"]
    data_for_this_topic = received_data["Data"]

    if(type(data_for_this_topic) != type("string")):
        data_for_this_topic=str(data_for_this_topic)

    if(len(topic_name)>0 and len(data_for_this_topic)>0):
        c.send(bytes((str(data_for_this_topic) +' added to '+str(topic_name) ), 'utf-8'))
        mqtt_publisher(topic_name,data_for_this_topic)
    else:
        print("Nothing Published")
        c.send(bytes('Topic, data are empty', 'utf-8'))
    # time.sleep(1)
