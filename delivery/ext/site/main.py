from crypt import methods
from flask import Blueprint, render_template, request, url_for, redirect
from delivery.ext.site.controllers.form import UserForm
from delivery.ext.site.models.models import User
from delivery.ext.db import db

bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/signup", methods=["GET", "POST"])
def signup():
    form = UserForm()
    
    if form.validate_on_submit(): # if method is POST an validate
        user = User(email=form.email.data, passwd=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("site.signin"))
    
    if request.method == "POST":
        user = User(email=form.email.data, passwd=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("site.signin"))
    else:
        print("get")
    
    return render_template("sign-up.html", form=form)

@bp.route("/signin")
def signin():
    form = UserForm()
    return render_template("sign-in.html", form=form)