import random
import requests
from sensors.sensor_battery import GetBattery
from sensors.sensor_position import GetPosition
from sensors.sensor_temperature import GetTemperature
from sensors.sensor_velocity import GetVelocity

import sensors

# server url
url = "http://localhost:5000/api"

# drones available
n_drones = 10


# example drone data
# data = {
#     "Status": 0,
#     "Position": [0, 0, 0],
#     "Temperature": 0,
#     "Velocity": 0,
#     "Battery": 0,
# }


def post_droneById(id):
    # set randomly the status of the drone as it's "virtual", if on or off
    drone_status = random.randint(0, 1)
    data = {}
    if id < n_drones and drone_status:
        data = {
            "Status": drone_status,
            "Position": GetPosition(id),
            "Temperature": GetTemperature(id),
            "Velocity": GetVelocity(id),
            "Battery": GetBattery(id),
        }
    return print(data)


if __name__ == "__main__":
    post_droneById(1)
