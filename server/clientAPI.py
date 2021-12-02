import time
import random as rnd
import datetime
import json
import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(f'{dir_path}/../common')
from requests_manager import send_request
from genereate_data import get_command_data


# POST /v1/drone/drone_id
def post_command(drone_id):
    global url
    datajson = json.dumps(get_command_data(drone_id))
    s_code = send_request('POST', f"{url}/v1/command", datajson)
    return print(f"CODE {s_code}, {datajson}")


if __name__ == "__main__":
    # server url
    url = "http://192.168.104.150:5010/api"
    # drone id that sends data to the server
    drone_id = 1

    while 1:
        post_command(drone_id)
        time.sleep(5)
