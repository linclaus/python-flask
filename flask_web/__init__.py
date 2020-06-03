# -*- encoding: utf-8 -*-
from flask import Flask
from flask_migrate import Migrate

from common.extensions import db
from conf.default import config
from flask_web.api import api_v1_bp, VERSIONS_ALLOWED, API_VERSION_MAPPING


def create_app(config_name):
    """应用工厂方法

    :param config_name:
    :return: flask_app
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    _register_blueprint(app)
    # _register_extensions(app)

    return app


def _register_extensions(app):
    """注册扩展模块

    :param app:
    :return:
    """
    # cors = CORS()
    migrate = Migrate()
    # 跨域请求设置
    # cors.init_app(app, resources=app.config['CORS_RESOURCES'], supports_credentials=True)
    # compare_type默认为False,不检测字段数据变化
    migrate.init_app(app, db, compare_type=False)

    # 初始化SQLAlchemy
    with app.app_context():
        db.init_app(app)
        db.create_all()


def _register_blueprint(app):
    """注册不同类型的API蓝图：1.根据API版本；2.根据自定义API

    :param app: app_context
    :return: None
    """

    # 自动根据API版本注册蓝图
    for version in VERSIONS_ALLOWED:
        app.register_blueprint(
            API_VERSION_MAPPING[version], url_prefix=_get_url_prefix(version))


def _get_url_prefix(version):
    """根据API版本返回URL路径前缀

    :param version: 版本号，字符型
    :return: str, url路径
    """
    return '/api/v{0}'.format(str(version))


# 提取需要注册到网关上的路由信息
def get_api_route(app):
    rules = app.url_map.iter_rules()
    route_list = []
    for rule in rules:
        methods = rule.methods
        for method in methods:
            if method == "OPTIONS" or method == "HEAD":
                continue
            url = rule.rule
            if "/version" in url or "/healthcheck" in url:
                continue
            url = str(url).replace("/<", "/{").replace(">", "}")
            route_list.append({"methods": method, "url": url, "host": "", "noauth": False})
    return {"RouteInfo": {"alarm-api": route_list}}
