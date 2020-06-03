# -*- encoding: utf-8 -*-
from flask_migrate import MigrateCommand
from flask_script import Manager, Server, Shell

from flask_web import create_app, get_api_route

app = create_app('testing')

api_rules = get_api_route(app)


# 注册服务的路由信息到api网关
def register_api():
    return str(api_rules)


def make_shell_context():
    return dict(app=app)


app.add_url_rule("/v1/route/info", view_func=register_api, methods=["GET"])

manager = Manager(app)

# 命令行工具
manager.add_command('shell', Shell(make_context=make_shell_context))
# 操作数据库迁移
manager.add_command('db', MigrateCommand)
# 添加管理命令
manager.add_command('runserver', Server(host='0.0.0.0', port='8080'))

if __name__ == '__main__':
    manager.run()
