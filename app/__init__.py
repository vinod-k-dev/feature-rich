from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'

def create_app(config_class=None):
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    if config_class:
        app.config.from_object(config_class)
    else:
        app.config.from_object('app.config.Config')

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.recipes import bp as recipes_bp
    app.register_blueprint(recipes_bp, url_prefix='/recipe')

    return app
