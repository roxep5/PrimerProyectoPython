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

if __name__=='__main__':
    app=QtWidgets.QApplication([])
    window=Main()
    window.show()
    sys.exit(app.exec())
