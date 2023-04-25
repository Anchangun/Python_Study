import paho.mqtt.client as mqtt

#broker setting
broker_address = "localhost"  # MQTT broker ip
broker_port = 1883  # MQTT broker default port

# Mqtt recive callback function 
def on_message(client, userdata, message):
    print("Received message: " + message.payload.decode())

# MQTT Clinet Create
client = mqtt.Client()
client.on_message = on_message

# MQTT Broker Connect 
client.connect(broker_address, broker_port)
client.loop_start()
print("hi")
# Topic Subscribe
client.subscribe("/map_server/map/response")  #Topic Setting

# Message Wating loop
while True:
    pass

# MQTT Client Disconnect
client.loop_stop()
client.disconnect()
