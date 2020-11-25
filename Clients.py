from Ventana import *

import conexion
import var


class Clientes():
    def validarDNI(dni):
        try:
            tabla="TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext="XYZ"
            reemp_dig_ext={'X':'0','Y':'1','Z':'2'}
            numeros='1234567890'
            dni=dni.upper()
            if(len(dni)==9):
                dig_control=dni[8]
                dni=dni[:8]
                if(dni[0]in dig_ext):
                    dni=dni.replace(dni[0],reemp_dig_ext[dni[0]])
                return len(dni)==len([n for n in dni if n in numeros]) and tabla[int(dni)%23]==dig_control
            return False
        except:
            print('Error en el modulo de validacion del DNI')
            return None
    def abrirCalendar():
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error: %s '%str(error))
    def cargarFecha(qDate):
        try:
            data=('{0}/{1}/{2}'.format(qDate.day(),qDate.month(),qDate.year()))
            var.ui.lnCalendar.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print('Error al cargar fecha: %s '%str(error))

    def selProv(prov):
        try:
            # print('Has se leccionado la provincia de ', prov)
            # return prov
            global vpro
            vpro = prov
        except Exception as error:
            print('Error: %s selprov ' % str(error))

    def selSexo():
        try:
            if var.ui.rbtFem.isChecked():
                var.sex = 'Mujer'
            if var.ui.rbtMasc.isChecked():
                var.sex = 'Hombre'
        except Exception as error:
            print('Error: selsxo %s ' % str(error))

    def selPago():
        try:
            var.pay=[]
            for i, data in enumerate(var.ui.grpbtnPagos.buttons()):

                if data.isChecked() and i==0:
                    # print('pagas con efectivo')
                    var.pay.append('Efectivo')
                if data.isChecked() and i==1:
                    # print('pagas con tarjeta')
                    var.pay.append('Tarjeta')
                if data.isChecked() and i==2:
                    # print('pagas con Transferencia')
                    var.pay.append('Transferencia')
            return var.pay
        except Exception as error:
            print('Error: selpago %s ' % str(error))

    def showClients(self):
        # preparamos el registro
        '''try:

            newcli = []  # contiene todos los datos
            clitab = []  # será lo que carguemos en la tablas
            client = [var.ui.lnDNI, var.ui.lnApel, var.ui.lnNome, var.ui.lnCalendar, var.ui.lnDir]
            k = 0
            for i in client:
                newcli.append(i.text())  # cargamos los valores que hay en los editline
                if k < 3:
                    clitab.append(i.text())
                    k += 1
            newcli.append(vpro)
            newcli.append(var.sex)
            var.pay2 = Clientes.selPago()
            newcli.append(var.pay2)
            if client:
                # comprobarmos que no esté vacío lo principal
                # aquí empieza como trabajar con la TableWidget
                row = 0
                column = 0
                var.ui.cliTable.insertRow(row)
                for registro in clitab:
                    cell = QtWidgets.QTableWidgetItem(registro)
                    var.ui.cliTable.setItem(row, column, cell)
                    column += 1
                conexion.Conexion.altaCli(newcli)
            else:
                print('Faltan Datos')
            # Clientes.limpiarCli()
        except Exception as error:
            print('Error cargar fecha lo : %s ' % str(error))
        '''
        try:
            newcli=[]
            clitab=[]
            client=[var.ui.lnDNI,var.ui.lnApel,var.ui.lnNome,var.ui.lnCalendar,var.ui.lnDir]
            k=0
            for i in client:
                newcli.append(i.text())
                if k<3:
                    clitab.append(i.text())
                    k+=1
            newcli.append(vpro)
            #elimina duplicados
            var.pay2=Clientes.selPago()
            newcli.append(var.sex)
            newcli.append(var.pay2)

            if client:


                row=0
                column=0
                var.ui.cliTable.insertRow(row)
                for registro in clitab:
                    cell=QtWidgets.QTableWidgetItem(registro)
                    var.ui.cliTable.setItem(row,column,cell)
                    column+=1
                conexion.Conexion.altaCli(newcli)
            else:
                print('Faltan datos')
           # Clientes.limpiarCli(client)
        except Exception as error:
            print('Error: show %s ' % str(error))  

    def cargarCliente(self):
        try:
            fila=var.ui.cliTable.selectedItems()
            client=[var.ui.lnDNI,var.ui.lnApel,var.ui.lnNome]
            if fila:
                fila=[dato.text() for dato in fila]
            print(fila)
            i=0
            for i, dato in enumerate(client):
                dato.setText(fila[i])
            conexion.Conexion.cargarCliente(self)
        except Exception as error:
            print('Error: cargar %s ' % str(error))

    def bajaCliente(self):

        try:
            dni=var.ui.lnDNI.text()
            conexion.Conexion.bajaCli(dni)
            conexion.Conexion.mostrarClientes(self)
            Clientes.limpiarCli(self)
        except Exception as error:
            print('Error: baja %s ' % str(error))

    def limpiarCli(self):
        try:
            client=[var.ui.lnDNI,var.ui.lnApel,var.ui.lnNome,var.ui.lnCalendar,var.ui.lnDir]
            for i in range(len(client)):
                client[i].setText('')
            var.ui.grpbtnPagos.setExclusive(False)
            for dato in var.sex:
                dato.setChecked(False)
            for data in var.chkpago:
                data.setChecked(False)
            var.ui.cmbProv.setCurrentIndex(0)
            var.ui.lblValidar.setText('')
        except Exception as error:
            print('Error: %s ' % str(error))
            #ver que hostia falta
    def modifCliente(self):
        try:
            newdata=[]
            client=[
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
            var.pay=Clientes.selPago()
            print(var.pay)
            newdata.append(var.pay)
            cod=var.ui.lblCodcli.text()
            conexion.Conexion.modifCli(cod,newdata)
            conexion.Conexion.mostrarClientes(self)
        except Exception as error:
            print('Error: %s ' % str(error))