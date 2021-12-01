import json
from flask import Flask, abort, request
from flask.json import jsonify
import psycopg2

# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
# link documentazione tutorial
app = Flask(__name__)


drones = [
    {
        "IdDrone": 0,
        "Status": 0,
        "Position": [0, 0, 0],
        "Temperature": 0,
        "Velocity": 0,
        "Battery": 0,
        "Time": '1970-01-01_00:00:00'
    }
]


def insert(drone):
    conn = None
    try:
        print("Connecting to DB")
        conn = psycopg2.connect(
            host="192.168.104.150",
            port="5432",
            database="iotdb",
            user="iot",
            password="iot")
        cursor = conn.cursor()
        cursor.execute("INSERT")  # query
        print("inserted")
        conn.commit()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


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
    insert(drone)
    drones.append(drone)
    return jsonify({'drone': drone}), 201


@app.route('/api/v1/drones', methods=['GET'])
def api_GetAll():
    return jsonify({'drones': drones})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
