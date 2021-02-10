from PyQt5 import QtSql

from Ventana import *

import conexion
import var


class Productos():
    def nuevoProducto(self):
        '''

        Módulo que insertar los proudctos en la tabla y en la base de datos
        en las búsquedas mostrará los datos del producto
        :return: None
        :rtype: None
        '''
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
        """

        Módulo para dar de baja un producto y recarga la tabla productos y limpia el formulario productos

        :return: None
        :type: None

        """
        try:
            id = var.ui.editCod.text()
            conexion.Conexion.bajaProductos(id)
            conexion.Conexion.mostrarProductos(self)
            Productos.cargarProd(self)
        except Exception as error:
            print('Error: baja %s ' % str(error))
    def cargarProd(self):
        '''

        Módulo que carga en widgets formulario productos la fila que se clickea en la tablaPro

        :return: None
        :type: None

        '''
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
        """

        Módulo para modificar datos de un producto con determinado código

        :return: None
        :rtype: None

        Además recarga la tabla de productos con los valores actualizados

        """
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