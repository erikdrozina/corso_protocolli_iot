import datetime
import random as rnd
import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(f'{dir_path}/../client')
from sensors.sensor_battery import GetBattery
from sensors.sensor_velocity import GetVelocity
from sensors.sensor_position import GetPosition
from sensors.sensor_temperature import GetTemperature


# obtain data from virtual sensors
def get_sensors_data(id):
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
    # if the drone is on also return True, otherwise return False
    # it's used to check if the drone is on or off
    if tmp == 1:
        return data, True
    else:
        return data, False


# obtain data from virtual sensors
def get_command_data(id):
    # all possibl commands
    command_list = ['start', 'stop', 'up', 'down',
                'forward', 'back', 'left', 'right']
    # get date and time from datetime
    now = datetime.datetime.now()
    # set randomly the status of the drone as it's "virtual", if on or off
    data = {
        "IdDrone": id,
        "Command": command_list[rnd.randint(0, len(command_list)-1)],
        "Time": now.strftime("%Y-%m-%d_%H:%M:%S"),
    }
    return data
