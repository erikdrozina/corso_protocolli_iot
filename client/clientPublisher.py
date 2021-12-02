
from paho.mqtt.client import Client
import json
import time
import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(f'{dir_path}/../common')
from generate_data import get_sensors_data


def publish_droneById(drone_id):
    global url
    datajson = json.dumps(get_sensors_data(drone_id))
    client.publish(topic=f"iot/drone_{drone_id}/sensors", payload=datajson)


if __name__ == "__main__":

    drone_id = 1
    client = Client(client_id=f"{drone_id}")
    client.connect("192.168.104.150")

    while 1:
        publish_droneById(drone_id)
        time.sleep(5)
