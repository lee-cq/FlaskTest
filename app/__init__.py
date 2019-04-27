"""
终端命令 :export FLASK_ENV=development; flask run
"""
from flask import Flask


def create_app():
    app = Flask(__name__)
    # 注册蓝图
    from .main import main as bp_main

    app.register_blueprint(bp_main)
    app.debug = True
    return app
