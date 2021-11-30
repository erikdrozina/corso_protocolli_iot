import time
import random as rnd
import datetime
import json
import sys
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(f'{dir_path}/../common')
from requests_manager import send_request
# all possibl commands
command_list = ['start', 'stop', 'up', 'down',
                'forward', 'back', 'left', 'right']


# obtain data from virtual sensors
def get_data(id):
    # get date and time from datetime
    now = datetime.datetime.now()
    # set randomly the status of the drone as it's "virtual", if on or off
    data = {
        "IdDrone": id,
        "Command": command_list[rnd.randint(0, len(command_list)-1)],
        "Time": now.strftime("%Y-%m-%d_%H:%M:%S"),
    }
    return data


# POST /v1/drone/drone_id
def post_command(drone_id):
    global url
    datajson = json.dumps(get_data(drone_id))
    s_code = send_request('POST', f"{url}/v1/command", datajson)
    return print(f"CODE {s_code}, {datajson}")


if __name__ == "__main__":
    # server url
    url = "http://localhost:5010/api"
    # drone id that sends data to the server
    drone_id = 1

    while 1:
        post_command(drone_id)
        time.sleep(5)
