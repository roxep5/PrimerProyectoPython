from PyQt5 import QtWidgets, QtSql

import var
import conexion
import ventas


class Conexion():
    '''

   Módulo que realiza la conexión de la aplicación con la BBDD

   :param filename: nombre de la BBDD
   :type: string
   :return: True o False
   :rtype: bool

   Utiliza la librería de QtSql y el gestor de la BBDD es QSQlite. En caso de error muestra pantalla
   de aviso.

    '''
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
        '''

        Da de alta un cliente cuyos datos se pasan por una lista.
        Muestra mensaje de resultado en el barra de estado.
        Recarga la tabla actualizada de clientes

        :param: cliente
        :type: lista
        :return: None
        :rtype: None

        '''
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
        '''

        Módulo que carga los datos del cliente por orden alfabético en la tabla Clientes

        :return: None
        :rtype: None

        '''
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
        '''

        Módulo para eliminar cliente.

        :param dni
        :type: string
        :return None
        :rtype None

        Se pasa como argumento el dni del cliente a eliminar.
        A continuación recarga la tablaCli actualizada
        Muestra mensje resultado en la barra de estado

        '''
        query=QtSql.QSqlQuery()
        query.prepare('delete from clientes where dni= :dni')
        query.bindValue(':dni',dni)
        if query.exec_():
            print('Baja cliente')
            var.ui.lblstatus.setText('Cliente con dni '+dni+' dado de baja')
        else:
            print("Error baja clientes: ",query.lastError().text())

    def modifCli(codigo,newdata):
        '''

        Módulo que actualiza datos de clinte

        :param codigo: código cliente
        :type codigo: int
        :param newdata: datos cliente
        :type newdata: lista
        :return: None
        :rtype: None

        Recibe como parámetros el código del cliente a modificar así como los datos que deseamos modificar.
        En realidad toma todos los datos que hay en los widgets de la pantalla clientes.

        '''
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
        '''

        Muestra los datos por pantalla de un cliente cuando se clickea sobre el mismo en la tabla.

        :return: None
        :rtype: None

        '''
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
            '''

            Módulos que busca un cliente y carga sus datos en la pantalla cliente

            :param dni: dni cliente a buscar
            :type dni: string
            :return: None
            :rtype: None

            '''

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
        '''

        Da de alta un producto cuyos datos se pasan por una lista.
        Muestra mensaje de resultado en el barra de estado.
        Recarga la tabla actualizada de productos

        :param: producto
        :type: lista
        :return: None
        :rtype: None

        '''
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
        '''

        Módulo que carga los datos del producto por orden alfabético en la tabla Productos

        :return: None
        :rtype: None

        '''
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
        ''''

        Módulo para eliminar producto del inventario.

        :param cod
        :type: int
        :return None
        :rtype None

        Se pasa como argumento el código del producto a eliminar.
        A continuación recarga la tablaProd actualizada
        Muestra mensaje resultado en la barra de estado

        '''
        query = QtSql.QSqlQuery()
        query.prepare('delete from Productos where Codigo= :Codigo')
        query.bindValue(':Codigo', id)
        if query.exec_():
            print('Baja Producto')
            var.ui.lblstatus.setText('Producto con id ' + id + ' dado de baja')
        else:
            print("Error baja Producto: ", query.lastError().text())
    def cargarProd(cod):
        '''

        Muestra los datos por pantalla de un producto cuando se clickea sobre el mismo en la tabla.

        :param cod: código del producto
        :type cod: entero
        :return: None
        :rtype: None

        '''

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
        '''

        Módulo que actualiza datos del producto

        :param cod: código producto
        :type cod: int
        :param newdata: datos producto
        :type newdata: lista
        :return: None
        :rtype: None

        Recibe como parámetros el código del producto a modificar así como los datos que deseemos modificar.
        En realidad toma todos los datos que hay en los widgets de la pantalla productos.
        El precio se formatea con dos decimales y punto.
        Muestra resultado en la barra de estado

        '''
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
        '''

        Módulo que carga los datos en el combobox provincias haciendo un llamada a la BBDD.

        :return: None
        :rtype: None

        '''
        try:
            var.cmbVenta.clear()
            query=QtSql.QSqlQuery()
            var.cmbVenta.addItem('')
            query.prepare('select Codigo, NomeProd from productos order by NomeProd')
            if query.exec_():
                while query.next():
                    var.cmbVenta.addItem(str(query.value(1)))
        except Exception as error:
            print("error en cargar cmbventa %s "%str(error))


    def altaFact(dni, fecha, apel):
        '''

        Módulo que da de alta una factura previa al proceso de venta

        :param dni: dni cliente
        :type dni: string
        :param fecha: fecha de alta de la factura
        :type fecha: formato fecha en string
        :param apel: apellidos del ciente
        :type apel: string
        :return: None
        :rtype: None

        Recibe datos para carga la factura en la BBDD y en la tabla Factura. Además obtiene el código de la
        factura dada de alta para cargarla en el label lblNumFac ya que al ser autonumérico no se obtiene hasta
        que previamente insertemos la factura.

        '''
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
        '''

        Módulo que carga los datos de la factura por orden descendente numérico en la tabla Facturas

        :return: None
        :rtype: None

        '''
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
        '''

        Módulo que carga datos de un factura en los widgets al clickear sobre una fila de la tablaPro

        :param cod: código de la factura
        :type cod: int
        :return: None
        :rtype: None

        '''
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
            print("Error cargar facturas: ", query.lastError().text())
    def obtenetCodPrec(articulo):
        '''

        Módulo que devuelve el precio y código del producto que se pasa como parámetro

        :param: articulo
        :type: string
        :return: dato
        :rtype: lista que contiene código y precio del producto

        '''
        dato=[]
        query=QtSql.QSqlQuery()
        query.prepare('select codigo, precioUnidad from productos where NomeProd =:articulo')
        query.bindValue(':articulo',str(articulo))
        if query.exec_():
            while query.next():
                dato=[str(query.value(0)),str(query.value(1))]
            return dato
        else:
            print("Error obtener cod precio: ", query.lastError().text())
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

    def altaVenta(self):
        '''

        Módulo que añade líneas de venta en una factura creada

        :return: None
        :rtype: None

        Inserta en la tabla ventas una línea de venta que se va mostrando cada vez que realizamos la transacción.
        Tras realizar la venta se crea una nueva factura incluyendo el combobox de selección de artículor

        '''
        query=QtSql.QSqlQuery()
        query.prepare('insert into ventas (codfact, codart, cantidad,precio) VALUES (:codfact,:codart,:cantidad, :precio)')
        query.bindValue(':codfact',int(var.venta[0]))
        query.bindValue(':codart',int(var.venta[1]))
        query.bindValue(':cantidad',int(var.venta[3]))
        query.bindValue(':precio',int(var.venta[4]))
        row=var.ui.tableArticulos.currentRow()
        if query.exec_():
            var.ui.lblstatus.setText('Venta realizada')
            var.ui.tableArticulos.setItem(row,1,QtWidgets.QTableWidgetItem(str(var.venta[2])))
            var.ui.tableArticulos.setItem(row,2,QtWidgets.QTableWidgetItem(str(var.venta[3])))
            var.ui.tableArticulos.setItem(row,3,QtWidgets.QTableWidgetItem(str(var.venta[4])))
            var.ui.tableArticulos.setItem(row,4,QtWidgets.QTableWidgetItem(str(var.venta[5])))
            row = row+1
            var.ui.tableArticulos.insertRow(row)
            var.ui.tableArticulos.setCellWidget(row,1,var.cmbVenta)
            var.ui.tableArticulos.scrollToBottom()
            Conexion.cargarComboVenta(var.cmbVenta)
        else:
            print("Error alta venta: ", query.lastError().text())

    def listadoVentasFact(codfact):
        """

        Módulo que lista las ventas contenidaa en una factura

        :param codfac: valor factura a la que se incluirán las líneas de venta
        :type codfac: int
        :return: None
        :rtype: None

        Recibe el código de la factura para seleccionar los datos de las ventas cargadas a esta.
        De la BB.DD toma el nombre del producto y su precio para cada línea de venta. El precio lo multiplica
        por las unidades y se obtiene el subtotal de cada línea. Después en cada línea de la tabla irá
        el código de la venta, el nombre del producto, las unidades y el subtotal.
        Finalmente, va sumando el subfact, que es la suma de todas las ventas de esa factura, le aplica el IVA y
        el importe total de la factura. Los tres valores, subfact, iva y fac los muestra en los label asignados.

        En excepciones se recoge cualquier error que se produzca en la ejecución del módulo.

        """
        try:
            var.ui.tableArticulos.clearContents()
            var.subfac=0.00
            subtotal=0.00
            query=QtSql.QSqlQuery()
            query1=QtSql.QSqlQuery()
            query.prepare('select clientes, codart,cantidad from ventas where codfact=:codfact')
            query.bindValue(':codfact',int(codfact))
            if query.exec_():
                index=0
                while query.next():
                    codventa=query.value(0)
                    codartventa=query.value(1)
                    cantidad=query.value(2)
                    var.ui.tableArticulos.setRowCount(index+1)
                    var.ui.tableArticulos.setItem(index,0,QtWidgets.QTableWidgetItem(str(codventa)))
                    query1.prepare('select nomeprod, precioUnidad from productos where codigo=:codartventa')
                    query1.bindValue(':codartventa',int(codartventa))
                    if query1.exec_():
                        while query1.next():
                            articulo=query1.value(0)
                            precio=query1.value(1)
                            var.ui.tableArticulos.setItem(index,1,QtWidgets.QTableWidgetItem(str(articulo)))
                            var.ui.tableArticulos.setItem(index,2,QtWidgets.QTableWidgetItem(str(cantidad)))
                            subtotal=round(float(cantidad)*float(precio),2)
                            var.ui.tableArticulos.setItem(index,3,QtWidgets.QTableWidgetItem(str(precio)))
                            var.ui.tableArticulos.setItem(index,4,QtWidgets.QTableWidgetItem(str(subtotal)))
                    index+=1
                    var.subfac=round(float(subtotal)+float(var.subfac),2)
            if int(index)>0:
                ventas.Ventas.prepararTabVentas(index)
            else:
                print(index)
                var.ui.tableArticulos.setRowCount(0)
                ventas.Ventas.prepararTabVentas(0)
            var.ui.lblSubtotal.setText(str(var.subfac))
            var.iva=round(float(var.subfac)*0.21,2)
            var.ui.lblIVA.setText(str(var.iva))
            var.fac=round(float(var.iva)+float(var.subfac),2)
            var.ui.lblTotal.setText(str(var.fac))
        except Exception as error:
            print('Error Listado de la tabla de ventas: %s ' % str(error))


    def borrarVenta(codVenta):
        '''

        Módulo que anula una linea de venta de una factura

        :param: codVenta que es el código de la venta a anlar
        :return: None
        :rtype: None

        Muestra mensaje en la barra de estado

        '''
        query=QtSql.QSqlQuery()
        query.prepare('delete from ventas where Clientes = :clientes')
        query.bindValue(':clientes',codVenta)
        if query.exec_():
            var.ui.lblstatus.setText('Factura Anulada')
        else:
            print("Error baja venta: ",query.lastError().text())
    def borrarFacturas(codFactura):
        '''

        Módulo que borra una factura y todas las ventas asociadas a esa factura

        :param: codfac o código de la factura
        :type: int
        :return: None
        :rtype: None

        En primer lugar borra la factura y luego vuelve a realizar una llamada a la base de datos para
        borrar todas aquellas ventas asociadas a esa factura.

        '''
        query=QtSql.QSqlQuery()
        query.prepare('delete from Facturas where CodFactura=:codfactura')
        query.bindValue(':codfactura',codFactura)
        if query.exec_():
            var.ui.lblstatus.setText('Factura Anulada')
        else:
            print("Error baja venta: ",query.lastError().text())
    def borrarVentasFacturas(codFactura):
        query=QtSql.QSqlQuery()
        query.prepare('delete from Ventas where CodFact=:codfact')
        query.bindValue(':codfact',codFactura)
        if query.exec_():
            print("Ventas eliminadas")
        else:
            print("Error baja ventasFact: ",query.lastError().text())
