# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1112, 815)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 1081, 761))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lblxestion = QtWidgets.QLabel(self.tab)
        self.lblxestion.setGeometry(QtCore.QRect(420, 20, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lblxestion.setFont(font)
        self.lblxestion.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.42, y1:0, x2:0.449, y2:1, stop:0 rgba(245, 0, 255, 255), stop:0.642045 rgba(255, 255, 255, 255))")
        self.lblxestion.setAlignment(QtCore.Qt.AlignCenter)
        self.lblxestion.setObjectName("lblxestion")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 170, 881, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblapel = QtWidgets.QLabel(self.layoutWidget)
        self.lblapel.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblapel.setFont(font)
        self.lblapel.setAlignment(QtCore.Qt.AlignCenter)
        self.lblapel.setObjectName("lblapel")
        self.horizontalLayout_2.addWidget(self.lblapel)
        self.lnApel = QtWidgets.QLineEdit(self.layoutWidget)
        self.lnApel.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lnApel.setObjectName("lnApel")
        self.horizontalLayout_2.addWidget(self.lnApel)
        self.lblnome = QtWidgets.QLabel(self.layoutWidget)
        self.lblnome.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblnome.setFont(font)
        self.lblnome.setAlignment(QtCore.Qt.AlignCenter)
        self.lblnome.setObjectName("lblnome")
        self.horizontalLayout_2.addWidget(self.lblnome)
        self.lnNome = QtWidgets.QLineEdit(self.layoutWidget)
        self.lnNome.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lnNome.setObjectName("lnNome")
        self.horizontalLayout_2.addWidget(self.lnNome)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 200, 881, 73))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblDirec = QtWidgets.QLabel(self.layoutWidget1)
        self.lblDirec.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblDirec.setFont(font)
        self.lblDirec.setObjectName("lblDirec")
        self.horizontalLayout_3.addWidget(self.lblDirec)
        self.lnDir = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lnDir.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lnDir.setObjectName("lnDir")
        self.horizontalLayout_3.addWidget(self.lnDir)
        self.lblProv = QtWidgets.QLabel(self.layoutWidget1)
        self.lblProv.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblProv.setFont(font)
        self.lblProv.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblProv.setObjectName("lblProv")
        self.horizontalLayout_3.addWidget(self.lblProv)
        self.cmbProv = QtWidgets.QComboBox(self.layoutWidget1)
        self.cmbProv.setMaximumSize(QtCore.QSize(300, 16777215))
        self.cmbProv.setObjectName("cmbProv")
        self.horizontalLayout_3.addWidget(self.cmbProv)
        self.layoutWidget2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget2.setGeometry(QtCore.QRect(190, 290, 610, 64))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lblSex = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblSex.setFont(font)
        self.lblSex.setObjectName("lblSex")
        self.horizontalLayout_4.addWidget(self.lblSex)
        self.horlaySex = QtWidgets.QHBoxLayout()
        self.horlaySex.setObjectName("horlaySex")
        self.rbtFem = QtWidgets.QRadioButton(self.layoutWidget2)
        self.rbtFem.setObjectName("rbtFem")
        self.horlaySex.addWidget(self.rbtFem)
        self.rbtMasc = QtWidgets.QRadioButton(self.layoutWidget2)
        self.rbtMasc.setObjectName("rbtMasc")
        self.horlaySex.addWidget(self.rbtMasc)
        self.horizontalLayout_4.addLayout(self.horlaySex)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lblMetodoPago = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblMetodoPago.setFont(font)
        self.lblMetodoPago.setObjectName("lblMetodoPago")
        self.horizontalLayout_5.addWidget(self.lblMetodoPago)
        self.horlayPago = QtWidgets.QHBoxLayout()
        self.horlayPago.setObjectName("horlayPago")
        self.chkEfectivo = QtWidgets.QCheckBox(self.layoutWidget2)
        self.chkEfectivo.setObjectName("chkEfectivo")
        self.horlayPago.addWidget(self.chkEfectivo)
        self.chkTarjeta = QtWidgets.QCheckBox(self.layoutWidget2)
        self.chkTarjeta.setObjectName("chkTarjeta")
        self.horlayPago.addWidget(self.chkTarjeta)
        self.chkTransf = QtWidgets.QCheckBox(self.layoutWidget2)
        self.chkTransf.setObjectName("chkTransf")
        self.horlayPago.addWidget(self.chkTransf)
        self.horizontalLayout_5.addLayout(self.horlayPago)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.layoutWidget3 = QtWidgets.QWidget(self.tab)
        self.layoutWidget3.setGeometry(QtCore.QRect(91, 670, 801, 51))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btnGrabar = QtWidgets.QPushButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.btnGrabar.setFont(font)
        self.btnGrabar.setObjectName("btnGrabar")
        self.horizontalLayout_7.addWidget(self.btnGrabar)
        self.btnModificar = QtWidgets.QPushButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.btnModificar.setFont(font)
        self.btnModificar.setObjectName("btnModificar")
        self.horizontalLayout_7.addWidget(self.btnModificar)
        self.btnEliminar = QtWidgets.QPushButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.btnEliminar.setFont(font)
        self.btnEliminar.setObjectName("btnEliminar")
        self.horizontalLayout_7.addWidget(self.btnEliminar)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_7.addWidget(self.pushButton_3)
        self.btnOk = QtWidgets.QPushButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.btnOk.setFont(font)
        self.btnOk.setObjectName("btnOk")
        self.horizontalLayout_7.addWidget(self.btnOk)
        self.btnsalir = QtWidgets.QPushButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.btnsalir.setFont(font)
        self.btnsalir.setObjectName("btnsalir")
        self.horizontalLayout_7.addWidget(self.btnsalir)
        self.layoutWidget4 = QtWidgets.QWidget(self.tab)
        self.layoutWidget4.setGeometry(QtCore.QRect(80, 100, 851, 60))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget4)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lbldni = QtWidgets.QLabel(self.layoutWidget4)
        self.lbldni.setMinimumSize(QtCore.QSize(75, 0))
        self.lbldni.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbldni.setFont(font)
        self.lbldni.setObjectName("lbldni")
        self.horizontalLayout.addWidget(self.lbldni)
        self.lnDNI = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lnDNI.setMinimumSize(QtCore.QSize(150, 0))
        self.lnDNI.setMaximumSize(QtCore.QSize(20, 16777215))
        self.lnDNI.setObjectName("lnDNI")
        self.horizontalLayout.addWidget(self.lnDNI)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.lblValido = QtWidgets.QLabel(self.layoutWidget4)
        self.lblValido.setMinimumSize(QtCore.QSize(40, 0))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblValido.setFont(font)
        self.lblValido.setText("")
        self.lblValido.setObjectName("lblValido")
        self.horizontalLayout.addWidget(self.lblValido)
        self.lblFecha = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblFecha.setFont(font)
        self.lblFecha.setObjectName("lblFecha")
        self.horizontalLayout.addWidget(self.lblFecha)
        self.lnCalendar = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lnCalendar.setObjectName("lnCalendar")
        self.horizontalLayout.addWidget(self.lnCalendar)
        self.btnCalendar = QtWidgets.QPushButton(self.layoutWidget4)
        self.btnCalendar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/calendario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCalendar.setIcon(icon)
        self.btnCalendar.setIconSize(QtCore.QSize(50, 50))
        self.btnCalendar.setObjectName("btnCalendar")
        self.horizontalLayout.addWidget(self.btnCalendar)
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setGeometry(QtCore.QRect(90, 340, 801, 321))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 799, 319))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.cliTable = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.cliTable.setGeometry(QtCore.QRect(0, 0, 811, 321))
        self.cliTable.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cliTable.setObjectName("cliTable")
        self.cliTable.setColumnCount(3)
        self.cliTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.cliTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cliTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.cliTable.setHorizontalHeaderItem(2, item)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1112, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblxestion.setText(_translate("MainWindow", "Xestion de clientes"))
        self.lblapel.setText(_translate("MainWindow", "Apelidos"))
        self.lblnome.setText(_translate("MainWindow", "Nome"))
        self.lblDirec.setText(_translate("MainWindow", "Direccion"))
        self.lblProv.setText(_translate("MainWindow", "Provincia"))
        self.lblSex.setText(_translate("MainWindow", "Sexo"))
        self.rbtFem.setText(_translate("MainWindow", "Femenino"))
        self.rbtMasc.setText(_translate("MainWindow", "Masculino"))
        self.lblMetodoPago.setText(_translate("MainWindow", "Métodos de pago"))
        self.chkEfectivo.setText(_translate("MainWindow", "Efectivo"))
        self.chkTarjeta.setText(_translate("MainWindow", "Tarjeta"))
        self.chkTransf.setText(_translate("MainWindow", "Transferencia"))
        self.btnGrabar.setText(_translate("MainWindow", "Grabar"))
        self.btnModificar.setText(_translate("MainWindow", "Modificar"))
        self.btnEliminar.setText(_translate("MainWindow", "Eliminar"))
        self.pushButton_3.setText(_translate("MainWindow", "Limpiar"))
        self.btnOk.setText(_translate("MainWindow", "Aceptar"))
        self.btnsalir.setText(_translate("MainWindow", "Salir"))
        self.label.setText(_translate("MainWindow", "codcliente"))
        self.lbldni.setText(_translate("MainWindow", "DNI:"))
        self.lblFecha.setText(_translate("MainWindow", "Fecha de alta"))
        item = self.cliTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DNI"))
        item = self.cliTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Apellidos"))
        item = self.cliTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nombre"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Clientes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Facturación"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
import calendar_rc
