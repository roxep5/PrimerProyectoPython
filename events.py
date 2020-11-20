import Clients
import var
import sys


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


