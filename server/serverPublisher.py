from paho.mqtt.client import Client
import json
import time
import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(f'{dir_path}/../common')
from generate_data import get_command_data  # noqa: E402


# send sensors data to broker
def publish_droneById(drone_id):
    # obtain command
    datajson = json.dumps(get_command_data(drone_id))
    topic = f"iot/drone/{drone_id}/command"
    client.loop_start()
    # publish data to the topic declared above with qos 2
    client.publish(topic, datajson, 2)
    print(f"Sent '{datajson}' to topic {topic}")


if __name__ == "__main__":
    drone_id = 1
    # set the device name, must be unique
    client = Client(client_id=f"{drone_id}")
    # connect to the broker
    client.connect("192.168.104.150")

    while 1:
        publish_droneById(drone_id)
        time.sleep(5)
