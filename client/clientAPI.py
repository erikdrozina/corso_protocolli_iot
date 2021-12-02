import datetime
import json
import time
import random as rnd
import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(f'{dir_path}/../common')
from requests_manager import send_request
from sensors.sensor_battery import GetBattery
from sensors.sensor_position import GetPosition
from sensors.sensor_temperature import GetTemperature
from sensors.sensor_velocity import GetVelocity


# obtain data from virtual sensors
def get_data(id):
    # get date and time from datetime
    now = datetime.datetime.now()
    # set randomly the status of the drone as it's "virtual", if on or off
    tmp = rnd.randint(0, 1)
    data = {
        "IdDrone": id,
        "Status": tmp,
        "Position": GetPosition(id),
        "Temperature": GetTemperature(id),
        # check if tmp, which represent the status of the drone, is 1 (on) if it's on it gets it current velocity
        "Velocity": GetVelocity(id) if tmp else 0,
        "Battery": GetBattery(id),
        "Time": now.strftime("%Y-%m-%d_%H:%M:%S"),
    }
    return data


# POST /v1/drone/drone_id
def post_droneById(drone_id):
    global url
    datajson = json.dumps(get_data(drone_id))
    s_code = send_request('POST', f"{url}/v1/drone", datajson)
    return print(f"CODE {s_code}, {datajson}")


if __name__ == "__main__":
    # server url
    url = "http://192.168.104.55:5000/api"
    # drone id that sends data to the server
    drone_id = 1

    while 1:
        post_droneById(drone_id)
        time.sleep(5)
