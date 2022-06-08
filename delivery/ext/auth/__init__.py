from delivery.ext.db import db
from delivery.ext.admin import admin as main_admin
from delivery.ext.auth.admin import UserAdmin
from delivery.ext.site.models.models import User


def init_app(app):
    main_admin.add_view(UserAdmin(User, db.session))