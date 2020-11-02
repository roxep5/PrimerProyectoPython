import Clients
import var
import sys


class Eventos():

    def Saludo():
        try:
            var.ui.lblxestion.setText('Has pulsado el boton')
        except Exception as error:
            print('Error: %s '%str(error))
    def Salir():
        try:
            sys.exit()
        except Exception as error:
            print("Error %s:  "%str(error))
    '''
    eventos clientes
    '''

    def validoDNI():
        try:
            dni=var.ui.lnDNI.text()
            if Clients.Clientes.validarDNI(dni):
                var.ui.lblValido.setStyleSheet('QLabel {color: green;}')
                var.ui.lblValido.setText('V')
                var.ui.lnDNI.setText(dni.upper())
            else:
                var.ui.lblValido.setStyleSheet('QLabel {color: red;}')
                var.ui.lblValido.setText('X')
                var.ui.lnDNI.setText(dni.upper())

        except Exception as error:
            print('Error: %s'%str(error))