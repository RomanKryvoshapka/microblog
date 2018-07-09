import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # DEBUG = os.environ.get("FLASK_DEBUG") == 'true'
    DEBUG = False

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_SERVER = 'smtp.gmail.com'
    # MAIL_PORT = int(os.environ['MAIL_PORT'])
    MAIL_PORT = 465
    # MAIL_USE_SSL = os.environ['MAIL_USE_SSL'] == 'true'
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    #MAIL_USERNAME = 'dmytrok@completecase.com'
    #MAIL_PASSWORD = '0935786917qwerty'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = [MAIL_USERNAME]








