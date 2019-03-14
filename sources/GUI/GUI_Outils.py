# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Outils.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        Dialog.resize(1092, 800)
        Dialog.setWindowTitle(_fromUtf8(""))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.B_Nouvelle_annee = QtGui.QPushButton(Dialog)
        self.B_Nouvelle_annee.setMinimumSize(QtCore.QSize(90, 90))
        self.B_Nouvelle_annee.setMaximumSize(QtCore.QSize(90, 90))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.B_Nouvelle_annee.setFont(font)
        self.B_Nouvelle_annee.setObjectName(_fromUtf8("B_Nouvelle_annee"))
        self.gridLayout.addWidget(self.B_Nouvelle_annee, 5, 0, 1, 1)
        self.B_Enregistrer = QtGui.QPushButton(Dialog)
        self.B_Enregistrer.setMinimumSize(QtCore.QSize(90, 90))
        self.B_Enregistrer.setMaximumSize(QtCore.QSize(90, 90))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.B_Enregistrer.setFont(font)
        self.B_Enregistrer.setObjectName(_fromUtf8("B_Enregistrer"))
        self.gridLayout.addWidget(self.B_Enregistrer, 1, 0, 1, 1)
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 7, 1, 1, 1)
        self.B_Copie_mail = QtGui.QPushButton(Dialog)
        self.B_Copie_mail.setMinimumSize(QtCore.QSize(90, 90))
        self.B_Copie_mail.setMaximumSize(QtCore.QSize(90, 90))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.B_Copie_mail.setFont(font)
        self.B_Copie_mail.setObjectName(_fromUtf8("B_Copie_mail"))
        self.gridLayout.addWidget(self.B_Copie_mail, 2, 0, 1, 1)
        self.B_Quitter = QtGui.QPushButton(Dialog)
        self.B_Quitter.setMinimumSize(QtCore.QSize(90, 90))
        self.B_Quitter.setMaximumSize(QtCore.QSize(90, 90))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.B_Quitter.setFont(font)
        self.B_Quitter.setObjectName(_fromUtf8("B_Quitter"))
        self.gridLayout.addWidget(self.B_Quitter, 7, 0, 1, 1)
        self.B_Copie_back_up = QtGui.QPushButton(Dialog)
        self.B_Copie_back_up.setMinimumSize(QtCore.QSize(90, 90))
        self.B_Copie_back_up.setMaximumSize(QtCore.QSize(90, 90))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.B_Copie_back_up.setFont(font)
        self.B_Copie_back_up.setObjectName(_fromUtf8("B_Copie_back_up"))
        self.gridLayout.addWidget(self.B_Copie_back_up, 3, 0, 1, 1)
        self.B_Dupliquer_mois = QtGui.QPushButton(Dialog)
        self.B_Dupliquer_mois.setMinimumSize(QtCore.QSize(90, 90))
        self.B_Dupliquer_mois.setMaximumSize(QtCore.QSize(90, 90))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.B_Dupliquer_mois.setFont(font)
        self.B_Dupliquer_mois.setStyleSheet(_fromUtf8(""))
        self.B_Dupliquer_mois.setObjectName(_fromUtf8("B_Dupliquer_mois"))
        self.gridLayout.addWidget(self.B_Dupliquer_mois, 6, 0, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 6, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 8, 0, 1, 1)
        self.B_Importer_donnees = QtGui.QPushButton(Dialog)
        self.B_Importer_donnees.setMinimumSize(QtCore.QSize(90, 90))
        self.B_Importer_donnees.setMaximumSize(QtCore.QSize(90, 90))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.B_Importer_donnees.setFont(font)
        self.B_Importer_donnees.setObjectName(_fromUtf8("B_Importer_donnees"))
        self.gridLayout.addWidget(self.B_Importer_donnees, 4, 0, 1, 1)
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setMouseTracking(True)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 4, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 5, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.B_Enregistrer, self.B_Copie_mail)
        Dialog.setTabOrder(self.B_Copie_mail, self.B_Copie_back_up)
        Dialog.setTabOrder(self.B_Copie_back_up, self.B_Importer_donnees)
        Dialog.setTabOrder(self.B_Importer_donnees, self.B_Nouvelle_annee)
        Dialog.setTabOrder(self.B_Nouvelle_annee, self.B_Dupliquer_mois)
        Dialog.setTabOrder(self.B_Dupliquer_mois, self.B_Quitter)

    def retranslateUi(self, Dialog):
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Permet de créer une copie du fichier contenant les données dans le dossier de sauvegarde spécifié dans le fichier de configuration (Configuration.json).</span></p><p><span style=\" font-size:10pt;\">Ce fichier portera le même nom que le fichier de données plus la date et l\'heure de l\'enregistrement.</span></p></body></html>", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Permet d\'envoyer une copie du fichier contenant les données vers la boîte mail spécifié dans le fichier de configuration (Configuration.json)</span></p></body></html>", None))
        self.B_Nouvelle_annee.setText(_translate("Dialog", "Créer une\n"
"nouvelle\n"
"année", None))
        self.B_Enregistrer.setText(_translate("Dialog", "Enregistrer", None))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Permet de quitter l\'application.</span></p></body></html>", None))
        self.B_Copie_mail.setText(_translate("Dialog", "Envoyer\n"
"une copie\n"
"par mail", None))
        self.B_Quitter.setText(_translate("Dialog", "Quitter", None))
        self.B_Copie_back_up.setText(_translate("Dialog", "Créer\n"
"une copie\n"
"back up", None))
        self.B_Dupliquer_mois.setText(_translate("Dialog", "Dupliquer\n"
"un mois", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Permet d\'enregistrer les données dans le dossier spécifié dans le fichier de configuration (Configuration.json)</span></p></body></html>", None))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Permet de dupliquer les données des prélèvements et des épargnes d\'un mois vers un autre mois.</span></p></body></html>", None))
        self.B_Importer_donnees.setText(_translate("Dialog", "Importer\n"
"des données", None))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Permet d\'importer des données en provenance de l\'application des comptes.</span></p><p><span style=\" font-size:10pt;\">Ces données seront insérées dans la catégorie dépenses du mois sélectionné.</span></p></body></html>", None))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Permet de créer un fichier de donnée pour l\'année suivante.</span></p><p><span style=\" font-size:10pt;\">Il est possible de choisir de dupliquer les données des prélèvements et des épargnes du mois de décembre de l\'année actuelle pour le mois de janvier de l\'année suivante.</span></p></body></html>", None))

