from datetime import *

from Calendar import *
from VenSalir import *
from Ventana import *
import sys
import events
import var
import Clients
class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.dlgsalir=Ui_VenSalir()
        var.dlgsalir.setupUi(self)
        var.dlgsalir.btnboxSalir.button(QtWidgets.QDialogButtonBox.Yes).clicked.connect(events.Eventos.Salir)

class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar,self).__init__()
        var.dlgcalendar=Ui_Ui_dlgCalendar()
        var.dlgcalendar.setupUi(self)
        diaactual=datetime.now().day
        mesactual=datetime.now().month
        anoactual=datetime.now().year
        var.dlgcalendar.calendarWidget.setSelectedDate((QtCore.QDate(anoactual,mesactual,diaactual)))
        var.dlgcalendar.calendarWidget.clicked.connect(Clients.Clientes.cargarFecha)

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
            var.dlgsalir=DialogSalir()
            var.dlgcalendar=DialogCalendar()
            var.ui.lnDNI.editingFinished.connect(events.Eventos.validoDNI)
            var.ui.btnCalendar.clicked.connect(Clients.Clientes.abrirCalendar)
            var.rbtSex=(var.ui.rbtFem,var.ui.rbtMasc)
            for i in var.rbtSex:
                i.toggled.connect(Clients.Clientes.selSexo)
            var.chkPago=(var.ui.chkEfectivo,var.ui.chkTarjeta,var.ui.chkTransf)
            for i in var.chkPago:
                i.stateChanged.connect(Clients.Clientes.selPago)
            events.Eventos.cargarProv()
            var.ui.cmbProv.activated[str].connect(Clients.Clientes.selProv)
            var.ui.cliTable.clicked.connect(Clients.Clientes.cargarCliente)
            var.ui.cliTable.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
            var.ui.btnOk.clicked.connect(Clients.Clientes.showClients)
            var.ui.btnOk.clicked.connect(Clients.Clientes.limpiarCli)
        def closeEvent(self,event):
            if event:
                events.Eventos.Salir(event)

if __name__=='__main__':
    app=QtWidgets.QApplication([])
    window=Main()
    window.show()
    sys.exit(app.exec())

