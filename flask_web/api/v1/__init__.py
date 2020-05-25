# -*- encoding: utf-8 -*-  
from flask import Blueprint
from flask_restful import Api

from flask_web.api.v1.helloworld import HelloWorld
from flask_web.api.v1.user import User

api_v1_bp = Blueprint("api_v1", __name__)
api = Api(api_v1_bp, catch_all_404s=True)

api.add_resource(HelloWorld, '/helloworld')
api.add_resource(User, '/user/<int:pk>')
