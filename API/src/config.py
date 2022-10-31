class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'transitus-tt.mysql.database.azure.com'
    MYSQL_USER = 'usuario'
    MYSQL_PASSWORD = 'Tt202212345678'
    MYSQL_DB = 'places'
    MYSQL_PORT = 3306


config = {
    'development': DevelopmentConfig
}