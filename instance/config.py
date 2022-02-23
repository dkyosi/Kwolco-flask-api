import os

class Config(object):
    """ application configuration class """
    DEBUG = False
    SECRET = 'SECRET'
    DATABASE_URL =''
    
class DevelopmentConfig(Config):
    """ Configurations for Development """
    DEBUG = True
    TESTING = True
    
class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}