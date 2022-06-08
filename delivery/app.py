from flask import Flask

from .ext import admin, auth, cli, config, db, hooks, migrate, site, toolbar


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    return app
