# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana1.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ventana1(object):
    def setupUi(self, Ventana1):
        Ventana1.setObjectName("Ventana1")
        Ventana1.resize(527, 388)
        self.centralwidget = QtWidgets.QWidget(Ventana1)
        self.centralwidget.setObjectName("centralwidget")
        self.lblHola = QtWidgets.QLabel(self.centralwidget)
        self.lblHola.setGeometry(QtCore.QRect(210, 110, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.lblHola.setFont(font)
        self.lblHola.setObjectName("lblHola")
        self.btnaceptar = QtWidgets.QPushButton(self.centralwidget)
        self.btnaceptar.setGeometry(QtCore.QRect(220, 240, 75, 23))
        self.btnaceptar.setObjectName("btnaceptar")
        Ventana1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ventana1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 527, 21))
        self.menubar.setObjectName("menubar")
        self.menuarchivo = QtWidgets.QMenu(self.menubar)
        self.menuarchivo.setObjectName("menuarchivo")
        Ventana1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ventana1)
        self.statusbar.setObjectName("statusbar")
        Ventana1.setStatusBar(self.statusbar)
        self.actionsalir = QtWidgets.QAction(Ventana1)
        self.actionsalir.setObjectName("actionsalir")
        self.menuarchivo.addAction(self.actionsalir)
        self.menubar.addAction(self.menuarchivo.menuAction())

        self.retranslateUi(Ventana1)
        QtCore.QMetaObject.connectSlotsByName(Ventana1)

    def retranslateUi(self, Ventana1):
        _translate = QtCore.QCoreApplication.translate
        Ventana1.setWindowTitle(_translate("Ventana1", "MainWindow"))
        self.lblHola.setText(_translate("Ventana1", "Hola mundo"))
        self.btnaceptar.setText(_translate("Ventana1", "Aceptar"))
        self.menuarchivo.setTitle(_translate("Ventana1", "Archivo"))
        self.actionsalir.setText(_translate("Ventana1", "Salir"))
