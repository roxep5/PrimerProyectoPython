from datetime import *
from  PyQt5 import QtPrintSupport
import conexion
import productos
import ventas
from Calendar import *
from Eliminar import Ui_Eliminar
from VenSalir import *
from Ventana import *
import sys, events, var, Clients
import locale

from ventas import Ventas
from logoempresa import Ui_About
from modificarProd import Ui_Modificar
from printer import Printer

locale.setlocale(locale.LC_ALL,'es-ES')

class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.dlgsalir=Ui_VenSalir()
        var.dlgsalir.setupUi(self)
        var.dlgsalir.btnboxSalir.button(QtWidgets.QDialogButtonBox.Yes).clicked.connect(events.Eventos.Salir)

class DialogEliminar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogEliminar, self).__init__()
        var.dlgaviso=Ui_Eliminar()
        var.cliente=True
        var.dlgaviso.setupUi(self)
        var.dlgaviso.btnSi.clicked.connect(events.Eventos.Eliminar)
        var.dlgaviso.btnNo.clicked.connect(events.Eventos.Anular)
class DialogAbout(QtWidgets.QDialog):
    def __init__(self):
        super(DialogAbout, self).__init__()
        var.dlgAbout=Ui_About()
        var.dlgAbout.setupUi(self)
        var.dlgAbout.btnNo.clicked.connect(events.Eventos.cerrar)
class DialogModificar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogAbout, self).__init__()
        var.dlgModificar=Ui_Modificar()
        var.dlgModificar.setupUi(self)
        var.dlgModificar.btnNo.clicked.connect(events.Eventos.cerrarMod)
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

class DialogCalendarFactura(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendarFactura,self).__init__()
        var.dlgcalendarF=Ui_Ui_dlgCalendar()
        var.dlgcalendarF.setupUi(self)
        diaactual=datetime.now().day
        mesactual=datetime.now().month
        anoactual=datetime.now().year
        var.dlgcalendarF.calendarWidget.setSelectedDate((QtCore.QDate(anoactual,mesactual,diaactual)))
        var.dlgcalendarF.calendarWidget.clicked.connect(ventas.Ventas.cargarFecha())

class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir,self).__init__()
        self.setWindowTitle('Abrir arcivo')
        self.setModal(True)

class PrintDialogAbrir(QtPrintSupport.QPrintDialog):
    def __init__(self):
        super(PrintDialogAbrir,self).__init__()

class Main(QtWidgets.QMainWindow):

        def __init__(self):
            super(Main, self).__init__()
            var.ui=Ui_MainWindow()
            var.ui.setupUi(self)
            var.ui.statusbar.addPermanentWidget(var.ui.lblstatus,1)
            var.ui.statusbar.addPermanentWidget(var.ui.lblTiempo,2)
            var.ui.lblstatus.setText('Bienvenido a 2º DAM')
            conexion.Conexion.db_connect(var.filebd)

            #conexion.Conexion()
            '''
            conexión con los eventos
            '''
            var.rbtsex=(var.ui.rbtFem,var.ui.rbtMasc)
            var.chkpago = (var.ui.chkEfectivo, var.ui.chkTarjeta, var.ui.chkTransf)
            #var.ui.btnOk.clicked.connect(events.Eventos.Saludo)
            var.ui.btnsalir.clicked.connect(events.Eventos.Salir)
            var.dlgsalir=DialogSalir()
            var.dlgcalendar=DialogCalendar()
            var.dlgcalendarF=DialogCalendarFactura()
            var.dlgaviso = DialogEliminar()
            var.filedlgabrir=FileDialogAbrir()
            var.dlgimprimir=PrintDialogAbrir()
            var.dlgAbout=DialogAbout()
            var.ui.lnDNI.editingFinished.connect(events.Eventos.validoDNI)
            var.ui.btnCalendar.clicked.connect(Clients.Clientes.abrirCalendar)
            var.rbtSex=(var.ui.rbtFem,var.ui.rbtMasc)
            for i in var.rbtSex:
                i.toggled.connect(Clients.Clientes.selSexo)
                print('rbtsex')
            var.chkPago=(var.ui.chkEfectivo,var.ui.chkTarjeta,var.ui.chkTransf)
            for i in var.chkPago:
                i.stateChanged.connect(Clients.Clientes.selPago)
            events.Eventos.cargarProv()
            var.ui.cmbProv.activated[str].connect(Clients.Clientes.selProv)
            var.ui.cliTable.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
            var.ui.btnOk.clicked.connect(Clients.Clientes.showClients)
            var.ui.btnOk.clicked.connect(Clients.Clientes.limpiarCli)
            var.ui.btnModificar.clicked.connect(Clients.Clientes.modifCliente)
            conexion.Conexion.mostrarClientes(self)
            var.ui.btnEliminar.clicked.connect(events.Eventos.mostrarAvisoCli)
            var.ui.btnLimpiar.clicked.connect(Clients.Clientes.limpiarCli)
            var.ui.cliTable.clicked.connect(Clients.Clientes.cargarCliente)
            var.ui.actionsalir.triggered.connect(events.Eventos.Salir)
            var.ui.toolbarSalir.triggered.connect(events.Eventos.Salir)
            #var.ui.btnLimpiar.clicked.connect(Clients.Clientes.limpiarCli)
            #var.ui.btnBuscar.clicked.connect(Clients.Clientes.buscarCli)
            fecha = date.today()
            var.ui.lblTiempo.setText(fecha.strftime('%A %d de %B del %Y'))
            Clients.Clientes.valoresSpin(self)
            var.ui.toolbarAbrir.triggered.connect(events.Eventos.abrirDir)
            var.ui.toolbarImprimir.triggered.connect(events.Eventos.abrirPrinter)
            var.ui.toolbarBackup.triggered.connect(events.Eventos.Backup)
            var.ui.toolbarBackup.triggered.connect(events.Eventos.Backup)
            var.ui.btnBuscar.clicked.connect(events.Eventos.buscarCli)
            #Examen

            var.ui.btnAltaProd.clicked.connect(productos.Productos.nuevoProducto)
            var.ui.btnBajaProd.clicked.connect(productos.Productos.bajaProducto)
            var.ui.btnModificarProd.clicked.connect(productos.Productos.modificarProd)
            var.ui.tableProd.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
            conexion.Conexion.mostrarProductos(self)
            var.ui.tableProd.clicked.connect(productos.Productos.cargarProd)
            var.ui.actionAbout.triggered.connect(events.Eventos.MostrarVentanaAbout)
            var.ui.actionListado_de_clientes.triggered.connect(Printer.reportCli)
            #Facturas
            ventas.Ventas.prepararTabVentas(0)
            var.ui.btnCalendarFactura.clicked.connect(Clients.Clientes.abrirCalendar)




        def closeEvent(self,event):
            if event:
                events.Eventos.Salir(event)

if __name__=='__main__':
    app=QtWidgets.QApplication([])
    window=Main()
    window.show()
    sys.exit(app.exec())

