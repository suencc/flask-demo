#!/usr/bin/env python
# encoding: utf-8


"""
@version: 0.01
@author: zxs
@contact: xiaoshan.zhou@bayesba.com
@site: http://www.bayesba.com
@software: PyCharm
@file: __init__.py.py
@time: 17-7-18 下午6:06
"""

from flask import Flask, Blueprint
from flask_restaction import Api
from flask_sqlalchemy import SQLAlchemy

from config import config

app = Flask(__name__)
app.config.from_object(config["development"])

# 数据库连接
db = SQLAlchemy(app)

# 蓝图
apiv1bp = Blueprint('api', __name__)
front = Blueprint('front', __name__)

# 过滤器

# view

# Flask-restAction 创建API,并且给API添加资源
apiv1 = Api(apiv1bp)
from app.apis.v1.demo import Hello
apiv1.add_resource(Hello)
apiv1.add_resource(type('Docs', (), {'get': apiv1.meta_view}))

# 蓝图添加路由
app.register_blueprint(front, url_prefix='/')
app.register_blueprint(apiv1bp, url_prefix='/v1')
# app.register_blueprint(apiv1bp, url_prefix='/v1')