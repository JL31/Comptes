"""
    Module qui contient la classe LectureFichierJSON pour Y
"""

# =================================================================================================
# Paramètres globaux
# =================================================================================================

__all__ = ["LectureFichierJSON"]


# =================================================================================================
# Import des librairies
# =================================================================================================

import os
import sys
import json
from src.verification_donnees_json import VerificationDonneesJSON


# =================================================================================================
# Classes
# =================================================================================================

class LectureFichierJSON(object):
    """
    Classe de lecture du contenu du fichier contenant les données pour Y
    """

    def __init__(self, emplacement_absolu_du_fichier: str, type_de_fichier: str):
        """
        Constructeur de la classe
        """

        self._emplacement_absolu_du_fichier: str = emplacement_absolu_du_fichier
        self._type_de_fichier: str = type_de_fichier

        self._contenu_du_fichier = None
        self._objet_VerificationDonneesJSON = None

    def get_contenu_du_fichier(self):
        """
        Accesseur de l'attribut _contenu_du_fichier
        """

        return self._contenu_du_fichier

    def lecture_du_fichier(self):
        """
        Méthode qui permet de lire le contenu du fichier au format JSON
        """

        # On vérifie si le fichier existe dans le répertoire contenant l'application
        if not os.path.isfile(self._emplacement_absolu_du_fichier):
            raise OSError("Le fichier '{}' n'existe pas dans le dossier '{}'".format(os.path.basename(self._emplacement_absolu_du_fichier), os.path.dirname(self._emplacement_absolu_du_fichier)))

        # Lecture du fichier
        # ATTENTION : il faut que le fichier JSON soit encodé en ANSI sinon impossible de le lire !
        with open(self._emplacement_absolu_du_fichier, 'r', encoding="utf-8") as fichier:
            try:
                self._contenu_du_fichier = json.load(fichier)
            except ValueError:
                print("Le fichier '{}' est peut-être vide, merci de vérifier".format(os.path.basename(self._emplacement_absolu_du_fichier)))
                sys.exit()

        # Création d'un objet VerificationDonneesJSON pour les vérification basiques sur le contenu du fichier
        if self._type_de_fichier in ["donnees"]:
            self._objet_VerificationDonneesJSON = VerificationDonneesJSON(self._contenu_du_fichier)
