import json
from flask import Flask
from flask_restful import Resource,Api, reqparse

app = Flask(__name__)
api = Api(app)

class Data(Resource):
    def get(self):
        parser = reqparse.RequestParser() 
        
        parser.add_argument('IdDrone', required=True) 
        parser.add_argument('Position', required=True)
        parser.add_argument('', required = True)
        parser.add_argument('IdClient', required=True)
        
api.add_resource(Data, "/data")
if __name__ == '__main__':
    app.run()