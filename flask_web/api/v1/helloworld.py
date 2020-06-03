# -*- encoding: utf-8 -*-
import logging

from flask import request
from flask_restful import Resource

LOGGER = logging.getLogger(__name__)


class HelloWorld(Resource):
    def get(self):
        return 'hello world1'

    def post(self):
        json_data = request.get_json()
        LOGGER.warning(json_data)
