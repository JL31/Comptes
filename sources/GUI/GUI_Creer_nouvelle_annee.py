# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Creer_nouvelle_annee.ui'
#
# Created: Wed Feb 13 14:22:54 2019
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(430, 235)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(430, 235))
        Dialog.setMaximumSize(QtCore.QSize(430, 235))
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
        Dialog.setPalette(palette)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.l_vide = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_vide.sizePolicy().hasHeightForWidth())
        self.l_vide.setSizePolicy(sizePolicy)
        self.l_vide.setMinimumSize(QtCore.QSize(250, 10))
        self.l_vide.setMaximumSize(QtCore.QSize(250, 10))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_vide.setFont(font)
        self.l_vide.setStyleSheet(_fromUtf8("color: rgb(240, 240, 240);"))
        self.l_vide.setText(_fromUtf8(""))
        self.l_vide.setObjectName(_fromUtf8("l_vide"))
        self.gridLayout.addWidget(self.l_vide, 4, 0, 1, 2)
        self.CB_mois = QtGui.QComboBox(Dialog)
        self.CB_mois.setMinimumSize(QtCore.QSize(140, 30))
        self.CB_mois.setMaximumSize(QtCore.QSize(140, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 90, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 90, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 90, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.CB_mois.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.CB_mois.setFont(font)
        self.CB_mois.setObjectName(_fromUtf8("CB_mois"))
        self.gridLayout.addWidget(self.CB_mois, 2, 1, 1, 1)
        self.l_mois = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_mois.sizePolicy().hasHeightForWidth())
        self.l_mois.setSizePolicy(sizePolicy)
        self.l_mois.setMinimumSize(QtCore.QSize(250, 50))
        self.l_mois.setMaximumSize(QtCore.QSize(250, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.l_mois.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.l_mois.setFont(font)
        self.l_mois.setStyleSheet(_fromUtf8(""))
        self.l_mois.setObjectName(_fromUtf8("l_mois"))
        self.gridLayout.addWidget(self.l_mois, 2, 0, 1, 1)
        self.B_creer = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.B_creer.sizePolicy().hasHeightForWidth())
        self.B_creer.setSizePolicy(sizePolicy)
        self.B_creer.setMinimumSize(QtCore.QSize(140, 40))
        self.B_creer.setMaximumSize(QtCore.QSize(140, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.B_creer.setFont(font)
        self.B_creer.setObjectName(_fromUtf8("B_creer"))
        self.gridLayout.addWidget(self.B_creer, 5, 1, 1, 1)
        self.l_choix = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_choix.sizePolicy().hasHeightForWidth())
        self.l_choix.setSizePolicy(sizePolicy)
        self.l_choix.setMinimumSize(QtCore.QSize(250, 80))
        self.l_choix.setMaximumSize(QtCore.QSize(250, 80))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.l_choix.setFont(font)
        self.l_choix.setStyleSheet(_fromUtf8("color: rgb(240, 240, 240);"))
        self.l_choix.setObjectName(_fromUtf8("l_choix"))
        self.gridLayout.addWidget(self.l_choix, 0, 0, 1, 1)
        self.B_choix = QtGui.QPushButton(Dialog)
        self.B_choix.setMinimumSize(QtCore.QSize(140, 80))
        self.B_choix.setMaximumSize(QtCore.QSize(140, 80))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.B_choix.setFont(font)
        self.B_choix.setCheckable(False)
        self.B_choix.setFlat(False)
        self.B_choix.setObjectName(_fromUtf8("B_choix"))
        self.gridLayout.addWidget(self.B_choix, 0, 1, 1, 1)
        self.l_vide_2 = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_vide_2.sizePolicy().hasHeightForWidth())
        self.l_vide_2.setSizePolicy(sizePolicy)
        self.l_vide_2.setMinimumSize(QtCore.QSize(250, 10))
        self.l_vide_2.setMaximumSize(QtCore.QSize(250, 10))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_vide_2.setFont(font)
        self.l_vide_2.setStyleSheet(_fromUtf8("color: rgb(240, 240, 240);"))
        self.l_vide_2.setText(_fromUtf8(""))
        self.l_vide_2.setObjectName(_fromUtf8("l_vide_2"))
        self.gridLayout.addWidget(self.l_vide_2, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Créer une nouvelle année", None))
        self.l_mois.setText(_translate("Dialog", "<html><head/><body><p>Sélectionnez le mois qui </p><p>contient les données à utiliser</p></body></html>", None))
        self.B_creer.setText(_translate("Dialog", "Créer", None))
        self.l_choix.setText(_translate("Dialog", "<html><head/><body><p>Utiliser des données de l\'année</p><p>en cours pour le mois de janvier</p><p>de l\'année suivante</p></body></html>", None))
        self.B_choix.setText(_translate("Dialog", "NON", None))

