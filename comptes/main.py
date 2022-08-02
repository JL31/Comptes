"""
    Module qui permet de lancer l'application
"""

# =================================================================================================
# Import des librairies
# =================================================================================================

# Import des librairies graphiques
from PyQt5 import QtWidgets

# Import des librairies qui contiennent le modèle
from src.controleur import Controleur

# Import des autres librairies
import sys


# =================================================================================================
# Utilisation
# =================================================================================================

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    instance_controleur = Controleur(app)
    app.exec_()
