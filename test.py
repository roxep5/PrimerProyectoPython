import unittest

from PyQt5 import QtSql

import Clients
import conexion
import var


class MyTestCase(unittest.TestCase):
    def test_conexion(self):
        value=conexion.Conexion.db_connect(var.filebd)
        msg = 'Conexion no válida'
        self.assertTrue(value,msg)

    def test_dni(self):
        dni = '00000000T'
        value = Clients.Clientes.validarDNI(str(dni))
        msg = 'Proba DNI Errónea'
        self.assertTrue(value, msg)

    def test_fact(self):
        valor=181.44
        codfac=1
        try:
            msg = 'Cálculos incorrectos'
            var.subfac =0.00
            query=QtSql.QSqlQuery()
            query1=QtSql.QSqlQuery()
            query.prepare('Select clientes, codart, cantidad from ventas where codfact = :codfact')
            query.bindValue(':codfact',int(codfac))
            if query.exec_():
                while query.next():
                    codarticventa=query.value(1)
                    cantidad=query.value(2)
                    query1.prepare('select nomeprod, preciounidad from productos where codigo = :codigo')
                    query1.bindValue(':codigo',int(codarticventa))
                    if query1.exec_():
                        while query1.next():
                            precio=query1.value(1)
                            subtotal=round(float(cantidad)*float(precio), 2)
                    var.subfac = round(float(subtotal) + float(var.subfac), 2)
            var.iva = round(float(var.subfac) * 0.21,2)
            var.fac = round(float(var.iva) + float(var.subfac),2)
        except Exception as error:
            print('Error listado de la tabla de ventas: %s'%str(error))
        self.assertEqual(round(float(valor),2), round(float(var.fac),2),msg)

    def test_cargar_cliente(self):
        print("Hola")
        nombre = "God of war"
        codigo=1
        msg = "Error no se ha cargado bien"

        print("Hola")
        value = conexion.Conexion.comprobarNombre(int(codigo))
        self.assertEqual(nombre, value, msg)

if __name__ == '__main__':
    unittest.main()
