from PyQt5 import QtSql

from Ventana import *

import conexion
import var


class Productos():
    def nuevoProducto(self):
        try:

            newProd=[]

            prod=[var.ui.editNombreProd.text(), var.ui.editPrecioProd.text()]
            print("funciona")
            if prod:
                conexion.Conexion.altaProd(prod)
            else:
                print("faltan datos")
        except Exception as error:
            print('Error buscar clientes: % ' % str(error))
    def bajaProducto(self):

        try:
            id = var.ui.editCod.text()
            conexion.Conexion.bajaProductos(id)
            conexion.Conexion.mostrarProductos(self)
        except Exception as error:
            print('Error: baja %s ' % str(error))
    def cargarProd(self):
        fila = var.ui.tableProd.selectedItems()
        producto = [var.ui.editCod,var.ui.editNombreProd, var.ui.editPrecioProd]
        if fila:
            fila = [dato.text() for dato in fila]

        i = 0
        print(fila)
        for i, dato in enumerate(producto):
            dato.setText(fila[i])

        conexion.Conexion.cargarProd(self)
    def modificarProd(self):
        try:
            newdata = []
            client = [
                var.ui.editNombreProd,
                var.ui.editPrecioProd,
            ]
            for i in client:
                newdata.append(i.text())
            cod = var.ui.editCod.text()
            conexion.Conexion.modificarProd(cod, newdata)
            conexion.Conexion.mostrarClientes(self)
        except Exception as error:
            print('Error: %s ' % str(error))