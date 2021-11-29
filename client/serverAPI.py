import json
from flask import Flask, abort, request
from flask.json import jsonify

# server api on the drone
app = Flask(__name__)
commands = []


@app.route('/')
def index():
    return "Server to receive commands"


@app.route('/api/v1/command', methods=['POST'])
def api_POST():
    if not request.json:
        abort(400)
    reqjson = json.loads(request.json)
    if reqjson['Command'] != "":
        command = {
            "IdDrone": reqjson['IdDrone'],
            "Command": reqjson['Command'],
            "Time": reqjson['Time'],
        }
        commands.append(command)
        return jsonify({'command': command}), 201
    else:
        return 200


@app.route('/api/v1/commands', methods=['GET'])
def api_GetAll():
    return jsonify({'commands': commands})


# start server on drone
app.run(host='0.0.0.0', port=5010)
