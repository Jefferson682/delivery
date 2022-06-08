def init_app(app):
    app.config['SECRET_KEY'] = "xUBB0WbP1xclj8y7wQsGyZmKRaZNnXR2"
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///delivery.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["FLASK_ADMIN_SWATCH"] = 'cerulean'
    
    if app.debug:
        app.config["DEBUG_TB_TEMPLATE_EDITOR_ENABLE"] = True
        app.config['DEBUG_TB_PROFILER_ENABLE'] = True
        app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False