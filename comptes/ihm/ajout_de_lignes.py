# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ajout_de_lignes.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 150)
        MainWindow.setMinimumSize(QtCore.QSize(470, 150))
        MainWindow.setMaximumSize(QtCore.QSize(470, 150))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 90, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 90, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 90, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 90, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.l_libelle = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_libelle.sizePolicy().hasHeightForWidth())
        self.l_libelle.setSizePolicy(sizePolicy)
        self.l_libelle.setMinimumSize(QtCore.QSize(130, 20))
        self.l_libelle.setMaximumSize(QtCore.QSize(130, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_libelle.setFont(font)
        self.l_libelle.setStyleSheet("color: rgb(240, 240, 240);")
        self.l_libelle.setObjectName("l_libelle")
        self.gridLayout.addWidget(self.l_libelle, 0, 0, 1, 1)
        self.LE_libelle = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LE_libelle.sizePolicy().hasHeightForWidth())
        self.LE_libelle.setSizePolicy(sizePolicy)
        self.LE_libelle.setMinimumSize(QtCore.QSize(200, 20))
        self.LE_libelle.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.LE_libelle.setFont(font)
        self.LE_libelle.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.LE_libelle.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LE_libelle.setReadOnly(False)
        self.LE_libelle.setObjectName("LE_libelle")
        self.gridLayout.addWidget(self.LE_libelle, 0, 1, 1, 1)
        self.B_ajouter = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.B_ajouter.sizePolicy().hasHeightForWidth())
        self.B_ajouter.setSizePolicy(sizePolicy)
        self.B_ajouter.setMinimumSize(QtCore.QSize(80, 50))
        self.B_ajouter.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.B_ajouter.setFont(font)
        self.B_ajouter.setObjectName("B_ajouter")
        self.gridLayout.addWidget(self.B_ajouter, 0, 2, 2, 1)
        self.l_montant = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_montant.sizePolicy().hasHeightForWidth())
        self.l_montant.setSizePolicy(sizePolicy)
        self.l_montant.setMinimumSize(QtCore.QSize(130, 20))
        self.l_montant.setMaximumSize(QtCore.QSize(130, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_montant.setFont(font)
        self.l_montant.setStyleSheet("color: rgb(240, 240, 240);")
        self.l_montant.setObjectName("l_montant")
        self.gridLayout.addWidget(self.l_montant, 1, 0, 1, 1)
        self.LE_montant = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LE_montant.sizePolicy().hasHeightForWidth())
        self.LE_montant.setSizePolicy(sizePolicy)
        self.LE_montant.setMinimumSize(QtCore.QSize(200, 20))
        self.LE_montant.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.LE_montant.setFont(font)
        self.LE_montant.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.LE_montant.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LE_montant.setReadOnly(False)
        self.LE_montant.setObjectName("LE_montant")
        self.gridLayout.addWidget(self.LE_montant, 1, 1, 1, 1)
        self.l_vide = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_vide.sizePolicy().hasHeightForWidth())
        self.l_vide.setSizePolicy(sizePolicy)
        self.l_vide.setMinimumSize(QtCore.QSize(130, 20))
        self.l_vide.setMaximumSize(QtCore.QSize(130, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_vide.setFont(font)
        self.l_vide.setStyleSheet("color: rgb(240, 240, 240);")
        self.l_vide.setText("")
        self.l_vide.setObjectName("l_vide")
        self.gridLayout.addWidget(self.l_vide, 2, 0, 1, 1)
        self.B_fermer_la_fenetre = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.B_fermer_la_fenetre.sizePolicy().hasHeightForWidth())
        self.B_fermer_la_fenetre.setSizePolicy(sizePolicy)
        self.B_fermer_la_fenetre.setMinimumSize(QtCore.QSize(120, 40))
        self.B_fermer_la_fenetre.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.B_fermer_la_fenetre.setFont(font)
        self.B_fermer_la_fenetre.setObjectName("B_fermer_la_fenetre")
        self.gridLayout.addWidget(self.B_fermer_la_fenetre, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.LE_libelle, self.LE_montant)
        MainWindow.setTabOrder(self.LE_montant, self.B_ajouter)
        MainWindow.setTabOrder(self.B_ajouter, self.B_fermer_la_fenetre)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ajout de lignes"))
        self.l_libelle.setText(_translate("MainWindow", "Libellé"))
        self.B_ajouter.setText(_translate("MainWindow", "Ajouter"))
        self.l_montant.setText(_translate("MainWindow", "Montant (en €)"))
        self.B_fermer_la_fenetre.setText(_translate("MainWindow", "Fermer la fenêtre"))
