# -*- encoding: utf-8 -*-
from marshmallow import Schema, fields, validate


class User(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))


user_schema = User()
