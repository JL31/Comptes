# coding: utf-8

""" Module qui contient la classe EnregistrementDesDonnees pour Y """


# =================================================================================================
# Paramètres globaux
# =================================================================================================

__author__ = "Julien LEPAIN"
__version__ = 1.0
__all__ = ["EnregistrementDesDonnees"]


# =================================================================================================
# Import des librairies
# =================================================================================================

import json
from datetime import datetime


# =================================================================================================
# Classes
# =================================================================================================

# =======================================
class EnregistrementDesDonnees(object):
    """
        Classe qui permet xxx
    """

    # ====================================================================
    def __init__(self, emplacement_absolu_du_fichier_de_donnees, donnees):
        """
            Constructeur de la classe
        """
        
        self._emplacement_absolu_du_fichier_de_donnees = emplacement_absolu_du_fichier_de_donnees
        self._donnees = donnees

    # =======================
    def enregistrement(self):
        """
            Méthode qui permet d'enregistrer/mettre-à-jour des données dans le fichier conteannt les données
        """
        
        # Récupération de la date du jour pour la modification de la date de mise-à-jour des données
        self._date_du_jour = datetime.now()
        
        # Modification de la date de mise-à-jour des données
        self._donnees["date_de_mise_a_jour"] = datetime.strftime(self._date_du_jour, "%d/%m/%Y")   # une autre solution serait de créer un objet contenant les données avec une méthode qui permet de modifier l'attribut date_de_mise_a_jour (via un mutateur)
        
        # Mise-à-jour des données
        with open(self._emplacement_absolu_du_fichier_de_donnees, 'w') as fichier_JSON:
            
            json.dump(self._donnees, fichier_JSON, indent=4)
            

# =================================================================================================
# Utilisation
# =================================================================================================

if __name__ == "__main__":
    
    print("Ce module n'est pas voué à être exécuté seul")
