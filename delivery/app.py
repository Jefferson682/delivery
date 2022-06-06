from flask import Flask
from .ext import site, debug, config


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    debug.init_app(app)
    site.init_app(app)
    return app
