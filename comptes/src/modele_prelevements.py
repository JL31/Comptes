# coding: utf-8

""" Module qui contient la classe ModelePrelevements pour Y """


# =================================================================================================
# Paramètres globaux
# =================================================================================================

__author__ = "Julien LEPAIN"
__version__ = 1.0
__all__ = ["ModelePrelevements"]


# =================================================================================================
# Import des librairies
# =================================================================================================

from PyQt5 import QtCore, QtGui
import numpy as np


# =================================================================================================
# Classes
# =================================================================================================

class ModelePrelevements(QtCore.QAbstractTableModel):
    """ 
    Classe qui permet de remplir le TableView à partir des données de la catégorie Prélèvements
    """ 

    def __init__(self, donnees, parent=None):
        """
        Constructeur de la classe
        """

        QtCore.QAbstractTableModel.__init__(self, parent)

        self._donnees = donnees

        self._donnees_pour_affichage = None
        self._header = ["Libellé", "Montant (en €)"]
        self._somme_des_prelevements = 0.0

        # Appel de la méthode qui permet d'extraire les données utiles pour l'affichage 
        self.extraction_des_donnees_pour_affichage()

    def extraction_des_donnees_pour_affichage(self):
        """
       Méthode qui permet d'extraire, dans les données, celles utiles pour l'affichage
        """

        self._donnees_pour_affichage = [
            {
                "titre": element.get("titre"),
                "montant": float(element.get("montant"))
            } for element in self._donnees
        ]

    def get_donnees(self):
        """
        Accesseur de l'attribut _donnees
        """

        return self._donnees

    def set_donnees(self, valeurs):
        """
        Mutateur de l'attribut _donnees
        """

        self._donnees = valeurs 
        self.extraction_des_donnees_pour_affichage()
        self.modelReset.emit()

    @property
    def somme_des_prelevements(self):
        """
        Propriété qui permet de récupérer la somme des prélèvements
        """

        return self._somme_des_prelevements

    def calculer_la_somme_des_prelevements(self):
        """
        Méthode qui permet de calculer la somme des dépenses
        """

        self._somme_des_prelevements = sum([float(element["montant"]) for indice, element in enumerate(self._donnees)])

    def rowCount(self, parent=None):
        """
        Méthode qui permet de compter le nombre de lignes
        """

        return len(self._donnees)

    def columnCount(self, parent=None):
        """
        Méthode qui permet de compter le nombre de colonnes
        """

        if self._donnees_pour_affichage:
            return len(self._donnees_pour_affichage[0].keys())
        else:
            return 0

    def data(self, index, role=QtCore.Qt.DisplayRole):
        """
        Méthode qui permet de remplir le TableVIew
        """

        # L'index est valide
        if index.isValid():
            # Si le rôle correspond au traitement du contenu de la cellule  ---> à vérifier !
            if role == QtCore.Qt.BackgroundRole:
                # Si le statut est à True on colorie la cellule en vert
                if self._donnees[index.row()]["statut"]:
                    return QtGui.QBrush(QtGui.QColor(0, 255, 0))
                # Sinon on laisse le fond par défaut
                else:
                    return QtGui.QBrush(QtGui.QColor(240, 240, 240))
            # permet d'éviter que, lorsque l'on édite une cellule, le contenu ne soit remplacé par 0
            elif role == QtCore.Qt.EditRole:
                return self._donnees_pour_affichage[index.row()]["montant"]
            # Si c'est pour de l'affichage on récupère seulement les données
            elif role == QtCore.Qt.DisplayRole:
                if index.column() == 0:
                    return self._donnees_pour_affichage[index.row()]["titre"]
                elif index.column() == 1:
                    return self._donnees_pour_affichage[index.row()]["montant"]

        return None

    def headerData(self, col, orientation, role):
        """
        Méthode qui permet de remplir la première ligne du TableView avec les en-tetês du dataframe
        """

        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._header[col]

        return None

    def flags(self, index):
        """
        Méthode qui permet de configurer les opérations possibles sur les cellules (sélection, édition...)
        """

        # Cas de la colonne contenant le libellé : la cellule est active et on autorise la sélection
        if index.column() == 0:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
        # Cas de la colonne le montant : la cellule est active et on autorise la sélection ainsi que l'édition
        elif index.column() == 1:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable

    def setData(self, index, valeur, role):
        """
        Méthode qui permet de modifier les données lorsque l'utilisateur a modifié la valeur d'une cellule
        """

        # Index invalide
        if not index.isValid():
            return False

        # Rôle invalide
        if role != QtCore.Qt.EditRole:
            return False

        # Extraction de l'indice de ligne et conversion de la nouvelle valeur
        ligne = index.row()

        # valeur est un objet QVariant qu'il faut convertir en float via la méthode toFloat, méthode qui retourne un
        # tuple contenant la valeur convertie (en position 0) ainsi qu'un booléen (en position 1)
        # il est ensuite nécessaire de convertir ce float en numpy.float64 pour être cohérent vis-à-vis des données
        # préalablement chargées
        valeur_convertie = np.float64(valeur)

        # Mise-à-jour de la donnée : on arrondi à trois chiffres après la virgule pour éviter les co....... du style :
        # je tape 2.35 et cela affiche 2.34999958
        self._donnees[ligne]["montant"] = round(valeur_convertie, 3)

        # Mise-à-jour des données pour affichage via la méthode "extraction_des_donnees_pour_affichage"
        self.extraction_des_donnees_pour_affichage()

        # Envoi du signal de changement des données
        self.dataChanged.emit(index, index)

        # Retour de la méthode
        return True
