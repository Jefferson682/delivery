from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from delivery.ext.db import db
from delivery.ext.site.models.models import Address, Category, Item, Store

admin = Admin()

def init_app(app):
    admin.name = app.config.get("ADMIN_NAME", "Delivery")
    admin.template_mode = app.config.get("ADMIN_TEMPLATE","bootstrap3")
    
    admin.add_view(ModelView(Category, db.session))
    admin.add_view(ModelView(Address, db.session))
    admin.add_view(ModelView(Item, db.session))
    admin.add_view(ModelView(Store, db.session))
    
    admin.init_app(app)