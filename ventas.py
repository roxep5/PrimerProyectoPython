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
            Ventas.cargarFacturas(self)
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
    def cargarFacturas(self):
        try:
            var.subfac=0.00
            var.fac=0.00
            var.iva=0.00
            fila=var.ui.tableNfactura.selectedItems()
            if fila:
                fila=[dato.text() for dato in fila]
            conexion.Conexion.cargarFactura(fila[0])
        except Exception as error:
            print('Error al cargar Factura: %s ' % str(error))
    def procesoVenta(self):
        try:
            var.subfac=0.00
            var.venta=[]
            codfact=var.ui.lblCodFact.text()
            var.venta.append(int(codfact))
            articulo=var.cmbVenta.currentText()
            dato=conexion.Conexion.obtenetCodPrec(articulo)
            var.venta.append(int(dato[0]))
            var.venta.append(articulo)
            row=var.ui.tableArticulos.currentRow()
            cantidad=var.ui.tableArticulos.item(row,2).text()
            cantidad=cantidad.replace(',','.')
            var.venta.append(int(cantidad))
            precio=dato[1].replace(',','.')
            var.venta.append(round(float(precio),2))
            subtotal=round(float(cantidad)*float(dato[1]),2)
            var.venta.append(subtotal)
            var.venta.append(row)
            if codfact!='' and articulo!='' and cantidad!='':
                conexion.Conexion.altaVenta(self)
                '''var.subfac=round(float(subtotal)+float(var.subfac),2)
                var.ui.lblSubtotal.setText(str(var.subfac))
                var.iva=round(float(var.subfac)*0.21,2)
                var.ui.lblIVA.setText(str(var.iva))
                var.fac=round(float(var.iva)+float(var.subfac),2)
                var.ui.lblTotal.setText(str(var.fac))
                '''
                Ventas.mostrarVentas(self)
            else:
                print('Error ')
        except Exception as error:
            print('Error al proceso Venta: %s ' % str(error))
    def mostrarVentas(self):
        try:
            var.cmbVenta=QtWidgets.QComboBox()
            conexion.Conexion.cargarComboVenta(var.cmbVenta)
            codfac=var.ui.lblCodFact.text()
            conexion.Conexion.listadoVentasFact(codfac)
        except Exception as error:
            print('Error en proceso mostrar ventas por factura: %s'%str(error))

    def borrarVenta(self):
        try:
            fila = var.ui.tableArticulos.selectedItems()
            if fila:
                fila = [dato.text() for dato in fila]
                print("sss")
            codventa = int(fila[0])
            conexion.Conexion.borrarVenta(codventa)
            Ventas.mostrarVentas(self)
        except Exception as error:
            print("error al borrar venta de una factura: %s" % str(error))

    def borrarFactura(self):
        try:
            codFactura=int(var.ui.lblCodFact.text())
            conexion.Conexion.borrarFacturas(codFactura)
            conexion.Conexion.borrarVentasFacturas(codFactura)
            Ventas.cargarFacturas(self);
        except Exception as error:
            print("error al borrar venta de una factura: %s"%str(error))





