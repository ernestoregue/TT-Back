class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'transitustt.mysql.database.azure.com'
    MYSQL_USER = 'usuario'
    MYSQL_PASSWORD = 'Mi23esJo'
    MYSQL_DB = 'places'
    MYSQL_PORT = 3306


config = {
    'development': DevelopmentConfig
}
