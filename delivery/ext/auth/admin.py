from flask_admin.contrib.sqla import ModelView
from flask_admin.actions import action
from delivery.ext.db import db
from delivery.ext.site.models.models import User
from flask import flash

class UserAdmin(ModelView):
    """Interface ModelView class"""
    
    column_formatters = {
        "email" : lambda s, r, u, *a: u.email.split("@")[0]
    }
    
    column_list = ["email", "admin"]
    
    column_searchable_list = ["email"]
    column_filter = ["admin"]
    
    @action(
        'toggle_admin',
        'Toggle Admin Status',
        'Are you sure?'
        
    )
    def toggle_admin_status(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        for user in users:
            user.admin = not user.admin
        db.session.commit()
        if len(users) > 1:
            flash(f'{len(users)} user successfully updated!','success')
        else:
            flash(f'{len(users)} user successfully updated!', 'success')
            
    @action(
        'send_mail',
        'Send Email',
        'Are you sure?'
        
    )
    def send_mail(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        list_mails = []
        for user in users:
            list_mails.append(user.email)
        # print(list_mails)
        # db.session.commit()
        flash(f'Emails send sucessfully', 'success')
