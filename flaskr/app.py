from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class ahlijawatankuasa(Resource):
	def get(self):
		return {"api": True}

api.add_resource(ahlijawatankuasa, '/ajk')

app.run(port=5000, debug=True)
