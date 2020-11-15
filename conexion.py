import pymongo, var

class Conexion():
    try:
        HOST='localhost'
        PORT='27017'
        URI_CONNECTION='mongodb://'+HOST+':'+PORT+'/'
        var.DATABASE='empresa'
        print('Ok -- Conectado al servidor %s'%HOST)
        print('Conexion de datos establecida')
    except pymongo.errors.ServerSelectionTimeoutError as error:
        print('Error en la conexion MongoDB: %s'%error)
    #except pymongo.errors.ConnecionFailure as error:
     #   print('No se puede conectar to MongoDB: %s'%error)