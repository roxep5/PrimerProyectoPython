import Clients
import conexion
import var
import sys
from datetime import  datetime
import zipfile,os

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

    def validoDNI():
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

    def cargarProv():
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

    def mostrarAvisoCli():
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