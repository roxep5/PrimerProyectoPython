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
        MainWindow.resize(1150, 916)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1150, 0))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(50, 40, 1061, 761))
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
        self.layoutWidget.setGeometry(QtCore.QRect(19, 170, 911, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblapel = QtWidgets.QLabel(self.layoutWidget)
        self.lblapel.setMinimumSize(QtCore.QSize(75, 0))
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
        self.lnApel.setMinimumSize(QtCore.QSize(300, 0))
        self.lnApel.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.lnApel.setObjectName("lnApel")
        self.horizontalLayout_2.addWidget(self.lnApel)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
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
        self.lnNome.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.lnNome.setObjectName("lnNome")
        self.horizontalLayout_2.addWidget(self.lnNome)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 200, 911, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblDirec = QtWidgets.QLabel(self.layoutWidget1)
        self.lblDirec.setMinimumSize(QtCore.QSize(75, 0))
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
        self.lnDir.setMinimumSize(QtCore.QSize(300, 0))
        self.lnDir.setMaximumSize(QtCore.QSize(900, 16777215))
        self.lnDir.setObjectName("lnDir")
        self.horizontalLayout_3.addWidget(self.lnDir)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
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
        self.cmbProv.setMinimumSize(QtCore.QSize(150, 0))
        self.cmbProv.setMaximumSize(QtCore.QSize(500, 16777215))
        self.cmbProv.setObjectName("cmbProv")
        self.horizontalLayout_3.addWidget(self.cmbProv)
        self.layoutWidget2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget2.setGeometry(QtCore.QRect(18, 290, 881, 31))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lblSex = QtWidgets.QLabel(self.layoutWidget2)
        self.lblSex.setMaximumSize(QtCore.QSize(50, 16777215))
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
        self.lbledad = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbledad.setFont(font)
        self.lbledad.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbledad.setObjectName("lbledad")
        self.horizontalLayout_6.addWidget(self.lbledad)
        self.spinEdad = QtWidgets.QSpinBox(self.layoutWidget2)
        self.spinEdad.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinEdad.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinEdad.setObjectName("spinEdad")
        self.horizontalLayout_6.addWidget(self.spinEdad)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
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
        self.grpbtnPagos = QtWidgets.QButtonGroup(MainWindow)
        self.grpbtnPagos.setObjectName("grpbtnPagos")
        self.grpbtnPagos.setExclusive(False)
        self.grpbtnPagos.addButton(self.chkEfectivo)
        self.horlayPago.addWidget(self.chkEfectivo)
        self.chkTarjeta = QtWidgets.QCheckBox(self.layoutWidget2)
        self.chkTarjeta.setObjectName("chkTarjeta")
        self.grpbtnPagos.addButton(self.chkTarjeta)
        self.horlayPago.addWidget(self.chkTarjeta)
        self.chkTransf = QtWidgets.QCheckBox(self.layoutWidget2)
        self.chkTransf.setObjectName("chkTransf")
        self.grpbtnPagos.addButton(self.chkTransf)
        self.horlayPago.addWidget(self.chkTransf)
        self.horizontalLayout_5.addLayout(self.horlayPago)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.layoutWidget3 = QtWidgets.QWidget(self.tab)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 120, 911, 41))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblCodcli = QtWidgets.QLabel(self.layoutWidget3)
        self.lblCodcli.setMinimumSize(QtCore.QSize(60, 20))
        self.lblCodcli.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lblCodcli.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lblCodcli.setStyleSheet("background-color: rgb(225, 255, 253)")
        self.lblCodcli.setText("")
        self.lblCodcli.setObjectName("lblCodcli")
        self.horizontalLayout.addWidget(self.lblCodcli)
        self.lbldni = QtWidgets.QLabel(self.layoutWidget3)
        self.lbldni.setMinimumSize(QtCore.QSize(20, 0))
        self.lbldni.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbldni.setFont(font)
        self.lbldni.setObjectName("lbldni")
        self.horizontalLayout.addWidget(self.lbldni)
        self.lnDNI = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lnDNI.setMinimumSize(QtCore.QSize(150, 0))
        self.lnDNI.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lnDNI.setObjectName("lnDNI")
        self.horizontalLayout.addWidget(self.lnDNI)
        self.btnBuscar = QtWidgets.QPushButton(self.layoutWidget3)
        self.btnBuscar.setMaximumSize(QtCore.QSize(30, 30))
        self.btnBuscar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscar.setIcon(icon)
        self.btnBuscar.setIconSize(QtCore.QSize(25, 25))
        self.btnBuscar.setObjectName("btnBuscar")
        self.horizontalLayout.addWidget(self.btnBuscar)
        self.btnLimpiar2 = QtWidgets.QPushButton(self.layoutWidget3)
        self.btnLimpiar2.setMaximumSize(QtCore.QSize(30, 30))
        self.btnLimpiar2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/guardar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLimpiar2.setIcon(icon1)
        self.btnLimpiar2.setIconSize(QtCore.QSize(25, 25))
        self.btnLimpiar2.setObjectName("btnLimpiar2")
        self.horizontalLayout.addWidget(self.btnLimpiar2)
        self.lblValido = QtWidgets.QLabel(self.layoutWidget3)
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
        spacerItem3 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.lblFecha = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblFecha.setFont(font)
        self.lblFecha.setObjectName("lblFecha")
        self.horizontalLayout.addWidget(self.lblFecha)
        self.lnCalendar = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lnCalendar.setObjectName("lnCalendar")
        self.horizontalLayout.addWidget(self.lnCalendar)
        self.btnCalendar = QtWidgets.QPushButton(self.layoutWidget3)
        self.btnCalendar.setAutoFillBackground(False)
        self.btnCalendar.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.btnCalendar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/calendario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCalendar.setIcon(icon2)
        self.btnCalendar.setIconSize(QtCore.QSize(50, 30))
        self.btnCalendar.setObjectName("btnCalendar")
        self.horizontalLayout.addWidget(self.btnCalendar)
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setGeometry(QtCore.QRect(60, 360, 801, 321))
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
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.cliTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.cliTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.cliTable.setHorizontalHeaderItem(2, item)
        self.cliTable.horizontalHeader().setDefaultSectionSize(250)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layoutWidget4 = QtWidgets.QWidget(self.tab)
        self.layoutWidget4.setGeometry(QtCore.QRect(60, 690, 801, 51))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btnOk = QtWidgets.QPushButton(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.btnOk.setFont(font)
        self.btnOk.setObjectName("btnOk")
        self.horizontalLayout_7.addWidget(self.btnOk)
        self.btnModificar = QtWidgets.QPushButton(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.btnModificar.setFont(font)
        self.btnModificar.setObjectName("btnModificar")
        self.horizontalLayout_7.addWidget(self.btnModificar)
        self.btnEliminar = QtWidgets.QPushButton(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.btnEliminar.setFont(font)
        self.btnEliminar.setObjectName("btnEliminar")
        self.horizontalLayout_7.addWidget(self.btnEliminar)
        self.btnLimpiar = QtWidgets.QPushButton(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.btnLimpiar.setFont(font)
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.horizontalLayout_7.addWidget(self.btnLimpiar)
        self.btnsalir = QtWidgets.QPushButton(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.btnsalir.setFont(font)
        self.btnsalir.setObjectName("btnsalir")
        self.horizontalLayout_7.addWidget(self.btnsalir)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.lblstatus = QtWidgets.QLabel(self.centralwidget)
        self.lblstatus.setGeometry(QtCore.QRect(10, 810, 51, 20))
        self.lblstatus.setObjectName("lblstatus")
        self.lblTiempo = QtWidgets.QLabel(self.centralwidget)
        self.lblTiempo.setGeometry(QtCore.QRect(950, 810, 171, 16))
        self.lblTiempo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTiempo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblTiempo.setObjectName("lblTiempo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1150, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuinformes = QtWidgets.QMenu(self.menubar)
        self.menuinformes.setObjectName("menuinformes")
        self.menuAcerca_de = QtWidgets.QMenu(self.menubar)
        self.menuAcerca_de.setObjectName("menuAcerca_de")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMinimumSize(QtCore.QSize(1150, 0))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionsalir = QtWidgets.QAction(MainWindow)
        self.actionsalir.setObjectName("actionsalir")
        self.actionArchivo = QtWidgets.QAction(MainWindow)
        self.actionArchivo.setObjectName("actionArchivo")
        self.toolbarSalir = QtWidgets.QAction(MainWindow)
        self.toolbarSalir.setEnabled(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/56805.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolbarSalir.setIcon(icon3)
        self.toolbarSalir.setIconVisibleInMenu(False)
        self.toolbarSalir.setObjectName("toolbarSalir")
        self.toolbarAbrir = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/62319.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolbarAbrir.setIcon(icon4)
        self.toolbarAbrir.setObjectName("toolbarAbrir")
        self.toolbarImprimir = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/imprimir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolbarImprimir.setIcon(icon5)
        self.toolbarImprimir.setObjectName("toolbarImprimir")
        self.toolbarBackup = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/databackup_theapplication_dedatos_3366.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolbarBackup.setIcon(icon6)
        self.toolbarBackup.setObjectName("toolbarBackup")
        self.actionimprimir_2 = QtWidgets.QAction(MainWindow)
        self.actionimprimir_2.setIcon(icon5)
        self.actionimprimir_2.setObjectName("actionimprimir_2")
        self.actionListado_de_clientes = QtWidgets.QAction(MainWindow)
        self.actionListado_de_clientes.setObjectName("actionListado_de_clientes")
        self.actionImprimir_factura = QtWidgets.QAction(MainWindow)
        self.actionImprimir_factura.setObjectName("actionImprimir_factura")
        self.actionListado_productos = QtWidgets.QAction(MainWindow)
        self.actionListado_productos.setObjectName("actionListado_productos")
        self.menuArchivo.addAction(self.actionArchivo)
        self.menuArchivo.addAction(self.actionimprimir_2)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionsalir)
        self.menuinformes.addAction(self.actionListado_de_clientes)
        self.menuinformes.addAction(self.actionImprimir_factura)
        self.menuinformes.addAction(self.actionListado_productos)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuinformes.menuAction())
        self.menubar.addAction(self.menuAcerca_de.menuAction())
        self.toolBar.addAction(self.toolbarAbrir)
        self.toolBar.addAction(self.toolbarImprimir)
        self.toolBar.addAction(self.toolbarBackup)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolbarSalir)

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
        self.lbledad.setText(_translate("MainWindow", "Edad"))
        self.lblMetodoPago.setText(_translate("MainWindow", "Métodos de pago"))
        self.chkEfectivo.setText(_translate("MainWindow", "Efectivo"))
        self.chkTarjeta.setText(_translate("MainWindow", "Tarjeta"))
        self.chkTransf.setText(_translate("MainWindow", "Transferencia"))
        self.lbldni.setText(_translate("MainWindow", "DNI:"))
        self.lblFecha.setText(_translate("MainWindow", "Fecha de alta"))
        item = self.cliTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DNI"))
        item = self.cliTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Apellidos"))
        item = self.cliTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nombre"))
        self.btnOk.setText(_translate("MainWindow", "Grabar"))
        self.btnModificar.setText(_translate("MainWindow", "Modificar"))
        self.btnEliminar.setText(_translate("MainWindow", "Eliminar"))
        self.btnLimpiar.setText(_translate("MainWindow", "Limpiar"))
        self.btnsalir.setText(_translate("MainWindow", "Salir"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Clientes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Facturación"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.lblstatus.setText(_translate("MainWindow", "TextLabel"))
        self.lblTiempo.setText(_translate("MainWindow", "TextLabel"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuinformes.setTitle(_translate("MainWindow", "Informes"))
        self.menuAcerca_de.setTitle(_translate("MainWindow", "Acerca de"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionsalir.setText(_translate("MainWindow", "Salir"))
        self.actionsalir.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionArchivo.setText(_translate("MainWindow", "Archivo"))
        self.toolbarSalir.setText(_translate("MainWindow", "algo"))
        self.toolbarAbrir.setText(_translate("MainWindow", "algo"))
        self.toolbarImprimir.setText(_translate("MainWindow", "imprimir"))
        self.toolbarBackup.setText(_translate("MainWindow", "backup"))
        self.actionimprimir_2.setText(_translate("MainWindow", "imprimir"))
        self.actionListado_de_clientes.setText(_translate("MainWindow", "Listado de clientes"))
        self.actionImprimir_factura.setText(_translate("MainWindow", "Imprimir factura"))
        self.actionListado_productos.setText(_translate("MainWindow", "Listado productos"))
import abrircarpeta_rc
import backup_rc
import buscar_rc
import calendar_rc
import imprimir_rc
import recargar_rc
import toolbarsalir_rc
