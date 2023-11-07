class Config:
    SECRET_KEY = "mysecretkey" # used for session management. Utilizada para mensajes flash, como usuario no válida, password incorrecto, etc.


class DevelopmentConfig(Config):
    DEBUG = True

    # Database configuration
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'testingpythondb'

configuration = {
    'development': DevelopmentConfig,
}