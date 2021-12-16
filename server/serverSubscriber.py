from paho.mqtt.client import Client

client = Client(client_id="ServerSub", clean_session=False)
client.connect("192.168.104.150")

# name of the topic the client subscribe to
client.subscribe('iot/drone/1/sensors', 1)


def on_message(client, userdata, message):
    print(f"Message received from topic {message.topic}: ", str(message.payload.decode("utf-8")))


def run():
    client.on_message = on_message
    client.loop_forever()


run()
