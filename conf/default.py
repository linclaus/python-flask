# -*- encoding: utf-8 -*-


class TestingConfig(object):
    DB_USER = "postgres"
    DB_PASSWORD = "postgres"
    HOST = "127.0.0.1"
    DB_NAME = "postgres"

    DEBUG = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://' + DB_USER + ':' + DB_PASSWORD + "@" + HOST + '/' + DB_NAME

# class TestingConfig(object):
#     DB_USER = "root"
#     DB_PASSWORD = "mysql"
#     HOST = "127.0.0.1"
#     DB_NAME = "test"
#
#     DEBUG = True
#
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + DB_USER + ':' + DB_PASSWORD + "@" + HOST + '/' + DB_NAME


config = {
    'testing': TestingConfig
}
