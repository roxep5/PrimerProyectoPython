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
        try:
            prov = ['', 'A Coruña', 'Lugo', 'Ourense', 'Pontevedra']
            for i in prov:
                var.ui.cmbProv.addItem(i)
        except Exception as error:
            print('Error: prov %s ' % str(error))

    def Confirmar(self):
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
            var.cliente=True
            #var.dlgaviso.addWidget(var.ui.lblstatus, 1)
            #var.dlgaviso.lblAviso.SetText('Hey')
            var.dlgaviso.show()
        except Exception as error:
            print('Error mostrar aviso: % '%str(error))
    def Anular(self):
        try:
            var.dlgaviso.hide()
            print("hola")
        except Exception as error:
            print('Error Boton anula %s '%str(error))
    def abrirDir(self):
        try:
            var.filedlgabrir.show()
        except Exception as error:
            print('Error abrir explorador: % ' % str(error))
    def abrirPrinter(self):
        try:
            var.dlgimprimir.setWindowTitle('Imprimir')
            var.dlgimprimir.setModal(True)
            var.dlgimprimir.show()
        except Exception as error:
            print('Error abrir explorador: % ' % str(error))
    def Backup(self):
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