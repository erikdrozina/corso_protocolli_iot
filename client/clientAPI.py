import datetime
import time
import random as rnd
import requests as rq
from sensors.sensor_battery import GetBattery
from sensors.sensor_position import GetPosition
from sensors.sensor_temperature import GetTemperature
from sensors.sensor_velocity import GetVelocity

# example drone data
# data = {
#     "Status": 0,
#     "Position": [0, 0, 0],
#     "Temperature": 0,
#     "Velocity": 0,
#     "Battery": 0,
#     "LastUpdate": '1970-01-01_00:00:00'
# }


def patch_droneById(id):
    global url
    # get date and time from datetime
    now = datetime.datetime.now()
    # set randomly the status of the drone as it's "virtual", if on or off
    data = {
        "Status": rnd.randint(0, 1),
        "Position": GetPosition(id),
        "Temperature": GetTemperature(id),
        "Velocity": GetVelocity(id),
        "Battery": GetBattery(id),
        "LastUpdate": now.strftime("%Y-%m-%d_%H:%M:%S"),
    }
    rq.patch(f"{url}/v1/drone/{id}", data)
    return print(data)


if __name__ == "__main__":
    # server url
    url = "http://localhost:5000/api"
    while 1:
        patch_droneById(1)
        time.sleep(5)
