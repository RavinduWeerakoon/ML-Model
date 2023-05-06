from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from recommender import get_locations
app = Flask(__name__)
api = Api(app)
CORS(app)




class status (Resource):
    def get(self):
        try:
            return {'data': 'Api is Running'}
        except:
            return {'data': 'An Error Occurred during fetching Api'}


class Destination(Resource):
    def get(self, a):
        return jsonify({'data': get_locations(a)})
    
class Plan(Resource):
    def get(self, a):
        return jsonify({'data':'z7Dd2OYLSB1XHnENED68'})


api.add_resource(status, '/')
api.add_resource(Destination, '/get/<string:a>')
api.add_resource(Plan, '/plan/<string:a>')

if __name__ == '__main__':
    app.run()