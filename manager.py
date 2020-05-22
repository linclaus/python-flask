# -*- encoding: utf-8 -*-
from flask_script import Manager, Server, Shell

from flask_web import create_app, get_api_route

app = create_app()

api_rules = get_api_route(app)


# 注册服务的路由信息到api网关
def register_api():
    return str(api_rules)


app.add_url_rule("/v1/route/info", view_func=register_api, methods=["GET"])

manager = Manager(app)

# manager.add_command('runserver', Server(host='localhost', port='8080'))

if __name__ == '__main__':
    manager.run()
