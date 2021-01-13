from PyQt5 import QtSql
from reportlab.pdfgen import canvas
import os, var
from  datetime import datetime
class Printer():
    '''def cabecera(self):
        #logo=
    def pie(self):
        var.rep.line(50,50,525,50)
        fecha=datetime.today()
        fecha=fecha.strftime('%d.%n.%Y %H.%M.%S')
    '''
    def reportCli(self):
        try:
            var.rep=canvas.Canvas('informes/listadoclientes.pdf')
            Printer.cabecera(self)
            var.rep.setFont('Helvetica-Bold',size=9)
            textlistado='LISTADO DE CLIENTES'
            var.rep.drawString(100,750,textlistado)
            var.rep.line(45,730,525,730)
            itemcli=['Cod','DNI','APELLIDOS','NOMBRE','FECHA ALTA']
            #TERMINAR
            var.rep.drawString(45,710,itemcli[0])
            var.rep.drawString(90,710,itemcli[1])
            var.rep.drawString(180,710,itemcli[2])
            var.rep.drawString(325,710,itemcli[3])
            var.rep.drawString(465,710,itemcli[4])
            var.rep.line(45,703,525,703)
            query=QtSql.QSqlQuery()
            query.prepare('select codigo, dni, apelidos, nome, fechalta from clientes order by apelidos, nome')
            var.rep.setFont('Helvetica',size=10)
            if query.exec_():
                i=50
                j=690
                while query.next():
                    var.rep.drawString(i,j,str(query.value(0)))
                    var.rep.drawString(i+30,j,str(query.value(1)))
                    var.rep.drawString(i+130,j,str(query.value(2)))
                    var.rep.drawString(i+280,j,str(query.value(3)))
                    var.rep.drawRightString(i+470,j,str(query.value(4)))
                    j=j-30
            Printer.pie(textlistado)
            var.rep.save()
            rootPath= ".\\informes"
            cont=0
            for file in os.listdir(rootPath):
                if file.endswith('.pdf'):
                    os.startfile("%s/%s"%(rootPath,file))
                cont=cont+1
        except Exception as error:
           print('Error reporcli %s'%str(error))

    def cabecera(self):
        try:

            var.rep.setTitle('INFORMES')
            var.rep.setAuthor('Administracion')
            var.rep.setFont('Helvetica',size=10)
            var.rep.line(45,820,525,820)
            var.rep.line(45,745,525,745)
            textcif='A0000000H'
            textnom='IMPORTACION Y EXPORTACION TEIS, S.L.'
            textdir='Avenida de Galicia, 101-vigo'
            texttlf='886 12 04 64'
            var.rep.drawString(50,805,textcif)
            var.rep.drawString(50,790,textnom)
            var.rep.drawString(50,775,textdir)
            var.rep.drawString(50,760,texttlf)
        except Exception as error:
            print('Error en la cabecera del informe: %s'%str(error))
    def pie(textlistado):
        try:
            var.rep.line(50,50,525,50)
            fecha=datetime.today()
            fecha=fecha.strftime('%d.%m.%Y %H.%M.%S')
            var.rep.setFont('Helvetica-Oblique',size=7)
            var.rep.drawString(460,40,str(fecha))
            var.rep.drawString(275,40,str('Página %s'%var.rep.getPageNumber()))
            var.rep.drawString(50,40,str(textlistado))
        except Exception as error:
            print('Error en el pie del informe: %s'%str(error))