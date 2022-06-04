from flask import Blueprint
from flask import render_template, request

bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    return render_template("index.html", name=request.args["name"])
