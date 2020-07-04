from flask import Flask,render_template
import logging
#from logging.handlers import SMTPHandler
#from logging.handlers import RotatingFileHandler
import os
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_bootstrap import Bootstrap

from flask_login import LoginManager 
import datetime

#from redis import Redis
#import rq

year_now= datetime.datetime.now().year

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'
mail = Mail()
bootstrap = Bootstrap()
#moment = Moment()
#babel = Babel()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    #moment.init_app(app)
    #babel.init_app(app)
    
    #app.redis = Redis.from_url(app.config['REDIS_URL'])
    #app.task_queue = rq.Queue('microblog-tasks', connection=app.redis)############stop######

    from numerology.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from numerology.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from numerology.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from numerology.users import bp as users_bp
    app.register_blueprint(users_bp)
    
    from numerology.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')


    return app

from numerology import models