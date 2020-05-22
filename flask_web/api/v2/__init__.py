# -*- encoding: utf-8 -*-  
from flask import Blueprint
from flask_restful import Api

from flask_web.api.v2.helloworld import HelloWorld

api_v2_bp = Blueprint("api_v2", __name__)
api = Api(api_v2_bp, catch_all_404s=True)

api.add_resource(HelloWorld, '/helloworld')
