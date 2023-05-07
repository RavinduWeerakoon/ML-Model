from flask import Flask, jsonify,request
from flask_restful import Resource, Api
from flask_cors import CORS
from recommender import get_locations, rec_plan
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
    def get(self):
        data = request.args.get('data')
        days = request.args.get('days')
        # do something with the data and days parameters to generate a plan
     
        return jsonify({'data': rec_plan(data, int(days))})
    


api.add_resource(status, '/')
api.add_resource(Destination, '/get/<string:a>')
api.add_resource(Plan, '/getPlan')

if __name__ == '__main__':
    app.run()