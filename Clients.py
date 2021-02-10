from Ventana import *

import conexion
import var


class Clientes():
    def validarDNI(dni):
        '''

        Móudulo que valida la letra de un dni según sea nacional o extranjerao

        :param a: dni
        :type: string
        :return: None
        :rtype: bool

        Pone la letra en mayúsculas, comprueba que son nueve caracteres. Toma los 8 primeros, si extranjero
        cambia la letra por el número, y aplica el algoritmo de comprobación de la letra basado en la normativa
        Si es correcto devuelve True, si es falso devuelva False

        '''
        try:

            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = '1234567890'
            dni = dni.upper()
            if (len(dni) == 9):
                dig_control = dni[8]
                dni = dni[:8]
                if (dni[0] in dig_ext):
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control
            return False
        except:
            print('Error en el modulo de validacion del DNI')
            return None

    def abrirCalendar():
        try:
            '''
            modulo que abre el calendario para introducirlo en el editText
            '''
            var.dlgcalendar.show()
        except Exception as error:
            print('Error: %s ' % str(error))

    def cargarFecha(qDate):
        '''
        carga la fecha en el edit text
        :rtype: object
        recibe el qdate y lo pasa al edit text en formato string
        '''
        try:

            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.lnCalendar.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print('Error al cargar fecha: %s ' % str(error))

    def selProv(prov):
        try:
            '''

            Al seleccion una provincia en el combo de provincias llamba al evento cmbProv.activated que devuelve
            la provincia selecccionada

            :param a: provincia seleccionada
            :type a: string
            :return: None
            :rtype: None

            '''
            # print('Has se leccionado la provincia de ', prov)
            # return prov
            global vpro
            vpro = prov
        except Exception as error:
            print('Error: %s selprov ' % str(error))

    def selSexo():
        try:
            '''
            Modulo que según checkemos el rbtbutton Fem o Masc carga el texto correspondiente de Mujer o Hombre a la
            variable var.sex que luego se añade a la lista de los datos del cliente a incluir en la BBDD

            :return: None
            :rtype: None

                    '''
            if var.ui.rbtFem.isChecked():
                var.sex = 'Mujer'
            if var.ui.rbtMasc.isChecked():
                var.sex = 'Hombre'
        except Exception as error:
            print('Error: selsxo %s ' % str(error))

    def selPago():
        try:
            '''

            Cheque que valores de paga seleccion en el checkbos y los añade a una variable lista var.py

            :return: None

            En QtDesigner se debe agrupar los checkbox en un ButtonGroup

            '''
            var.pay = []
            for i, data in enumerate(var.ui.grpbtnPagos.buttons()):

                if data.isChecked() and i == 0:
                    # print('pagas con efectivo')
                    var.pay.append('Efectivo')
                if data.isChecked() and i == 1:
                    # print('pagas con tarjeta')
                    var.pay.append('Tarjeta')
                if data.isChecked() and i == 2:
                    # print('pagas con Transferencia')
                    var.pay.append('Transferencia')
            return var.pay
        except Exception as error:
            print('Error: selpago %s ' % str(error))

    def showClients(self):
        # preparamos el registro
        """

        Módulo que carga los datos del cliente

        :param a: None
        :param b: None
        :return: None

        Se crea una lista newcli que contendrá todos los datos del cliente que se introduzcan en los widgets,
        esta lista se pasa como argumento al módulo altaCli del módulo Conexión.
        El módulo llama a la función mostrarClientes que recarga la tabla con todos los clientes además del nuevo
        El módulo llama a la función limpiarCli que vacía el contenido de los widgets.

        """
        try:
            newcli = []
            clitab = []
            client = [var.ui.lnDNI, var.ui.lnApel, var.ui.lnNome, var.ui.lnCalendar, var.ui.lnDir,var.ui.spinEdad]
            intedad=client[5]
            k = 0
            for i in client:
                newcli.append(i.text())
                if k < 3:
                    clitab.append(i.text())
                    k += 1
            newcli.append(vpro)
            # elimina duplicados
            var.pay2 = Clientes.selPago()
            newcli.append(var.sex)
            newcli.append(var.pay2)

            if client:

                row = 0
                column = 0
                var.ui.cliTable.insertRow(row)
                for registro in clitab:
                    cell = QtWidgets.QTableWidgetItem(registro)
                    var.ui.cliTable.setItem(row, column, cell)
                    column += 1
                conexion.Conexion.altaCli(newcli)
            else:
                print('Faltan datos')
        # Clientes.limpiarCli(client)
        except Exception as error:
            print('Error: show %s ' % str(error))

    def cargarCliente(self):
        '''

        Limpia datos formulario y recarga la tabla de clientes llamando al módulo mostrarClientes de la clase
        Conexion

        :return: None

        '''
        try:
            fila = var.ui.cliTable.selectedItems()
            client = [var.ui.lnDNI, var.ui.lnApel, var.ui.lnNome]
            if fila:
                fila = [dato.text() for dato in fila]
            print(fila)
            i = 0
            for i, dato in enumerate(client):
                dato.setText(fila[i])
            conexion.Conexion.cargarCliente(self)
        except Exception as error:
            print('Error: cargar %s ' % str(error))

    def bajaCliente(self):
        """

        Módulo que da de baja un cliente a partir del dni. Además recarga el widget tablaCli con los datos actualizados
        desde la BBDD

        :return: None
        :rtype: None

        Toma el dni cargado en el widget editDni se lo pasa al módulo bajaCli de la clase Conexión y da de bja el cliente.
        Limpia los datos del formulario y recarga tablaCli

        """
        try:
            dni = var.ui.lnDNI.text()
            conexion.Conexion.bajaCli(dni)
            conexion.Conexion.mostrarClientes(self)
            Clientes.limpiarCli(self)
        except Exception as error:
            print('Error: baja %s ' % str(error))

    def limpiarCli(self):
        try:
            '''

            Modulo que vacía o limpia los datos del formulario cliente

            :return: None

            En los checkbox y radiobutton los pone a False.

            '''
            client = [var.ui.lnDNI, var.ui.lnApel, var.ui.lnNome, var.ui.lnCalendar, var.ui.lnDir]

            for i in range(len(client)):
                client[i].setText('')

            var.ui.grpbtnPagos.setExclusive(False)
            print("range")
            for dato in var.rbtsex:
                dato.setChecked(False)
                print("sex")
            for data in var.chkpago:
                data.setChecked(False)
                print("pago")
            var.ui.cmbProv.setCurrentIndex(0)
            var.ui.lblValido.setText('')
            var.ui.lblCodcli.setText('')
            var.ui.spinEdad.setValue(18)
        except Exception as error:
            print('Error: limpiar %s ' % str(error))
            # ver que hostia falta

    def modifCliente(self):
        try:
            """

            Módulos para modificar datos de un cliente con determinado código

            :return: None
            :rtype: None

            A partir del código del cliente, lee los nuevos datos de los widgets que se han cargado y modificado,
            llama al módulo modifCli de la clase Conexión para actualizar los datos en la BBDD pasándole una lista con
            los nuevos datos.
            Vuelve a mostrar la tablaCli actualizada pero no limpia datos de los widgets.

            """
            newdata = []
            client = [
                var.ui.lnDNI,
                var.ui.lnApel,
                var.ui.lnNome,
                var.ui.lnCalendar,
                var.ui.lnDir
            ]
            for i in client:
                newdata.append(i.text())
            newdata.append(var.ui.cmbProv.currentText())
            newdata.append(var.sex)
            var.pay = Clientes.selPago()
            print(var.pay)
            newdata.append(var.pay)
            cod = var.ui.lblCodcli.text()
            conexion.Conexion.modifCli(cod, newdata)
            conexion.Conexion.mostrarClientes(self)
        except Exception as error:
            print('Error: %s ' % str(error))

    def valoresSpin(self):
        try:
            '''

            Módulo que se lanza con el programa cargando por defecto el valor 16 en el spinEdad

            :return: None
            :rtype: None

            '''
            var.ui.spinEdad.setValue(18)
            #var.ui.spinEdad.(150)
            #var.ui.spinEdad.setMinimun(18)
        except Exception as error:
            print('Error valores spin: %s ' % str(error))
