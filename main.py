from Ventana import *
import sys
import events
import var


class Main(QtWidgets.QMainWindow):

        def __init__(self):
            super(Main, self).__init__()
            var.ui=Ui_MainWindow()
            var.ui.setupUi(self)
            '''
            conexión con los eventos
            '''
            #var.ui.btnOk.clicked.connect(events.Eventos.Saludo)
            var.ui.btnsalir.clicked.connect(events.Eventos.Salir)
            var.ui.lnDNI.editingFinished.connect(events.Eventos.validoDNI)
            var.rbtSex=(var.ui.rbtFem,var.ui.rbtMasc)
            for i in var.rbtSex:
                i.toggled.connect(events.Eventos.selSexo)
            var.chkPago=(var.ui.chkEfectivo,var.ui.chkTarjeta,var.ui.chkTransf)
            for i in var.chkPago:
                i.stateChanged.connect(events.Eventos.selPago)
            events.Eventos.cargarProv()
            var.ui.cmbProv.activated[str].connect(events.Eventos.selProv)

if __name__=='__main__':
    app=QtWidgets.QApplication([])
    window=Main()
    window.show()
    sys.exit(app.exec())
