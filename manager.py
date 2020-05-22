# -*- encoding: utf-8 -*-
from flask import jsonify
import json

from flask_web import create_app, get_api_route

app = create_app()

api_rules = get_api_route(app)


# 注册服务的路由信息到api网关
def register_api():
    return str(api_rules)


app.add_url_rule("/v1/route/info", view_func=register_api, methods=["GET"])

if __name__ == '__main__':
    app.run()
