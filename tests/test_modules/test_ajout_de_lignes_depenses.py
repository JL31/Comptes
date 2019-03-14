# coding: utf-8

""" Module qui xxx """

# =================================================================================================
# Paramètres globaux
# =================================================================================================

__author__ = "Julien LEPAIN"
__version__ = 1.0


# =================================================================================================
# Import des librairies
# =================================================================================================

from unittest import TestCase

from PyQt4 import QtGui, QtCore
import sys
from ajout_de_lignes import AjoutDeLignes, sous_classement_des_qvalidators

# =================================================================================================
# Classes
# =================================================================================================


# ================================
class TestAjoutDeLignes(TestCase):
    """
        Classe de test du modules d'ajout de lignes
    """

    # ==============
    def setUp(self):
        """
            Méthode setUp
        """

        pass

    # ==================
    def test_init(self):
        """
            Méthode de test du constructeur
        """

        on peut tester les QValidator des QLineEdit LE_date et LE_montant

    # ===================================
    def test_options_de_la_fenetre(self):
        """
            Méthode de test de la méthode qui permet de configurer certaines options pour la fenêtre
        """

        on peut tester les QValidator des QLineEdit LE_date et LE_montant

    # ====================================================
    def test_gestion_affichage_LE_moyen_de_paiement(self):
        """
            Méthode de test de la méthode qui permet de gérer l'affichage du QLineEdit LE_moyen_de_paiement
            selon la valeur choisie dans le QComboBox CB_moyen_de_paiement
        """

        pass

    # =======================
    @QtCore.pyqtSlot(str)
    def retour(self, valeur):

        pass

    # ===============================
    def test_ajouter_une_ligne(self):
        """
            Méthode de test de la méthode permet d'ajouter une ligne dans le TV affichage, dans la catégorie sélectionnée,
            en récupérant les informations renseignées par l'utilisateur dans la GUI
        """

        pass

# =================================================================================================
# Fonctions
# =================================================================================================

# =================================================================================================
# Utilisation
# =================================================================================================
