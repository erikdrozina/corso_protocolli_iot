import json
import time
import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(f'{dir_path}/../common')
from requests_manager import send_request
from generate_data import get_sensors_data


# POST /v1/drone
def post_droneById(drone_id):
    global url
    datajson = json.dumps(get_sensors_data(drone_id))
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
