#Configuraciones del proyecto

class DevelopmentConfig():
    DEBUG=True

#Parámetros de la base de datos
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'api2'

config={
    'development':DevelopmentConfig
}
