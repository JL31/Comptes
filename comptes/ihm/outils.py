# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'outils.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1092, 800)
        Dialog.setWindowTitle("")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.B_Nouvelle_annee = QtWidgets.QPushButton(Dialog)
        self.B_Nouvelle_annee.setMinimumSize(QtCore.QSize(90, 90))
        self.B_Nouvelle_annee.setMaximumSize(QtCore.QSize(90, 90))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.B_Nouvelle_annee.setFont(font)
        self.B_Nouvelle_annee.setObjectName("B_Nouvelle_annee")
        self.gridLayout.addWidget(self.B_Nouvelle_annee, 5, 0, 1, 1)
        self.B_Enregistrer = QtWidgets.QPushButton(Dialog)
        self.B_Enregistrer.setMinimumSize(QtCore.QSize(90, 90))
        self.B_Enregistrer.setMaximumSize(QtCore.QSize(90, 90))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.B_Enregistrer.setFont(font)
        self.B_Enregistrer.setObjectName("B_Enregistrer")
        self.gridLayout.addWidget(self.B_Enregistrer, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 1, 1, 1)
        self.B_Copie_mail = QtWidgets.QPushButton(Dialog)
        self.B_Copie_mail.setMinimumSize(QtCore.QSize(90, 90))
        self.B_Copie_mail.setMaximumSize(QtCore.QSize(90, 90))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.B_Copie_mail.setFont(font)
        self.B_Copie_mail.setObjectName("B_Copie_mail")
        self.gridLayout.addWidget(self.B_Copie_mail, 2, 0, 1, 1)
        self.B_Quitter = QtWidgets.QPushButton(Dialog)
        self.B_Quitter.setMinimumSize(QtCore.QSize(90, 90))
        self.B_Quitter.setMaximumSize(QtCore.QSize(90, 90))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.B_Quitter.setFont(font)
        self.B_Quitter.setObjectName("B_Quitter")
        self.gridLayout.addWidget(self.B_Quitter, 7, 0, 1, 1)
        self.B_Copie_back_up = QtWidgets.QPushButton(Dialog)
        self.B_Copie_back_up.setMinimumSize(QtCore.QSize(90, 90))
        self.B_Copie_back_up.setMaximumSize(QtCore.QSize(90, 90))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.B_Copie_back_up.setFont(font)
        self.B_Copie_back_up.setObjectName("B_Copie_back_up")
        self.gridLayout.addWidget(self.B_Copie_back_up, 3, 0, 1, 1)
        self.B_Dupliquer_mois = QtWidgets.QPushButton(Dialog)
        self.B_Dupliquer_mois.setMinimumSize(QtCore.QSize(90, 90))
        self.B_Dupliquer_mois.setMaximumSize(QtCore.QSize(90, 90))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.B_Dupliquer_mois.setFont(font)
        self.B_Dupliquer_mois.setStyleSheet("")
        self.B_Dupliquer_mois.setObjectName("B_Dupliquer_mois")
        self.gridLayout.addWidget(self.B_Dupliquer_mois, 6, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 8, 0, 1, 1)
        self.B_Importer_donnees = QtWidgets.QPushButton(Dialog)
        self.B_Importer_donnees.setMinimumSize(QtCore.QSize(90, 90))
        self.B_Importer_donnees.setMaximumSize(QtCore.QSize(90, 90))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.B_Importer_donnees.setFont(font)
        self.B_Importer_donnees.setObjectName("B_Importer_donnees")
        self.gridLayout.addWidget(self.B_Importer_donnees, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setMouseTracking(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
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
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Permet de créer une copie du fichier contenant les données dans le dossier de sauvegarde spécifié dans le fichier de configuration (Configuration.json).</span></p><p><span style=\" font-size:10pt;\">Ce fichier portera le même nom que le fichier de données plus la date et l\'heure de l\'enregistrement.</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Permet d\'envoyer une copie du fichier contenant les données vers la boîte mail spécifié dans le fichier de configuration (Configuration.json)</span></p></body></html>"))
        self.B_Nouvelle_annee.setText(_translate("Dialog", "Créer une\n"
"nouvelle\n"
"année"))
        self.B_Enregistrer.setText(_translate("Dialog", "Enregistrer"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Permet de quitter l\'application.</span></p></body></html>"))
        self.B_Copie_mail.setText(_translate("Dialog", "Envoyer\n"
"une copie\n"
"par mail"))
        self.B_Quitter.setText(_translate("Dialog", "Quitter"))
        self.B_Copie_back_up.setText(_translate("Dialog", "Créer\n"
"une copie\n"
"back up"))
        self.B_Dupliquer_mois.setText(_translate("Dialog", "Dupliquer\n"
"un mois"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Permet d\'enregistrer les données dans le dossier spécifié dans le fichier de configuration (Configuration.json)</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Permet de dupliquer les données des prélèvements et des épargnes d\'un mois vers un autre mois.</span></p></body></html>"))
        self.B_Importer_donnees.setText(_translate("Dialog", "Importer\n"
"des données"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Permet d\'importer des données en provenance de l\'application des comptes.</span></p><p><span style=\" font-size:10pt;\">Ces données seront insérées dans la catégorie dépenses du mois sélectionné.</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Permet de créer un fichier de donnée pour l\'année suivante.</span></p><p><span style=\" font-size:10pt;\">Il est possible de choisir de dupliquer les données des prélèvements et des épargnes du mois de décembre de l\'année actuelle pour le mois de janvier de l\'année suivante.</span></p></body></html>"))