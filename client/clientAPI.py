import datetime
import json
import time
import random as rnd
import requests as rq
from colorama import Fore
from sensors.sensor_battery import GetBattery
from sensors.sensor_position import GetPosition
from sensors.sensor_temperature import GetTemperature
from sensors.sensor_velocity import GetVelocity

# example drone data
# data = {
#     "IdDronw": 0
#     "Status": 0,
#     "Position": [0, 0, 0],
#     "Temperature": 0,
#     "Velocity": 0,
#     "Battery": 0,
#     "Time": '1970-01-01_00:00:00'
# }


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


# handle the requests and eventually its exceptions
def send_request(method, url, resdata={}):
    try:
        # each method return a status code
        if method == 'GET':
            tmp = rq.get(url)
            return tmp.status_code
        elif method == 'POST':
            tmp = rq.post(url, json=resdata)
            return tmp.status_code
        elif method == 'PUT':
            tmp = rq.put(url, json=resdata)
            return tmp.status_code
        elif method == 'PATCH':
            tmp = rq.patch(url, json=resdata)
            return tmp.status_code
        else:
            raise SystemExit(rq.exceptions.RequestException)
    except rq.exceptions.Timeout:
        print(Fore.RED+"Connection timeout, retrying..."+Fore.RESET)
        send_request(method, url, data="")
    except rq.exceptions.TooManyRedirects:
        print(
            Fore.RED+"Bad url, check it is indeed correct or try a different one"+Fore.RESET)
    except rq.exceptions.ConnectionError:
        print(Fore.RED+"Cannot connect to server, better luck next time..."+Fore.RESET)
    except rq.exceptions.RequestException as e:
        raise SystemExit(e)


# POST /v1/drone/drone_id
def post_droneById(drone_id):
    global url
    res_data = get_data(drone_id)
    datajson = json.dumps(res_data)
    s_code = send_request('POST', f"{url}/v1/drone", datajson)
    return print(f"CODE {s_code}, {res_data}")


if __name__ == "__main__":
    # server url
    url = "http://localhost:5000/api"
    # drone id that sends data to the server
    drone_id = 1

    while 1:
        post_droneById(drone_id)
        time.sleep(5)
