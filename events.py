import shutil

import Clients
import conexion
import var
import sys
from datetime import  datetime
import zipfile,os
from PyQt5 import QtWidgets, QtSql
import xlrd

class Eventos():

    # def Saludo():
    #   try:
    #      print('Error: %s '%str(error))
    def Salir(event):
        '''

        Módulo para cerrar el programa

        :return: None

        Muestra ventana de aviso

        '''
        try:
            var.dlgsalir.show()
            if var.dlgsalir.exec_():
                sys.exit()
            else:
                var.dlgsalir.hide()
                event.ignore()
        except Exception as error:
            print("Error a %s:  " % str(error))
    def Eliminar(self):
            try:
                if var.cliente:
                    Clients.Clientes.bajaCliente("self")

                    var.dlgaviso.hide()
                    var.cliente=False
                    conexion.Conexion.mostrarClientes(None)
                    print("Eliminar")
            except Exception as error:
                print("Error eliminar %s:  " % str(error))

    '''
    eventos clientes
    '''

    def validoDNI(self):
        try:
            """

                   Modulo que según sea correcto el dni o no, muestra una imagen distinta

                   :return: none

                   Si es falso escribe en el label una cruz roja si es true devuelve una V verda

                   """
            dni = var.ui.lnDNI.text()
            if Clients.Clientes.validarDNI(dni):
                var.ui.lblValido.setStyleSheet('QLabel {color: green;}')
                var.ui.lblValido.setText('V')
                var.ui.lnDNI.setText(dni.upper())
            else:
                var.ui.lblValido.setStyleSheet('QLabel {color: red;}')
                var.ui.lblValido.setText('X')
                var.ui.lnDNI.setText(dni.upper())

        except Exception as error:
            print('Error: dni %s' % str(error))

    def cargarProv(self):
        """

        Módulo que se ejecuta al principio para cargar las provincias. En versión posterior cargaremos
        y municipios desde la BBDD.

        :return: None
        :rtype: None

        """
        try:
            prov = ['', 'A Coruña', 'Lugo', 'Ourense', 'Pontevedra']
            for i in prov:
                var.ui.cmbProv.addItem(i)
        except Exception as error:
            print('Error: prov %s ' % str(error))

    def Confirmar(self):
        '''

        Ventana de confirmación

        :return: None
        :rtype: None

        '''
        try:
            if var.cliente:
                Clients.Clientes.bajaCliente()
                var.dlgaviso.hide()
                var.cliente=False
                conexion.Conexion.mostrarClientes(None)
        except Exception as error:
            print('Error: confirmar %s ' % str(error))

    def mostrarAvisoCli(self):
        try:
            '''

            Ventana de aviso
            :return: None
            :rtype: None

            '''
            var.cliente=True
            #var.dlgaviso.addWidget(var.ui.lblstatus, 1)
            #var.dlgaviso.lblAviso.SetText('Hey')
            var.dlgaviso.show()
        except Exception as error:
            print('Error mostrar aviso: % '%str(error))
    def Anular(self):
        '''

        Ventana de confirmación

        :return: None
        :rtype: None

        '''
        try:
            var.dlgaviso.hide()
            print("hola")
        except Exception as error:
            print('Error Boton anula %s '%str(error))
    def abrirDir(self):
        '''

        Módulo que abre una ventana de diálogo

        :return: None
        :rtype: None

        '''
        try:
            var.filedlgabrir.show()
        except Exception as error:
            print('Error abrir explorador: % ' % str(error))
    def abrirPrinter(self):
        '''

        Módulo que abre la ventana de diálogo de la impresora

        :return: None
        :rtype: None

        '''
        try:
            var.dlgimprimir.setWindowTitle('Imprimir')
            var.dlgimprimir.setModal(True)
            var.dlgimprimir.show()
        except Exception as error:
            print('Error abrir explorador: % ' % str(error))
    def Backup(self):
        '''

        Módulo que realizar el backup de la BBDD

        :return: None
        :rtype: None

        Utiliza la librería zipfile, añade la fecha y hora de la copia al nombre de esta y tras realizar la copia
        la mueve al directorio deseado por el cliente. Para ello abre una ventana de diálogo

        '''
        try:
            fecha=datetime.now()
            fichzip=zipfile.ZipFile('_backup.zip','w')
            fichzip.write(var.filebd, os.path.basename(var.filebd),zipfile.ZIP_DEFLATED)
        except Exception as error:
            print('Error guardar backup: % ' % str(error))
    def buscarCli(self):
        try:
            dni=var.ui.lnDNI.text()
            conexion.Conexion.buscarCli(dni)
        except Exception as error:
            print('Error buscar clientes: % ' % str(error))

    def MostrarVentanaAbout(self):
        try:
            var.dlgAbout.show()
        except Exception as error:
            print('Error abrir about: % ' % str(error))

    def MostrarVentanaMod(self):
        try:
            var.dlgModificar.show()
        except Exception as error:
            print('Error abrir about: % ' % str(error))
    def cerrar(self):
        try:
            var.dlgAbout.hide()
        except Exception as error:
            print('Error Boton cerrar %s '%str(error))
    def cerrarMod(self):
        try:
            var.dlgModificar.hide()
        except Exception as error:
            print('Error Boton aceptar mod %s '%str(error))
    def restaurarBD(self):
        '''

        Módulo que restaura la BBDD

        :return: None
        :rtype: None

        Abre ventana de diálogo para buscar el directorio donde está copia de la BBDD y la restaura haciendo suo
        de la librería zipfile
        Muestra mensaje de confirmación

        '''
        try:
            option = QtWidgets.QFileDialog.Options()
            filename = var.filedlgabrir.getOpenFileName(None, 'Restaurar Copia de Seguridad','','*.zip;;All Files', options= option)
            if var.filedlgabrir.Accepted and filename != '':
                file = filename[0]
                with zipfile.ZipFile(str(file),'r') as bbdd:
                    bbdd.extractall(pwd=None)
                bbdd.close()
            conexion.Conexion.db_connect(var.filebd)
            conexion.Conexion.mostrarClientes(self)
            conexion.Conexion.mostrarProducts(self)
            conexion.Conexion.mostrarFacturas(self)
            var.ui.lblstatus.setText('COPIA DE SEGURIDAD RESTAURDA')
        except Exception as error:
            print('Error restaurar base de datos: %s '  % str(error))

    def Backup(self):
        '''

        Módulo que realizar el backup de la BBDD

        :return: None
        :rtype: None

        Utiliza la librería zipfile, añade la fecha y hora de la copia al nombre de esta y tras realizar la copia
        la mueve al directorio deseado por el cliente. Para ello abre una ventana de diálogo

        '''
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
            var.copia = (str(fecha) + '_backup.zip')
            option = QtWidgets.QFileDialog.Options()
            directorio, filename = var.filedlgabrir.getSaveFileName(None, 'Guardar Copia', var.copia, '.zip', options=option)
            if var.filedlgabrir.Accepted and filename != '':
                fichzip = zipfile.ZipFile(var.copia, 'w')
                fichzip.write(var.filebd, os.path.basename(var.filebd), zipfile.ZIP_DEFLATED)
                fichzip.close()
                var.ui.lblstatus.setText('COPIA DE SEGURIDAD DE BASE DE DATOS CREADA')
                shutil.move(str(var.copia), str(directorio))
        except Exception as error:
            print('Error: %s' % str(error))
    def ventanaImp(self):
        '''

        Módulo que restaura la BBDD

        :return: None
        :rtype: None

        Abre ventana de diálogo para buscar el directorio donde está copia de la BBDD y la restaura haciendo suo
        de la librería zipfile
        Muestra mensaje de confirmación

        '''
        try:
            option = QtWidgets.QFileDialog.Options()
            filename = var.filedlgabrir.getOpenFileName(None, 'Importar datos','','*.xls;;All Files', options= option)
            if var.filedlgabrir.Accepted and filename != '':
                file = filename[0]
                Eventos.importarDatos(file)
            var.ui.lblstatus.setText('COPIA DE SEGURIDAD RESTAURDA')
        except Exception as error:
            print('Error restaurar base de datos: %s '  % str(error))
    def importarDatos(file):
        documento = xlrd.open_workbook(file)
        productos = documento.sheet_by_index(0)
        columnas_lacteos = productos.ncols
        print("lacteos tiene " + str(columnas_lacteos) + " ringleiras y " +
              str(columnas_lacteos) + " columnas")

        for i in range(productos.ncols):
            ringleira = productos.row(i)
            print(ringleira)


        for i in range(1, productos.nrows):
            nombre=productos.cell_value(i,0)
            precio=productos.cell_value(i,1)
            stock=productos.cell_value(i,2)

            query1 = QtSql.QSqlQuery()

            query2 = QtSql.QSqlQuery()

            query1.prepare('select * from productos where nomeprod = :nomeprod')
            query1.bindValue(':nomeprod', nombre)

            if query1.exec_():
                while query1.next():
                    print(nombre + " " + str(query1.value(0)))
                    query2.prepare('update productos set preciounidad=:preciounidad, stock=:stock where nomeprod= :nomeprod')
                    query1.finish()
                    query2.prepare('select preciounidad from productos where nomeprod = :nomeprod')
                    query2.bindValue(':nomeprod',nombre)

                    if query2.exec_():
                        while query2.next():
                            query2.bindValue(':preciounidad',float(precio))
                            query2.bindValue(':stock',int(stock))
                            print('Actualizado')
                    else:
                        print('error en la actualizacion',query2.lastError().text())

                    query2.finish()

            else:
                query = QtSql.QSqlQuery()
                query.prepare('insert into productos (nomeprod, preciounidad, stock) values (:nomeprod, :preciounidad, :stock)')
                query.bindValue(':nomeprod',str(nombre))
                query.bindValue(':preciounidad',float(precio))
                query.bindValue(':stock',int(stock))

                if query.exec_():
                    print("Insertado correctamente")
                    query.finish()
                else:
                    print("Error baja ventasFact: ", query.lastError().text())
                query.finish()
                print('nuevo creado')

        print("---------")

