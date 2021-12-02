from paho.mqtt.client import Client

client = Client(client_id="controlCenter")
client.connect("192.168.104.150")

client.subscribe('iot/drone_1/sensors')

def on_message(client, userdata,message):
    print("message received " ,str(message.payload.decode("utf-8")))


def run():
    client.on_message=on_message
    client.loop_forever()

run()