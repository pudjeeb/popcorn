import os
import logging

class BaseConfig(object):
    DEBUG = False
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'app.log'
    LOGGING_LEVEL = logging.DEBUG

class DefaultConfig(BaseConfig):
    DEBUG = True

config = {
    "development": "app.config.DefaultConfig",
    "default": "app.config.DefaultConfig"
}

def configure_app(app):
    config_name = os.getenv('FLASK_CONFIG', 'default')
    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.cfg', silent=True)
    # Configure logging
    handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
    handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
