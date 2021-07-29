import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Smartphone2")
client.connect(mqttBroker)

print("Fetching TEMPERATURE....")

client.loop_start()
client.subscribe("TEMPERATURE")
client.on_message = on_message
time.sleep(50)
client.loop_end()