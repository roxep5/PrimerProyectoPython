import var
import conexion
from PyQt5 import QtWidgets, QtCore
from time import sleep
from Ventana import *

class Ventas:
    '''def altafactura(self):
        try:
            dni=var.ui.editDniFactura.text()
            fecha=var.editFechaFactura.text()
            apelidos=var.ui.editApelidosFactura.text()
            if dni!=''and fecha!='':


        except Exception as error:
        print('Error alta factura %s '%str(error))
    '''
    def prepararTabVentas(index):
        try:
            var.cmbVenta=QtWidgets.QComboBox()
            conexion.Conexion.cargarCmbVenta(var.cmbVenta)
            var.ui.tableArticulos.setRowCount(index +1)
            var.ui.tableArticulos.setItem(index,0,QtWidgets.QTableWidgetItem())
            var.ui.tableArticulos.setCellWidget(index,1,var.cmbVenta)
            var.ui.tableArticulos.setItem(index, 2, QtWidgets.QTableWidgetItem())
            var.ui.tableArticulos.setItem(index, 3, QtWidgets.QTableWidgetItem())
            var.ui.tableArticulos.setItem(index, 4, QtWidgets.QTableWidgetItem())
        except Exception as error:
            print("Preparar tabla de ventas: %s"% str(error))
    def altaFactura(self):
        try:
            dni=var.ui.editDniFactura.text()
            fecha=var.ui.editFechaFactura.text()
            apel=var.ui.editApelido.text()
            if dni!='' and fecha!='':
                conexion.Conexion.altaFact(dni, fecha, apel)
        except Exception as error:
            print("Error alta factura: %s" % str(error))

    def cargarFecha(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.editFechaFactura.setText(str(data))
            var.dlgcalendarF.hide()
        except Exception as error:
            print('Error al cargar fecha: %s ' % str(error))
    def abrirCalendar(self):
        try:
            var.dlgcalendarF.show()
        except Exception as error:
            print('Error: %s ' % str(error))