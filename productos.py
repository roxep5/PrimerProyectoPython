from PyQt5 import QtSql

from Ventana import *

import conexion
import var


class Productos():
    def nuevoProducto(self):
        try:

            newProd=[]

            prod=[var.ui.editNombreProd.text(), var.ui.editPrecioProd.text(),var.ui.editStock.text()]
            print("funciona")
            if prod:
                conexion.Conexion.altaProd(prod)
                conexion.Conexion.mostrarProductos(self)
            else:
                print("faltan datos")
        except Exception as error:
            print('Error buscar clientes: % ' % str(error))
    def bajaProducto(self):

        try:
            id = var.ui.editCod.text()
            conexion.Conexion.bajaProductos(id)
            conexion.Conexion.mostrarProductos(self)
            Productos.cargarProd(self)
        except Exception as error:
            print('Error: baja %s ' % str(error))
    def cargarProd(self):
        try:
            fila = var.ui.tableProd.selectedItems()
            producto = [var.ui.editNombreProd,var.ui.editPrecioProd,var.ui.editStock]
            if fila:
                fila = [dato.text() for dato in fila]

            i = 1
            cod=fila[0]
            print(fila)
            for i, dato in enumerate(producto):
                dato.setText(fila[i])

            conexion.Conexion.cargarProd(cod)
        except Exception as error:
            print('Error: cargar prod %s ' % str(error))


    def modificarProd(self):
        try:
            newdata = []
            client = [
                var.ui.editNombreProd,
                var.ui.editPrecioProd,
                var.ui.editStock,
            ]
            for i in client:
                newdata.append(i.text())
            cod = var.ui.editCod.text()
            conexion.Conexion.modificarProd(cod, newdata)
            conexion.Conexion.mostrarClientes(self)
            Productos.cargarProd(self)
        except Exception as error:
            print('Error: modificar prod %s ' % str(error))