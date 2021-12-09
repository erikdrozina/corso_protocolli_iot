from paho.mqtt.client import Client
import json
import time
import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(f'{dir_path}/../common')
from generate_data import get_sensors_data

# send sensors data to broker
def publish_droneById(drone_id):
    data, status = get_sensors_data(drone_id)
    datajson = json.dumps(data)
    topic = f"iot/drone/{drone_id}/sensors"
    client.publish(topic, datajson, 0)
    print(f"Sent '{datajson}' to topic {topic}")
    if status: 
        time.sleep(5)
    else:
        print("Drone status: offline")
        time.sleep(10)


if __name__ == "__main__":
    drone_id = 1
    client = Client(client_id=f"drone_{drone_id}")
    client.connect("192.168.104.150")

    while 1:
        publish_droneById(drone_id)