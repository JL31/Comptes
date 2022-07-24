# coding: utf-8

""" Module qui contient la classe AjoutDeLignesDepenses pour Y """


# =================================================================================================
# Paramètres globaux
# =================================================================================================

__author__ = "Julien LEPAIN"
__version__ = 1.0
__all__ = ["AjoutDeLignesDepenses"]


# =================================================================================================
# Import des librairies
# =================================================================================================

from PyQt5 import QtGui, QtCore, QtWidgets
import ihm.ajout_de_lignes_depenses as GUI_Ajout_de_lignes_depenses
import src.sous_classement_des_qvalidators as sous_classement_des_qvalidators


# =================================================================================================
# Classes
# =================================================================================================

# =========================================================================================
class AjoutDeLignesDepenses(QtWidgets.QMainWindow, GUI_Ajout_de_lignes_depenses.Ui_MainWindow):
    """
        Classe qui permet d'ouvrir une fenêtre afin d'insérer des lignes dans le TV affichage de la catégorie Dépenses
    """

    # Signal lié aux éléments à insérer : attribut _elements
    elements_a_inserer = QtCore.pyqtSignal(str)

    # ==============================
    def __init__(self, parent=None):
        """
            Constructeur de la classe
        """
        
        super(AjoutDeLignesDepenses, self).__init__(parent)
        self.setupUi(self)
        
        self.options_de_la_fenetre()
        self.connexion_des_widgets()

    # ==============================
    def options_de_la_fenetre(self):
        """
            Méthode qui permet de configurer certaines options pour la fenêtre
        """
        
        self.LE_moyen_de_paiement.setVisible(False)

        # Mise en place des QValidators
        validateur_date = sous_classement_des_qvalidators.SCQRegExpValidator()
        reg_exp = QtCore.QRegExp("[0-3][0-9]\/[0-1][0-9]\/20[0-9]{2}")
        validateur_date.setRegExp(reg_exp)
        self.LE_date.setValidator(validateur_date)

        validateur_montant = sous_classement_des_qvalidators.SCQDoubleValidation(-5000.0, 5000.0)
        validateur_montant.setDecimals(3)
        self.LE_montant.setValidator(validateur_montant)

    # ===============================================
    def gestion_affichage_LE_moyen_de_paiement(self):
        """
            Méthode qui permet de gérer l'affichage du QLineEdit LE_moyen_de_paiement
            selon la valeur choisie dans le QComboBox CB_moyen_de_paiement
        """

        if self.CB_moyen_de_paiement.currentText() in ["chèque"]:

            self.LE_moyen_de_paiement.setVisible(True)

        else:

            self.LE_moyen_de_paiement.setVisible(False)

    # ==========================
    def ajouter_une_ligne(self):
        """
            Méthode qui permet d'ajouter une ligne dans le TV affichage, dans la catégorie sélectionnée,
            en récupérant les informations renseignées par l'utilisateur dans la IHM
        """

        # Nettoyage de la chaîne de carcatères qui va contenir les éléments à envoyer
        self._elements = ""

        # Remplissage de la chaîne de caractères avec les éléments à envoyer
        self._elements = "{}\t{}\t{}\t{}".format(str(self.LE_date.text()),
                                                     str(self.LE_libelle.text()),
                                                     str(self.LE_montant.text()),
                                                     "chèque n° {}".format(self.LE_moyen_de_paiement.text()) if self.CB_moyen_de_paiement.currentText() in ["chèque"] else str(self.CB_moyen_de_paiement.currentText()))

        # Emission du signal contenant les éléments à insérer
        self.elements_a_inserer.emit(self._elements)

        # Nettoyage des QLineEdit
        self.LE_date.clear()
        self.LE_libelle.clear()
        self.LE_montant.clear()
        self.LE_moyen_de_paiement.clear()

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

        self.CB_moyen_de_paiement.currentIndexChanged.connect(self.gestion_affichage_LE_moyen_de_paiement)

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
