# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Eliminar.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Eliminar(object):
    def setupUi(self, Eliminar):
        Eliminar.setObjectName("Eliminar")
        Eliminar.resize(469, 275)
        Eliminar.setModal(True)
        self.lblAviso = QtWidgets.QLabel(Eliminar)
        self.lblAviso.setGeometry(QtCore.QRect(120, 150, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblAviso.setFont(font)
        self.lblAviso.setObjectName("lblAviso")
        self.label_2 = QtWidgets.QLabel(Eliminar)
        self.label_2.setGeometry(QtCore.QRect(150, 30, 141, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/kisspng-warning-sign-computer-icons-symbol-clip-art-alert-icon-image-gallery-5ab048f60c5a21.2844429515215024540506.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(Eliminar)
        self.widget.setGeometry(QtCore.QRect(130, 210, 158, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnSi = QtWidgets.QPushButton(self.widget)
        self.btnSi.setObjectName("btnSi")
        self.horizontalLayout.addWidget(self.btnSi)
        self.btnNo = QtWidgets.QPushButton(self.widget)
        self.btnNo.setObjectName("btnNo")
        self.horizontalLayout.addWidget(self.btnNo)

        self.retranslateUi(Eliminar)
        QtCore.QMetaObject.connectSlotsByName(Eliminar)

    def retranslateUi(self, Eliminar):
        _translate = QtCore.QCoreApplication.translate
        Eliminar.setWindowTitle(_translate("Eliminar", "Dialog"))
        self.lblAviso.setText(_translate("Eliminar", "¿Seguro que quieres eliminar?"))
        self.btnSi.setText(_translate("Eliminar", "Si"))
        self.btnNo.setText(_translate("Eliminar", "No"))
import aviso2_rc
