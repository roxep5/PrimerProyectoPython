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

''' def mostrarClientes(self):
        index=0
        query=QtSql.QSqlQuery()
        query.prepare('select dni, apelidos, nome from clientes')
        if query.exec_():
            while query.next():
                #cojo los valores
                dni=query.value(0)
                apelidos=query.value(1)
                nombre=query.value(2)
                #crea la fila
                var.ui.cliTable.setRowCout(index+1)
                #va metiendo los datos en cada celda de la fila
                var.ui.cliTable.setItem(index,0,QtWidgets.QTableWidgetItem(dni))
                var.ui.cliTable.setItem(index,1,QtWidgets.QTableWidgetItem(apelidos))
                var.ui.cliTable.setItem(index,2,QtWidgets.QTableWidgetItem(nombre))
        else:
            print("Error mostrar clientes:%s"% query.lastError().text())'''
    def cargarCli(cliente):
        query=QtSql.QSqlQuery()
        query.prepare('insert into clientes(dni, apellidos, nombre, fechalta, direccion, provincia, sexo, formaspago)'
                      'VALUES (:dni, :apellidos, :nombre, :fechalta, :direccion, :provincia, :sexo, :formaspago)')