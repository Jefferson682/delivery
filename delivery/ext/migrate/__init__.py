from flask_migrate import Migrate
from delivery.ext.site.models import models # noqa
from delivery.ext.db import db

migrate = Migrate()

def init_app(app):
    migrate.init_app(app, db)