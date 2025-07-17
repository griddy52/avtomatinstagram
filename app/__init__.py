from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from apscheduler.schedulers.background import BackgroundScheduler
import os

db = SQLAlchemy()
limiter = Limiter(key_func=get_remote_address)
scheduler = BackgroundScheduler()

def create_app():
    app = Flask(__name__)
    app.config.from_envvar('FLASK_CONFIG', silent=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
    db.init_app(app)
    limiter.init_app(app)
    with app.app_context():
        from . import main
        db.create_all()
    return app 