
import os


class Development(object):

    """

    Development environment configuration

    """

    DEBUG = True
    TESTING = False
    # JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = "postgres://postgres:pgijtsaMS@127.0.0.1:5432/joborderdb"


class Production(object):

    """

    Production environment configurations

    """

    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "postgres://postgres:pgijtsaMS@127.0.0.1:5432/joborderdb"
    # JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')


app_config = {

    'development': Development,

    'production': Production,

}