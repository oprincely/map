from flask import Flask
import os
from config import Config
#-------- mail --------------
import logging
from logging.handlers import SMTPHandler

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_mail import Mail


#from flask_wtf.csrf import CSRFProtect


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
bootstrap = Bootstrap()
moment = Moment()
mail = Mail()

login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    bootstrap = Bootstrap(app)
    moment.init_app(app)
    mail.init_app(app)
    
    # protecting our app 
    #csrf = CSRFProtect(app)
    
    #-------- mailling --------------
    if not app.debug:
        #-------- for mail --------------
        if app.config['MAIL_SERVER']:
            auth = None
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            secure = None
            if app.config['MAIL_USE_TLS']:
                secure = ()
            mail_handler = SMTPHandler(
                mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                fromaddr='no-reply@' + app.config['MAIL_SERVER'],
                toaddrs=app.config['ADMINS'], subject='Mapng Failure',
                credentials=auth, secure=secure)
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)
        #-------- mail --------------
        
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    
    ##from app.exams import bp as exams_bp
    ##app.register_blueprint(exams_bp)
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.main import bp as errors_bp
    app.register_blueprint(errors_bp)
    
    from app.transit import bp as transit_bp
    app.register_blueprint(transit_bp)
    
    from app.users import bp as users_bp
    app.register_blueprint(users_bp)
    
    from app.api import bp as api_bp
    app.register_blueprint(api_bp)
    
    from app.admin import bp as admin_bp
    app.register_blueprint(admin_bp)


    return app

from app import models

#from numerology import models