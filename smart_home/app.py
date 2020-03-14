"""
This file initializes application
and brings together all of the various components.
"""

from flask import Flask

from .blueprints.account import account
from .blueprints.error import error
from .blueprints.home import home

import os
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

app.register_blueprint(account)
app.register_blueprint(error)
app.register_blueprint(home)


# Logging configuration
if not app.debug:
    # Send email if an error occurred
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
            toaddrs=app.config['ADMINS'], subject='SmartHome Failure',
            credentials=auth, secure=secure
        )
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    # Logging to a file
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/smarthome.log',
                                       maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('SmartHome startup')
