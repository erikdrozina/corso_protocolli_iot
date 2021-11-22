import json
from flask import Flask, abort, request
from flask.json import jsonify

# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
# link documentazione tutorial
app = Flask(__name__)


drones = [
    {
        'IdDrone':0,
        'Position': 0,
        'IdClient': 0
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

@app.route('/api/v1/resources/drone/', methods=['POST'])
def api_POST():
    if not request.json or not 'IdDrone' in request.json:
        abort(400)
    drone = {
        'IdDrone': request.json['IdDrone'],
        'Position': request.json['Position'],
        'IdClient': request.json['IdClient']
    }
    drones.append(drone)
    return jsonify({'drone':drone}),201

@app.route('/api/v1/drones', methods=['GET'])
def api_GetAll():
    return jsonify({'drones':drones})
if __name__ == '__main__':
    app.run(debug=True)
