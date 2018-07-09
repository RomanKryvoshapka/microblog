from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
mail = Mail(app)
login.login_view = 'login'

# if not app.debug:
if 1:
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], 465),
            fromaddr='no-reply@' + app.config['MAIL_USERNAME'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD']), timeout=60)
        mail_handler.setLevel(logging.ERROR)
        print('1313'*100)
        app.logger.addHandler(mail_handler)

from app import routes, models, errors
