# -*- encoding: utf-8 -*-  
# 允许访问的API版本
from flask_web.api.v1 import api_v1_bp
from flask_web.api.v2 import api_v2_bp

VERSIONS_ALLOWED = ['1', '2']

# API版本映射
API_VERSION_MAPPING = {
    '1': api_v1_bp,
    '2': api_v2_bp
}
