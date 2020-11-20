from PyQt5 import QtWidgets, QtSql

import var

class Conexion():
    '''try:
        HOST='localhost'
        PORT='27017'
        URI_CONNECTION='mongodb://'+HOST+':'+PORT+'/'
        var.DATABASE='empresa'
        print('Ok -- Conectado al servidor %s'%HOST)
        print('Conexion de datos establecida')
    except pymongo.errors.ServerSelectionTimeoutError as error:
        print('Error en la conexion MongoDB: %s'%error)
    #except pymongo.errors.ConnecionFailure as error:
     #   print('No se puede conectar to MongoDB: %s'%error)'''
    def db_connect(filename):
        db=QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(filename)
        if not db.open():
            QtWidgets.QtMessageBox.critical(None,'No se puede abrir la base de datos',
                                            'No se puede establecer conexion.\n''Haz Click para Cancelar.',
                                            QtWidgets.QMessageBox.Cancel)
            return False
        else:
            print('Conexion establecida')
        return True


    '''def altaCli(cliente):

        query=QtSql.QSqlQuery()
        query.prepare('insert into clientes(dni, apelidos, nome, fechalta, direccion, provincia, sexo, formapago)'
                      'VALUES (:dni, :apelidos, :nome, :fechalta, :direccion, :provincia, :sexo, :formapago)')
        query.bindValue(':dni',str(cliente[0]))
        query.bindValue(':apelidos',str(cliente[1]))
        query.bindValue(':nome',str(cliente[2]))
        query.bindValue(':fechalta',str(cliente[3]))
        query.bindValue(':direccion',str(cliente[4]))
        query.bindValue(':provincia',str(cliente[5]))
        query.bindValue(':sexo',str(cliente[6]))
        query.bindValue(':formapago',str(cliente[7]))
        query.bindValue(':dni', "dni")
        query.bindValue(':apelidos', "apel")
        query.bindValue(':nome', "asd")
        query.bindValue(':fechalta', "alta")
        query.bindValue(':direccion', "direc")
        query.bindValue(':provincia', "f")
        query.bindValue(':sexo', "f")
        query.bindValue(':formapago', "F")
        print(cliente)
        if query.exec_():
            print("Inserción correcta")
        else:
            print ("Error: altacli ",query.lastError().text())'''

    def altaCli(cliente):
        query = QtSql.QSqlQuery()
        query.prepare('insert into clientes (dni, apelidos, nome, fechalta, direccion, provincia, sexo, formapago)'
                      'VALUES (:dni, :apelidos, :nome, :fechalta, :direccion, :provincia, :sexo, :formapago)')
        query.bindValue(':dni', str(cliente[0]))
        query.bindValue(':apelidos', str(cliente[1]))
        query.bindValue(':nome', str(cliente[2]))
        query.bindValue(':fechalta', str(cliente[3]))
        query.bindValue(':direccion', str(cliente[4]))
        query.bindValue(':provincia', str(cliente[5]))
        query.bindValue(':sexo', str(cliente[6]))
        # pagos = ' '.join(cliente[7]) si quiesesemos un texto, pero nos viene mejor meterlo como una lista
        query.bindValue(':formapago', str(cliente[7]))
        if query.exec_():
            print("Inserción Correcta")
