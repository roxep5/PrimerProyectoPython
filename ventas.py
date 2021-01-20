import var
import conexion
from PyQt5 import QtWidgets, QtCore
from time import sleep


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