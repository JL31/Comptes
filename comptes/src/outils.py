# coding: utf-8

""" Module qui contient la classe Outils pour Y """

# =================================================================================================
# Paramètres globaux
# =================================================================================================

__author__ = "Julien LEPAIN"
__version__ = 1.0
__all__ = ["Outils"]

# =================================================================================================
# Import des librairies
# =================================================================================================

from PyQt5 import QtGui, QtCore, QtWidgets
import ihm.outils as GUI_Outils
import sys


# =================================================================================================
# Classes
# =================================================================================================


class Outils(QtWidgets.QDialog, GUI_Outils.Ui_Dialog):
    """
    Classe de lien entre la Vue et le Modèle
    """

    def __init__(self, instance_fenetre_principale, parent=None):
        """
        Constructeur de la classe
        """

        super(Outils, self).__init__(parent)
        self.setupUi(self)

        self._instance_fenetre_principale = instance_fenetre_principale

        self._dico_des_methodes = {
            "enregistrement": self._instance_fenetre_principale.enregistrement_des_donnees,
            "copie_par_mail": self._instance_fenetre_principale.envoi_d_une_copie_des_donnees_par_mail,
            "copie_back_up": self._instance_fenetre_principale.creation_d_une_copie_back_up,
            "importer_des_donnees": self._instance_fenetre_principale.importer_des_donnees,
            "creer_nouvelle_annee": self._instance_fenetre_principale.creation_d_une_nouvelle_annee,
            "dupliquer_mois": self._instance_fenetre_principale.duplication_des_donnees_d_un_mois,
            "fermeture_application": self._instance_fenetre_principale.fermeture_application
        }

        self.options_de_la_fenetre()
        self.centrage_de_la_fenetre()
        self.connexion_des_widgets()

    def options_de_la_fenetre(self):
        """
        Méthode qui permet de configurer certaines options pour la fenêtre
        """

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

    def centrage_de_la_fenetre(self):
        """
        Méthode qui permet de centrer la fenêtre sur l'écran
        """

        # Récupération de la géométrie de la fenêtre dans un objet : QRect avec X, Y, largeur, hauteur
        qr = self.frameGeometry()
        print(qr)

        # Récupération de la position (X, Y) du centre de l'écran
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        print(cp)

        # Déplacement du centre de l'objet réprésentant la géométrie de la fenêtre au centre de l'écran
        qr.moveCenter(cp)

        # Déplacement de la fenêtre : on récupéère les coordonnées du coin haut gauche de l'objet représentant la
        # fenêtre et on déplace la fenêtre à cet emplacement
        # Pour rappel lorsqu'on déplace un widget avec la méthode move on modifie les coordonnées de son coin haut
        # gauche
        self.move(qr.topLeft())

    def appel_de_la_methode(self, option):
        """
        Méthode qui permet d'appeler la méthode adéquate à l'action sélectionnée
        Cette méthode va fermer la fenêtre des outils une fois l'action précédente réalisée
        """

        self._dico_des_methodes[option]()

        self.accept()

    def connexion_des_widgets(self):
        """
        Méthode qui permet de connecter les widgets
        """

        self.B_Enregistrer.clicked.connect(lambda: self.appel_de_la_methode("enregistrement"))
        self.B_Copie_mail.clicked.connect(lambda: self.appel_de_la_methode("copie_par_mail"))
        self.B_Copie_back_up.clicked.connect(lambda: self.appel_de_la_methode("copie_back_up"))
        self.B_Importer_donnees.clicked.connect(lambda: self.appel_de_la_methode("importer_des_donnees"))
        self.B_Nouvelle_annee.clicked.connect(lambda: self.appel_de_la_methode("creer_nouvelle_annee"))
        self.B_Dupliquer_mois.clicked.connect(lambda: self.appel_de_la_methode("dupliquer_mois"))
        self.B_Quitter.clicked.connect(lambda: self.appel_de_la_methode("fermeture_application"))
