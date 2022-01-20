from paho.mqtt.client import Client

# set the client name and set the session to ignore eventual queued messages
client = Client(client_id="ClientSub", clean_session=True)
# connect to the broker
client.connect("192.168.104.150")
# subscribe to the command topic with qos 2
client.subscribe('iot/drone/1/command', qos=2)


# when a message is published print it in the console
def on_message(client, userdata, message):
    print(f"Message received from topic {message.topic}: ", str(
        message.payload.decode("utf-8")))


def run():
    client.on_message = on_message
    # loop to continue listening to the topic
    client.loop_forever()


run()
