from reportlab.pdfgen import canvas
import os, var
from  datetime import datetime
class Printer()
    '''def cabecera(self):
        #logo=
    def pie(self):
        var.rep.line(50,50,525,50)
        fecha=datetime.today()
        fecha=fecha.strftime('%d.%n.%Y %H.%M.%S')
    '''
    def reportCli(self):
        try:
            var.rep=canvas.Canvas('informes/listadoclientes.pdf',pagesize=A4)
            Printer.cabecera(self)
            var.rep.setFont('Helvetica-Bold',size=9)
            var.rep.drawString(100,750,'Listado Clientes')
            var.rep.line(45,730,525,730)
            itemcli=['Cod','DNI','APELLIDOS','NOMBRE','FECHA ALTA']
            #TERMINAR
            var.rep.save()
            rootPath= ".\\informes"
            cont=0
            for file in os.listdir(rootPath)
                if file.endswith('.pdf')
                    os.startfile("%s/%s"%(rootPath,file))
                cont=cont+1
        except Exception as error:
           print('Error reporcli %s'%str(error))

    def cabecera(self):
        var.rep.setTitle('INFORMES')
        var.rep.setAuthor('Administracion')
        var.rep.setFont('Helvetoica',size=10)
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
