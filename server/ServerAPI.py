import json
from flask import Flask, abort, request
from flask.json import jsonify

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

# class Data(Resource):
#     def get(self):
#         parser = reqparse.RequestParser() 
        
#         parser.add_argument('IdDrone', required=True) 
#         parser.add_argument('Position', required=True)
#         parser.add_argument('', required = True)
#         parser.add_argument('IdClient', required=True)
        
# api.add_resource(Data, "/data")
# if __name__ == '__main__':
@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/v1/drone', methods=['POST'])
def api_POST():
    if not request.json or not 'IdDrone' in request.json:
        abort(400)
    drone = {
        'IdDrone': request.json['IdDrone'],
        'Status': request.json['Status'],
        'Position': request.json['Position'],
        'Temperature': request.json['Temperature'],
        'Velocity': request.json['Velocity'],
        'Battery': request.json['Battery'],
        'Time': request.json['Time'],
    }
    drones.append(drone)
    return jsonify({'drone':drone}),201

@app.route('/api/v1/drones', methods=['GET'])
def api_GetAll():
    return jsonify({'drones':drones})
if __name__ == '__main__':
    app.run(debug=True)
