from flask_debugtoolbar import DebugToolbarExtension


def init_app(app):
    return DebugToolbarExtension(app)