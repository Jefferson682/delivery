from delivery.ext.db import db
from delivery.ext.site.models import models # noqa

def init_app(app):
    @app.cli.command()
    def create_db():
        """Create a new database"""
        db.create_all()