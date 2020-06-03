# -*- encoding: utf-8 -*-
from flask import request
from flask_restful import Resource


class HelloWorld(Resource):
    def get(self):
        return 'hello world1'

    def post(self):
        json_data = request.get_json()
        print(json_data)
