import json
import time
import os
import sys
import yaml
import pika
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(f'{dir_path}/../common')
from generate_data import get_sensors_data  # noqa: E402


def getCredentials():
    credentials = yaml.safe_load(open('./client/credentials.yaml'))
    user = credentials['user']
    pwd = credentials['pwd']
    return user, pwd


# send sensors data to broker
def publish_droneById(drone_id):
    data, status = get_sensors_data(drone_id)
    datajson = json.dumps(data)
    channel.basic_publish(exchange='', routing_key='test', body=datajson)
    print("Message sent to consumer")
    if status:
        time.sleep(5)
    else:
        print("Drone status: offline")
        time.sleep(10)


if __name__ == "__main__":
    user, pwd = getCredentials()
    credentials = pika.PlainCredentials(user, pwd)
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='stingray.rmq.cloudamqp.com', credentials=credentials, virtual_host='akdjroei'))  # Connect to CloudAMQP
    channel = connection.channel()  # start a channel
    channel.queue_declare(queue='test')

    drone_id = 1
    while 1:
        publish_droneById(drone_id)
