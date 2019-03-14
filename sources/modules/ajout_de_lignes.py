# coding: utf-8

""" Module qui contient la classe AjoutDeLignes pour Y """


# =================================================================================================
# Paramètres globaux
# =================================================================================================

__author__ = "Julien LEPAIN"
__version__ = 1.0
__all__ = ["AjoutDeLignes"]


# =================================================================================================
# Import des librairies
# =================================================================================================

from PyQt4 import QtGui, QtCore
import GUI_Ajout_de_lignes as GUI_Ajout_de_lignes
import sous_classement_des_qvalidators as sous_classement_des_qvalidators


# =================================================================================================
# Classes
# =================================================================================================

# ========================================================================
class AjoutDeLignes(QtGui.QMainWindow, GUI_Ajout_de_lignes.Ui_MainWindow):
    """
        Classe qui permet d'ouvrir une fenêtre afin d'insérer des lignes dans le TV affichage de la catégorie sélectionnée
    """

    # Signal lié aux éléments à insérer : attribut _elements
    elements_a_inserer = QtCore.pyqtSignal(str)

    # =========================================
    def __init__(self, categorie, parent=None):
        """
            Constructeur de la classe

            :param categorie : catégorie (ici prelevements ou epargnes)
            :ivar categorie: str

            :param parent: parent de la fenêtre actuelle
            :ivar parent: None

            :param _categorie: [attribut privé] catégorie (ici prelevements ou epargnes)
            :ivar _categorie: str
        """
        
        super(AjoutDeLignes, self).__init__(parent)
        self.setupUi(self)
        
        self._categorie = categorie
        
        self.options_de_la_fenetre()
        self.connexion_des_widgets()

    # ==============================
    def options_de_la_fenetre(self):
        """
            Méthode qui permet de configurer certaines options pour la fenêtre
        """

        # Mise en place des QValidators
        validateur = sous_classement_des_qvalidators.SCQDoubleValidation(-5000.0, 5000.0)
        validateur.setDecimals(3)
        self.LE_montant.setValidator(validateur)

    # ==========================
    def ajouter_une_ligne(self):
        """
            Méthode qui permet d'ajouter une ligne dans le TV affichage, dans la catégorie sélectionnée,
            en récupérant les informations renseignées par l'utilisateur dans la GUI
        """

        # Nettoyage de la chaîne de carcatères qui va contenir les éléments à envoyer
        self._elements = ""

        # Remplissage de la chaîne de caractères avec les éléments à envoyer
        self._elements = "{}\t{}".format(str(self.LE_libelle.text()), str(self.LE_montant.text()))

        # Emission du signal contenant les éléments à insérer
        self.elements_a_inserer.emit(self._elements)

        # Nettoyage des QLineEdit
        self.LE_libelle.clear()
        self.LE_montant.clear()

    # ================================
    def fermeture_de_la_fenetre(self):
        """
            Méthode qui permet de fermer la fenêtre d'insertion des données
        """
        
        self.hide()

    # ==============================
    def connexion_des_widgets(self):
        """
            Méthode qui permet de connecter les widgets
        """
        
        self.B_ajouter.clicked.connect(self.ajouter_une_ligne)
        self.B_fermer_la_fenetre.clicked.connect(self.fermeture_de_la_fenetre)

    # =============
    def main(self):
        """
            Main de la classe
        """
        
        self.show()


# =================================================================================================
# Utilisation
# =================================================================================================

if __name__ == "__main__":
    
    print("Ce module n'est pas voué à être exécuté seul")
