# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Ajout_de_lignes_depenses.ui'
#
# Created: Tue Feb 12 14:13:48 2019
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(490, 210)
        MainWindow.setMinimumSize(QtCore.QSize(490, 210))
        MainWindow.setMaximumSize(QtCore.QSize(490, 210))
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
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.l_date = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_date.sizePolicy().hasHeightForWidth())
        self.l_date.setSizePolicy(sizePolicy)
        self.l_date.setMinimumSize(QtCore.QSize(170, 20))
        self.l_date.setMaximumSize(QtCore.QSize(170, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_date.setFont(font)
        self.l_date.setStyleSheet(_fromUtf8("color: rgb(240, 240, 240);"))
        self.l_date.setObjectName(_fromUtf8("l_date"))
        self.gridLayout.addWidget(self.l_date, 0, 0, 1, 1)
        self.LE_date = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LE_date.sizePolicy().hasHeightForWidth())
        self.LE_date.setSizePolicy(sizePolicy)
        self.LE_date.setMinimumSize(QtCore.QSize(200, 20))
        self.LE_date.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.LE_date.setFont(font)
        self.LE_date.setStyleSheet(_fromUtf8("background-color: rgb(240, 240, 240);"))
        self.LE_date.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LE_date.setReadOnly(False)
        self.LE_date.setObjectName(_fromUtf8("LE_date"))
        self.gridLayout.addWidget(self.LE_date, 0, 1, 1, 1)
        self.B_ajouter = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.B_ajouter.sizePolicy().hasHeightForWidth())
        self.B_ajouter.setSizePolicy(sizePolicy)
        self.B_ajouter.setMinimumSize(QtCore.QSize(80, 110))
        self.B_ajouter.setMaximumSize(QtCore.QSize(80, 110))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.B_ajouter.setFont(font)
        self.B_ajouter.setObjectName(_fromUtf8("B_ajouter"))
        self.gridLayout.addWidget(self.B_ajouter, 0, 2, 4, 1)
        self.l_libelle = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_libelle.sizePolicy().hasHeightForWidth())
        self.l_libelle.setSizePolicy(sizePolicy)
        self.l_libelle.setMinimumSize(QtCore.QSize(170, 20))
        self.l_libelle.setMaximumSize(QtCore.QSize(170, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_libelle.setFont(font)
        self.l_libelle.setStyleSheet(_fromUtf8("color: rgb(240, 240, 240);"))
        self.l_libelle.setObjectName(_fromUtf8("l_libelle"))
        self.gridLayout.addWidget(self.l_libelle, 1, 0, 1, 1)
        self.LE_libelle = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
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
        self.LE_libelle.setStyleSheet(_fromUtf8("background-color: rgb(240, 240, 240);"))
        self.LE_libelle.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LE_libelle.setReadOnly(False)
        self.LE_libelle.setObjectName(_fromUtf8("LE_libelle"))
        self.gridLayout.addWidget(self.LE_libelle, 1, 1, 1, 1)
        self.l_montant = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_montant.sizePolicy().hasHeightForWidth())
        self.l_montant.setSizePolicy(sizePolicy)
        self.l_montant.setMinimumSize(QtCore.QSize(170, 20))
        self.l_montant.setMaximumSize(QtCore.QSize(130, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_montant.setFont(font)
        self.l_montant.setStyleSheet(_fromUtf8("color: rgb(240, 240, 240);"))
        self.l_montant.setObjectName(_fromUtf8("l_montant"))
        self.gridLayout.addWidget(self.l_montant, 2, 0, 1, 1)
        self.LE_montant = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
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
        self.LE_montant.setStyleSheet(_fromUtf8("background-color: rgb(240, 240, 240);"))
        self.LE_montant.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LE_montant.setReadOnly(False)
        self.LE_montant.setObjectName(_fromUtf8("LE_montant"))
        self.gridLayout.addWidget(self.LE_montant, 2, 1, 1, 1)
        self.l_moyen_de_paiement = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_moyen_de_paiement.sizePolicy().hasHeightForWidth())
        self.l_moyen_de_paiement.setSizePolicy(sizePolicy)
        self.l_moyen_de_paiement.setMinimumSize(QtCore.QSize(170, 20))
        self.l_moyen_de_paiement.setMaximumSize(QtCore.QSize(170, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_moyen_de_paiement.setFont(font)
        self.l_moyen_de_paiement.setStyleSheet(_fromUtf8("color: rgb(240, 240, 240);"))
        self.l_moyen_de_paiement.setObjectName(_fromUtf8("l_moyen_de_paiement"))
        self.gridLayout.addWidget(self.l_moyen_de_paiement, 3, 0, 1, 1)
        self.CB_moyen_de_paiement = QtGui.QComboBox(self.centralwidget)
        self.CB_moyen_de_paiement.setMinimumSize(QtCore.QSize(200, 0))
        self.CB_moyen_de_paiement.setMaximumSize(QtCore.QSize(200, 16777215))
        self.CB_moyen_de_paiement.setObjectName(_fromUtf8("CB_moyen_de_paiement"))
        self.CB_moyen_de_paiement.addItem(_fromUtf8(""))
        self.CB_moyen_de_paiement.addItem(_fromUtf8(""))
        self.CB_moyen_de_paiement.addItem(_fromUtf8(""))
        self.CB_moyen_de_paiement.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.CB_moyen_de_paiement, 3, 1, 1, 1)
        self.l_vide = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_vide.sizePolicy().hasHeightForWidth())
        self.l_vide.setSizePolicy(sizePolicy)
        self.l_vide.setMinimumSize(QtCore.QSize(170, 20))
        self.l_vide.setMaximumSize(QtCore.QSize(170, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_vide.setFont(font)
        self.l_vide.setStyleSheet(_fromUtf8("color: rgb(240, 240, 240);"))
        self.l_vide.setText(_fromUtf8(""))
        self.l_vide.setObjectName(_fromUtf8("l_vide"))
        self.gridLayout.addWidget(self.l_vide, 4, 0, 1, 1)
        self.B_fermer_la_fenetre = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.B_fermer_la_fenetre.sizePolicy().hasHeightForWidth())
        self.B_fermer_la_fenetre.setSizePolicy(sizePolicy)
        self.B_fermer_la_fenetre.setMinimumSize(QtCore.QSize(120, 40))
        self.B_fermer_la_fenetre.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.B_fermer_la_fenetre.setFont(font)
        self.B_fermer_la_fenetre.setObjectName(_fromUtf8("B_fermer_la_fenetre"))
        self.gridLayout.addWidget(self.B_fermer_la_fenetre, 5, 0, 1, 1)
        self.LE_moyen_de_paiement = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LE_moyen_de_paiement.sizePolicy().hasHeightForWidth())
        self.LE_moyen_de_paiement.setSizePolicy(sizePolicy)
        self.LE_moyen_de_paiement.setMinimumSize(QtCore.QSize(200, 20))
        self.LE_moyen_de_paiement.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.LE_moyen_de_paiement.setFont(font)
        self.LE_moyen_de_paiement.setStyleSheet(_fromUtf8("background-color: rgb(240, 240, 240);"))
        self.LE_moyen_de_paiement.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LE_moyen_de_paiement.setReadOnly(False)
        self.LE_moyen_de_paiement.setObjectName(_fromUtf8("LE_moyen_de_paiement"))
        self.gridLayout.addWidget(self.LE_moyen_de_paiement, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.LE_date, self.LE_libelle)
        MainWindow.setTabOrder(self.LE_libelle, self.LE_montant)
        MainWindow.setTabOrder(self.LE_montant, self.CB_moyen_de_paiement)
        MainWindow.setTabOrder(self.CB_moyen_de_paiement, self.B_ajouter)
        MainWindow.setTabOrder(self.B_ajouter, self.B_fermer_la_fenetre)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Ajout de lignes", None))
        self.l_date.setText(_translate("MainWindow", "Date", None))
        self.B_ajouter.setText(_translate("MainWindow", "Ajouter", None))
        self.l_libelle.setText(_translate("MainWindow", "Libellé", None))
        self.l_montant.setText(_translate("MainWindow", "Montant (en €)", None))
        self.l_moyen_de_paiement.setText(_translate("MainWindow", "Moyen de paiement", None))
        self.CB_moyen_de_paiement.setItemText(0, _translate("MainWindow", "CB", None))
        self.CB_moyen_de_paiement.setItemText(1, _translate("MainWindow", "chèque", None))
        self.CB_moyen_de_paiement.setItemText(2, _translate("MainWindow", "virement bancaire", None))
        self.CB_moyen_de_paiement.setItemText(3, _translate("MainWindow", "elle", None))
        self.B_fermer_la_fenetre.setText(_translate("MainWindow", "Fermer la fenêtre", None))
