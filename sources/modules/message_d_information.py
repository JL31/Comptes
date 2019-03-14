# coding: utf-8

""" Module qui permet d'afficher des messages d'information pour l'utilisateur via une fenêtre qui va s'ouvrir pour un temps limité """

# =================================================================================================
# Paramètres globaux
# =================================================================================================

__author__ = "Julien LEPAIN"
__version__ = 1.0


# =================================================================================================
# Import des librairies
# =================================================================================================

# Import des librairies graphiques
from PyQt4 import QtGui, QtCore
import GUI_fenetre_affichage_information as GUI_fenetre_affichage_information


# =================================================================================================
# Classes
# =================================================================================================


# ========================================================
class AffichageMessage(QtGui.QDialog, GUI_fenetre_affichage_information.Ui_Dialog):
    """
        Classe qui permet l'affichage d'une fenêtre, pour un temps limité, qui contient un message pour l'utilisateur
        La duré d'affichage est fixé via un attribut d'instance de la classe
    """

    # =======================================
    def __init__(self, message, parent=None):
        """
            Constructeur de la classe

            :param message: message à afficher à l'utilisateur
            :type message: str

            :param parent: parent du widget actuel
            :type parent: None

            :param __temporisation: durée d'affichage de la fenêtre exprimée en millisecondes
            :type __temporisation: float
        """

        super(AffichageMessage, self).__init__(parent)
        self.setupUi(self)

        self.__temporisation = 5000.0  # exprimé en millisecondes

        self.L_message.setText(message)

    # ==============
    def exec_(self):
        """
            Surcharge de la méthode
        """

        # Option 1 : affichage du widget sans contour (i.e. sans le bouton de fermeture en haut à droite du widget)
        # il est indispensable de faire au moins un self.show() sinon il n'y a pas d'affichage
        # il est aussi nécessaire d'exécuter les actions dans l'ordre ci-dessous sinon le widget ne s'affichera pas
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.adjustSize()
        self.show()

        # Option 2 : affichage en plein écran --- pour utiliser cette option plutôt que la première il faut :
        # - commenter les lignes de l'option 1
        # - décommenter les lignes suivantes
        # self.adjustSize()
        # self.showFullScreen()

        # Permet d'exécuter la la fonction passé en second argument au terme du délai (en ms) indiqué en premier argument
        QtCore.QTimer.singleShot(self.__temporisation, self.fermeture)

    def fermeture(self):
        """
            Méthode qui permet de clôre la fenêtre
        """

        self.accept()

# =================================================================================================
# Fonctions
# =================================================================================================

# =================================================================================================
# Utilisation
# =================================================================================================

if __name__ == "__main__":

    print("Je ne tourne pas seul !")
