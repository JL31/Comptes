﻿"""
    Module qui contient la classe FenetreIntermediairePourLesOutils pour Y
"""


# =================================================================================================
# Paramètres globaux
# =================================================================================================

__all__ = ["FenetreIntermediairePourLesOutils"]


# =================================================================================================
# Import des librairies
# =================================================================================================

from PyQt5 import QtWidgets
import ihm.fenetre_intermediaire_pour_les_outils as GUI_FenetreIntermediairePourLesOutils
from src.outils import Outils


# =================================================================================================
# Classes
# =================================================================================================

class FenetreIntermediairePourLesOutils(QtWidgets.QDialog, GUI_FenetreIntermediairePourLesOutils.Ui_Dialog):
    """
    Classe de qui permet de créer une fenêtre intermédiaire pour les outils
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        """
        
        super(FenetreIntermediairePourLesOutils, self).__init__(parent)
        self.setupUi(self)

        self._instance_fenetre_principale = parent

        self._outils = None
        self._output_outils = None

    def exec_(self):
        """
        Surcharge de la méthode
        """

        self.options_de_la_fenetre()
        self.appel_des_outils()

    def options_de_la_fenetre(self):
        """
        Méthode qui permet de configurer certaines options pour la fenêtre
        """

        # Permet d'afficher la fenêtre en plein écran
        self.showFullScreen()

    def appel_des_outils(self):
        """
        Méthode qui permet de lancer la fenêtre qui contient les outils
        """

        # Création d'une instance de la classe Outils
        self._outils = Outils(self._instance_fenetre_principale, parent=self)

        # Lancement de l'instance
        self._outils.exec_()

        self.accept()
