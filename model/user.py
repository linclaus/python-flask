# -*- encoding: utf-8 -*-
from common.extensions import db
from common.mixins import DBMixin


class User(DBMixin, db.Model):
    id = db.Column(db.String(64), primary_key=True, nullable=False)
    name = db.Column(db.String(64), nullable=False)
