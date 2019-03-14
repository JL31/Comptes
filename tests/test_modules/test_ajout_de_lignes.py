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

        self.categorie = "depenses"
        self.parent = None

        self.valeur_du_retour = ""

        self.app = QtGui.QApplication(sys.argv)

    # ==================
    def test_init(self):
        """
            Méthode de test du constructeur
        """

        instance = AjoutDeLignes(self.categorie)

        test = instance.__dict__["_categorie"]
        msg = "La catégorie n'est pas la bonne"
        self.assertEqual(test, "depenses", msg=msg)

    # ===================================
    def test_options_de_la_fenetre(self):
        """
            Méthode de test de la méthode qui permet de configurer certaines options pour la fenêtre
        """

        instance = AjoutDeLignes.__new__(AjoutDeLignes)
        super(AjoutDeLignes, instance).__init__(self.parent)
        instance.setupUi(instance)
        instance.__dict__["_categorie"] = self.categorie

        instance.options_de_la_fenetre()

        test = instance.LE_montant.validator()
        msg = "Le QValidator associé au QWidget 'LE_montant' n'est pas correct : 'sous_classement_des_qvalidators.SCQDoubleValidation' attendu"
        self.assertIsInstance(test, sous_classement_des_qvalidators.SCQDoubleValidation, msg=msg)

    # =======================
    @QtCore.pyqtSlot(str)
    def retour(self, valeur):

        self.valeur_du_retour = valeur

    # ===============================
    def test_ajouter_une_ligne(self):
        """
            Méthode de test de la méthode permet d'ajouter une ligne dans le TV affichage, dans la catégorie sélectionnée,
            en récupérant les informations renseignées par l'utilisateur dans la GUI
        """

        instance = AjoutDeLignes(self.categorie)

        instance.LE_libelle.setText("essai")
        instance.LE_montant.setText("10.0")

        instance.elements_a_inserer.connect(self.retour)

        instance.ajouter_une_ligne()

        test_1 = instance.__dict__["_elements"]
        msg = "L'élément à insérer n'est pas correct : essai\t10.0 attendu"
        self.assertEqual(test_1, "essai\t10.0", msg=msg)

        msg = "L'élément à insérer, récupéré du signal émis (signal 'elements_a_inserer'), n'est pas correct : essai\t10.0 attendu"
        self.assertEqual(self.valeur_du_retour, "essai\t10.0", msg=msg)

# "trucs" de test interne Qt

# =================================================================================================
# Fonctions
# =================================================================================================

# =================================================================================================
# Utilisation
# =================================================================================================
