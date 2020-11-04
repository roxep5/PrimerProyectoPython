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

    def selSexo():
        try:
            if var.ui.rbtFem.isChecked():
                print("femenino")
            if var.ui.rbtMasc.isChecked():
                print("masculino")
        except Exception as error:
            print('Error: %s '% str(error))

    def selPago():
        try:
            if var.ui.chkEfectivo.isChecked():
                print('pagas con efectivo')
            if var.ui.chkTarjeta.isChecked():
                print('pagas con tarjeta')
            if var.ui.chkTransf.isChecked():
                print('pagas con Transferencia')
        except Exception as error:
            print('Error: %s '%str(error))

    def cargarProv():
        try:
            prov=['','A Coruña','Lugo','Ourense','Pontevedra']
            for i in prov:
                var.ui.cmbProv.addItem(i)
        except Exception as error:
            print('Error: %s ' % str(error))


    def selProv(prov):
        try:
            print('Has se leccionado la provincia de ', prov)
            return prov
        except Exception as error:
            print('Error: %s ' % str(error))
