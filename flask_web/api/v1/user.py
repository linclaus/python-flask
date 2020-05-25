# -*- encoding: utf-8 -*-
from flask_restful import Resource

from flask_web import model
from flask_web.schema import user_schema


class User(Resource):
    def get(self, pk):
        try:
            user = model.User.query.get(str(pk))
            result = user_schema.dump(user)
            return {'user': result}
        except Exception as e:
            print(e)
            return {'error': 404}

    def post(self):
        try:
            pass
        except Exception as e:
            pass

    def put(self, pk):
        try:
            pass
        except Exception as e:
            pass
