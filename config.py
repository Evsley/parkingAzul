class Config(object):
    SECRET_KEY = 'my_secret_key'

class DevelopmentConfig(Config):
    DEBUG = True
#    SQLALCHEMY_DATABASE_URI = 'mysql://admin:pa$$w0rd@parkingmapdb.ctqzi4ifuwr6.us-east-1.rds.amazonaws.com/parkingmap'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/parkingmap'
    SQLALCHEMY_TRACK_MODIFICATIONS = False