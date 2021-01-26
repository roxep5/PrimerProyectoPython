from PyQt5 import QtWidgets, QtSql

import var
import conexion
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



    def altaCli(cliente):
        query = QtSql.QSqlQuery()

        query.prepare('insert into clientes (dni, apelidos, nome, fechalta, direccion,edad, provincia, sexo, formapago)'
                      'VALUES (:dni, :apelidos, :nome, :fechalta, :direccion,:edad, :provincia, :sexo, :formapago)')
        query.bindValue(':dni', str(cliente[0]))
        query.bindValue(':apelidos', str(cliente[1]))
        query.bindValue(':nome', str(cliente[2]))
        query.bindValue(':fechalta', str(cliente[3]))
        query.bindValue(':direccion', str(cliente[4]))
        query.bindValue(':edad', str(cliente[5]))
        query.bindValue(':provincia', str(cliente[6]))
        query.bindValue(':sexo', str(cliente[7]))
        # pagos = ' '.join(cliente[7]) si quiesesemos un texto, pero nos viene mejor meterlo como una lista
        query.bindValue(':formapago', str(cliente[8]))


        if query.exec_():
            print("Inserción Correcta")
            Conexion.mostrarClientes(None)
            var.ui.lblstatus.setText('Insercion correcta: cliente con dni ' + cliente[0]+'')
        else:
            print("Error: altacli ", query.lastError().text())
    def mostrarClientes(self):
        index=0
        query=QtSql.QSqlQuery()
        query.prepare('select dni, apelidos, nome from clientes')
        if query.exec_():
            while query.next():
                dni=query.value(0)
                apelidos=query.value(1)
                nombre=query.value(2)
                var.ui.cliTable.setRowCount(index+1)
                var.ui.cliTable.setItem(index,0,QtWidgets.QTableWidgetItem(dni))
                var.ui.cliTable.setItem(index,1,QtWidgets.QTableWidgetItem(apelidos))
                var.ui.cliTable.setItem(index,2,QtWidgets.QTableWidgetItem(nombre))
                index+=1
        else:
            print("Error mostrar clientes: ",query.lastError().text())
    def bajaCli(dni):
        query=QtSql.QSqlQuery()
        query.prepare('delete from clientes where dni= :dni')
        query.bindValue(':dni',dni)
        if query.exec_():
            print('Baja cliente')
            var.ui.lblstatus.setText('Cliente con dni '+dni+' dado de baja')
        else:
            print("Error baja clientes: ",query.lastError().text())

    def modifCli(codigo,newdata):
        print(codigo,"   ",newdata)
        query=QtSql.QSqlQuery()
        codigo=int(codigo)
        query.prepare('update clientes set dni=:dni, apelidos=:apelidos,nome=:nome,'
                      ' direccion=:direccion,provincia=:provincia,sexo=:sexo,formapago=:formapago where codigo=:codigo')
        query.bindValue(':codigo',int(codigo))
        query.bindValue(':dni', str(newdata[0]))
        query.bindValue(':apelidos', str(newdata[1]))
        query.bindValue(':nome', str(newdata[2]))
        query.bindValue(':fechalta', str(newdata[3]))
        query.bindValue(':direccion', str(newdata[4]))
        query.bindValue(':provincia', str(newdata[5]))
        query.bindValue(':sexo', str(newdata[6]))
        # pagos = ' '.join(cliente[7]) si quiesesemos un texto, pero nos viene mejor meterlo como una lista
        query.bindValue(':formapago', str(newdata[7]))

        if query.exec_():
            print('Cliente modificado')
            var.ui.lblstatus.setText('Alta con cliente dni ' + newdata[0])
        else:
            print('error modificar cliente: ',query.lastError().text())

    def cargarCliente(self):
        try:
            dni=var.ui.lnDNI.text()
            query=QtSql.QSqlQuery()

            query.prepare('select * from clientes where dni=:dni')
            query.bindValue(':dni',dni)
            if query.exec_():
                while query.next():
                    var.ui.lblCodcli.setText(str(query.value(0)))
                    var.ui.lnCalendar.setText(str(query.value(4)))
                    var.ui.lnDir.setText(str(query.value(5)))
                    var.ui.lnDNI.setText(str(query.value(1)))
                    var.ui.editDniFactura.setText(str(query.value(1)))
                    var.ui.lnApel.setText(str(query.value(2)))
                    var.ui.editApelido.setText(str(query.value(2)))
                    var.ui.lnNome.setText(query.value(3))
                    var.ui.spinEdad.setValue(int(query.value(9)))
                    print('hola')
                    var.ui.cmbProv.setCurrentText(str(query.value(6)))


                    if str(query.value(7))=='Mujer':
                        var.ui.rbtFem.setChecked(True)
                        var.ui.rbtMasc.setChecked(False)

                    else:
                        var.ui.rbtFem.setChecked(False)
                        var.ui.rbtMasc.setChecked(True)
                    if 'Efectivo' in query.value(8):
                        var.chkpago[0].setChecked(True)
                    if 'Tarjeta' in query.value(8):
                        var.chkpago[1].setChecked(True)
                    if 'Transferencia' in query.value(8):
                        var.chkpago[2].setChecked(True)
            #print(str(query.value(8)))
        except Exception as error:
            print('Error: cargarCli %s ' % str(error))
    def buscarCli(dni):
        try:
            dni = var.ui.lnDNI.text()
            query = QtSql.QSqlQuery()

            query.prepare('select * from clientes where dni=:dni')
            query.bindValue(':dni', dni)
            if query.exec_():
                while query.next():
                    var.ui.lblCodcli.setText(str(query.value(0)))
                    var.ui.lnCalendar.setText(str(query.value(4)))
                    var.ui.lnDir.setText(str(query.value(5)))
                    var.ui.lnDNI.setText(str(query.value(1)))
                    var.ui.editDniFactura.setText(str(query.value(1)))
                    var.ui.lnApel.setText(str(query.value(2)))
                    var.ui.editApelido.setText(str(query.value(2)))
                    var.ui.lnNome.setText(query.value(3))
                    var.ui.spinEdad.setValue(int(query.value(9)))
                    print('hola')
                    var.ui.cmbProv.setCurrentText(str(query.value(6)))

                    if str(query.value(7)) == 'Mujer':
                        var.ui.rbtFem.setChecked(True)
                        var.ui.rbtMasc.setChecked(False)

                    else:
                        var.ui.rbtFem.setChecked(False)
                        var.ui.rbtMasc.setChecked(True)
                    if 'Efectivo' in query.value(8):
                        var.chkpago[0].setChecked(True)
                    if 'Tarjeta' in query.value(8):
                        var.chkpago[1].setChecked(True)
                    if 'Transferencia' in query.value(8):
                        var.chkpago[2].setChecked(True)
            # print(str(query.value(8)))
        except Exception as error:
            print('Error: cargarCli %s ' % str(error))
#Productos
    def altaProd(Prod):
        query = QtSql.QSqlQuery()

        query.prepare('insert into Productos (NomeProd,PrecioUnidad,Stock)'
                      'VALUES (:NomeProd, :PrecioUnidad, :Stock)')
        query.bindValue(':NomeProd', str(Prod[0]))
        query.bindValue(':PrecioUnidad', round(float(Prod[1]),2))
        query.bindValue(':Stock', int(Prod[2]))
        if query.exec_():
            print("Inserción Correcta")
            var.ui.lblstatus.setText('Insercion correcta Producto:  ' + Prod[0] + '')
        else:
            print("Error: altaProd ", query.lastError().text())
    def mostrarProductos(self):
        index=0
        query=QtSql.QSqlQuery()
        query.prepare('select * from Productos order by NomeProd')
        if query.exec_():
            while query.next():
                id = query.value(0)
                nombreProd = query.value(1)
                Precio = query.value(2)
                var.ui.tableProd.setRowCount(index + 1)
                var.ui.tableProd.setItem(index, 0, QtWidgets.QTableWidgetItem(str(id)))
                var.ui.tableProd.setItem(index, 1, QtWidgets.QTableWidgetItem(nombreProd))
                var.ui.tableProd.setItem(index, 2, QtWidgets.QTableWidgetItem(str(Precio)))
                index += 1
        else:
            print("Error mostrar productos: ", query.lastError().text())

    def bajaProductos(id):
        query = QtSql.QSqlQuery()
        query.prepare('delete from Productos where Codigo= :Codigo')
        query.bindValue(':Codigo', id)
        if query.exec_():
            print('Baja Producto')
            var.ui.lblstatus.setText('Producto con id ' + id + ' dado de baja')
        else:
            print("Error baja Producto: ", query.lastError().text())
    def cargarProd(cod):
        query = QtSql.QSqlQuery()

        query.prepare('select NomeProd, PrecioUnidad, Stock from Productos where codigo=:codigo')
        query.bindValue(':codigo', cod)
        print(cod)
        if query.exec_():
            while query.next():
                var.ui.editCod.setText(str(cod))
                var.ui.editNombreProd.setText(str(query.value(0)))
                var.ui.editPrecioProd.setText(str(query.value(1)))
                var.ui.editStock.setText(str(query.value(2)))
    def modificarProd(codigo, newdata):
            print(codigo, "   ", newdata)
            query = QtSql.QSqlQuery()
            codigo = int(codigo)
            query.prepare('update Productos set NomeProd=:NomeProd, PrecioUnidad=:PrecioUnidad,Stock=:Stock'
                          ' where Codigo=:Codigo')
            query.bindValue(':Codigo', int(codigo))
            query.bindValue(':NomeProd', str(newdata[0]))
            query.bindValue(':PrecioUnidad', round(float(newdata[1])))
            query.bindValue(':Stock', int(newdata[2]))
            print( newdata)
            if query.exec_():
                print('producto modificado')
                var.ui.lblstatus.setText('producto con id modificado' + str(codigo))
                conexion.Conexion.mostrarProductos(None)
            else:
                print('error modificar producto: ', query.lastError().text())

    def cargarCmbVenta(cmbventa):
        try:
            var.cmbVenta.clear()
            query=QtSql.QSqlQuery()
            var.cmbVenta.addItem('')
            query.prepare('select Codigo, NomeProd from productos order by NomeProd')
            if query.exec_():
                while query.next():
                    print("hola")
                    var.cmbVenta.addItem(str(query.value(1)))
        except Exception as error:
            print("error en cargar cmbventa %s "%str(error))


    def altaFact(dni, fecha, apel):
        try:
            query=QtSql.QSqlQuery()
            query.prepare('insert into facturas(dni, fecha, apellidos) VALUES (:dni, :fecha, :apellidos)')
            query.bindValue(':dni',str(dni))
            query.bindValue(':fecha',str(fecha))
            query.bindValue(':apellidos',str(apel))
            if query.exec_():
                var.ui.lblstatus.setText('Factura creada')
            else:
                print("Error alta factura: ", query.lastError().text())
            query1=QtSql.QSqlQuery()
            query1.prepare('select max(codfactura) from facturas')
            if query1.exec_():
                while query1.next():
                    var.ui.lblCodFact.setText(str(query1.value(0)))
        except Exception as error:
            print("error en altafact %s "%str(error))

    def mostrarFacturas(self):
        index=0
        query=QtSql.QSqlQuery()
        query.prepare('select Codfactura,Dni, fecha from facturas')
        if query.exec_():
            while query.next():
                codigo=query.value(0)
                DNI=query.value(1)
                fecha=query.value(2)
                var.ui.tableNfactura.setRowCount(index+1)
                var.ui.tableNfactura.setItem(index,0,QtWidgets.QTableWidgetItem(str(codigo)))
                var.ui.tableNfactura.setItem(index,1,QtWidgets.QTableWidgetItem(str(DNI)))
                var.ui.tableNfactura.setItem(index,2,QtWidgets.QTableWidgetItem(str(fecha)))
                index+=1
        else:
            print("Error mostrar facturas: ",query.lastError().text())

    def cargarFactura(cod):
            query = QtSql.QSqlQuery()
            query.prepare('select fecha,dni, apellidos from Facturas where CodFactura=:codfactura')
            query.bindValue(':codfactura', cod)
            print(cod)
            if query.exec_():
                while query.next():
                    var.ui.lblCodFact.setText(str(cod))
                    var.ui.editFechaFactura.setText(str(query.value(0)))
                    var.ui.editDniFactura.setText(str(query.value(1)))
                    var.ui.editApelido.setText(str(query.value(2)))
            else:
                print("Error mostrar facturas: ", query.lastError().text())
    def obtenetCodPrec(articulo):
        dato=[]
        query=QtSql.QSqlQuery()
        query.prepare('select codigo, precioUnidad from productos where NombreProd =:articulo')
        query.bindValue(':articulo',str(articulo))
        if query.exec_():
            while query.next():
                dato=[str(query.value(0)),str(query.value(1))]
            return dato
        else:
            print("Error mostrar facturas: ", query.lastError().text())
            return None
    def cargarComboVenta(cmbVenta):
        var.cmbVenta.clear()
        query=QtSql.QSqlQuery()
        var.cmbVenta.addItem('')
        query.prepare('select codigo, nomeprod from productos order by nomeProd ')
        if query.exec_():
            while query.next():
                var.cmbVenta.addItem(str(query.value(1)))
        else:
            print("Error cargar combo venta: ",query.lastError().text())
    #def listadoVentasfac(codfact):

