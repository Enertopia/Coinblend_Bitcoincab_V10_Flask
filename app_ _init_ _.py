# Copyright Emiliano German Solazzi Griminger 2024

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman
from .config import Config

db = SQLAlchemy()
jwt = JWTManager()
limiter = Limiter(key_func=get_remote_address)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    Talisman(app)
    db.init_app(app)
    jwt.init_app(app)
    limiter.init_app(app)

    from .api import payment_routes
    app.register_blueprint(payment_routes.payment_bp, url_prefix='/api')

    from .auth import auth
    app.register_blueprint(auth.auth_bp, url_prefix='/auth')

    return app
