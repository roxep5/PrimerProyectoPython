# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VenSalir.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import aviso_rc

class Ui_VenSalir(object):
    def setupUi(self, VenSalir):
        VenSalir.setObjectName("VenSalir")
        VenSalir.resize(407, 212)
        VenSalir.setModal(True)
        self.btnboxSalir = QtWidgets.QDialogButtonBox(VenSalir)
        self.btnboxSalir.setGeometry(QtCore.QRect(-70, 150, 341, 32))
        self.btnboxSalir.setOrientation(QtCore.Qt.Horizontal)
        self.btnboxSalir.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.btnboxSalir.setObjectName("btnboxSalir")
        self.lblImagen = QtWidgets.QLabel(VenSalir)
        self.lblImagen.setGeometry(QtCore.QRect(90, 60, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.lblImagen.setFont(font)
        self.lblImagen.setObjectName("lblImagen")
        self.label_2 = QtWidgets.QLabel(VenSalir)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 71, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/aviso2.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(VenSalir)
        self.btnboxSalir.accepted.connect(VenSalir.accept)
        self.btnboxSalir.rejected.connect(VenSalir.reject)
        QtCore.QMetaObject.connectSlotsByName(VenSalir)

    def retranslateUi(self, VenSalir):
        _translate = QtCore.QCoreApplication.translate
        VenSalir.setWindowTitle(_translate("VenSalir", "Dialog"))
        self.lblImagen.setText(_translate("VenSalir", "¿Estás seguro de que quieres salir de la aplicación?"))