from PyQt5.QtWidgets import *

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
            print('Error: %s ' % str(error))

    def selSexo():
        try:
            if var.ui.rbtFem.isChecked():
                var.sex = 'Mujer'
            if var.ui.rbtMasc.isChecked():
                var.sex = 'Hombre'
        except Exception as error:
            print('Error: %s ' % str(error))

    def selPago():
        try:
            if var.ui.chkEfectivo.isChecked():
                # print('pagas con efectivo')
                var.pay.append('Efectivo')
            if var.ui.chkTarjeta.isChecked():
                # print('pagas con tarjeta')
                var.pay.append('Tarjeta')
            if var.ui.chkTransf.isChecked():
                # print('pagas con Transferencia')
                var.pay.append('Transferencia')
        except Exception as error:
            print('Error: %s ' % str(error))

    def showClients():
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
            var.pay=set(var.pay)
            for j in var.pay:
                newcli.append(j)
           # newcli.append(var.sex)
            print(newcli)
            print(clitab)
            row=0
            column=0
            var.ui.cliTable.insertRow(row)
            for registro in clitab:
                cell=QTableWidgetItem(registro)
                var.ui.cliTable.setItem(row,column,cell)
                column+=1
        except Exception as error:
            print('Error: %s ' % str(error))
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
        except Exception as error:
            print('Error: %s ' % str(error))
    def limpiarCli():
        '''

        :param listaRbtSex:
        :param ListaChkpay:
        :return: none
        '''
        try:
            client=[var.ui.lnDNI,var.ui.lnApel,var.ui.lnNome,var.ui.lnCalendar,var.ui.lnDir]
            for i in range(len(client)):
                client[i].setText('')
            var.ui.horlayPago.setExclusive(False)
            '''for dato in var.sex:
                dato.setChecked
            for data in var.:
                data.setChecked(False)'''
            var.ui.cmbProv.setCurrentIndex(0)
            var.ui.lblValidar.setText('')
        except Exception as error:
            print('Error: %s ' % str(error))