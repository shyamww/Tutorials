import paho.mqtt.publish as publish
import socket
import json
import time

UDP_MQTT_PUBLISH_PORT = 12345
UDP_SERVER_IP = 'localhost'

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

while True:
    packet_from_socket = sock.recvfrom(8192)	
    data_received = packet_from_socket[0]
    data = data_received.decode()
    addr = packet_from_socket[1]
    received_data = json.loads(data) 

    topic_name = received_data["Topic"]
    data_for_this_topic = received_data["Data"]

    if(type(data_for_this_topic) != type("string")):
        data_for_this_topic = str(data_for_this_topic)

    if(len(topic_name)>0 and len(data_for_this_topic)>0):
        reply = data_for_this_topic + " added to topic " + topic_name
        sock.sendto(reply.encode(), addr)
        mqtt_publisher(topic_name,data_for_this_topic)
    else:
        print("Nothing Published")
        reply = "Topic, data are empty"
        sock.sendto(reply.encode(), addr)




  
