'''
Basic MQTT testing
Publisher Process
'''

# pub.py
import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("127.0.0.1", 1883)

for i in range(5):
    msg = f"Messaggio numero {i}"
    client.publish("test/topic", msg)
    print(f"[PUB] {msg}")
    time.sleep(1)

client.disconnect()
