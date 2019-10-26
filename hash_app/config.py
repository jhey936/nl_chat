import os
import random
import string

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", ''.join(random.choices(string.ascii_letters + string.digits, k=25)))
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('DATABASE_URL', 'localhost')}/{os.getenv('DATABASE_NAME', 'hash_db')}"


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True