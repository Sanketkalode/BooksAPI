"""Development Config"""
import datetime
import os


class DevelopmentConfig:
    """Development Configuration Class"""
    DEBUG = True
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or 'sanket'
    MONGODB_SETTINGS = {
        'db': os.environ.get("MONGODB_DATABASE") or 'BooksDB',
        'host': os.environ.get("MONGODB_HOSTNAME") or 'localhost',
        'port': 27017
    }
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=5)
