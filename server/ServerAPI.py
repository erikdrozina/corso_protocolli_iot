import json
from flask import Flask, abort, request
from flask.json import jsonify
import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(f'{dir_path}/../common')
from database_actions import insert_drone_data

# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
# link documentazione tutorial
app = Flask(__name__)

drones = []


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/api/v1/drone', methods=['POST'])
def api_POST():
    if not request.json or not 'IdDrone' in request.json:
        abort(400)
    reqjson = json.loads(request.json)
    drone = {
        'IdDrone': reqjson['IdDrone'],
        'Status': reqjson['Status'],
        'Position': reqjson['Position'],
        'Temperature': reqjson['Temperature'],
        'Velocity': reqjson['Velocity'],
        'Battery': reqjson['Battery'],
        'Time': reqjson['Time']
    }
    insert_drone_data(drone)
    drones.append(drone)
    return jsonify({'drone': drone}), 201


@app.route('/api/v1/drones', methods=['GET'])
def api_GetAll():
    return jsonify({'drones': drones})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
