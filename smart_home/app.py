"""
This file initializes application and brings together all components.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Extensions
db = SQLAlchemy()


def create_app(config_file='config.py'):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_pyfile(config_file)
    db.init_app(app)

    # Register all blueprints
    from .account import account
    app.register_blueprint(account)
    from .error import error
    app.register_blueprint(error)
    from .home import home
    app.register_blueprint(home)

    # Logging configuration
    if not app.debug:
        import os
        import logging
        from logging.handlers import SMTPHandler, RotatingFileHandler

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

    return app

# Import all models
from .account import models as account_models
from .home import models as home_models
