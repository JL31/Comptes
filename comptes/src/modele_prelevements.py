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

# ===================================================
class ModelePrelevements(QtCore.QAbstractTableModel):
    """ 
        Classe qui permet de remplir le TableView à partir des données de la catégorie Prélèvements
    """ 

    # =======================================
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

    # ==============================================
    def extraction_des_donnees_pour_affichage(self):
        """
           Méthode qui permet d'extraire, dans les données, celles utiles pour l'affichage 
        """
        
        self._donnees_pour_affichage = [ {"titre": element["titre"], "montant": float(element["montant"]) } for indice, element in enumerate(self._donnees) ]

    # ====================
    def get_donnees(self):
        """
            Accesseur de l'attribut _donnees
        """
        
        return self._donnees

    # =============================
    def set_donnees(self, valeurs):
        """
            Mutateur de l'attribut _donnees
        """
        
        self._donnees = valeurs 
        self.extraction_des_donnees_pour_affichage()
        self.modelReset.emit()

    # ===============================
    @property
    def somme_des_prelevements(self):
        """
            Propriété qui permet de récupérer la somme des prélèvements
        """
        
        return self._somme_des_prelevements

    # ===========================================
    def calculer_la_somme_des_prelevements(self):
        """
            Méthode qui permet de calculer la somme des dépenses
        """
        
        self._somme_des_prelevements = sum([ float(element["montant"]) for indice, element in enumerate(self._donnees) ])

    # ==============================
    def rowCount(self, parent=None):
        """
            Méthode qui permet de compter le nombre de lignes
        """
        
        return len(self._donnees)

    # =================================
    def columnCount(self, parent=None):
        """
            Méthode qui permet de compter le nombre de colonnes
        """
        
        if self._donnees_pour_affichage:
            
            return len(self._donnees_pour_affichage[0].keys())
            
        else:
            
            return 0

    # ================================================
    def data(self, index, role=QtCore.Qt.DisplayRole):
        """
            Méthode qui permet de remplir le TableVIew
        """
        
        if index.isValid():
        # L'index est valide
            
            if role == QtCore.Qt.BackgroundRole:
            # Si le rôle correspond au traitement du contenu de la cellule  ---> à vérifier !
                
                if self._donnees[index.row()]["statut"]:
                # Si le statut est à True on colorie la cellule en vert
                    
                    return QtGui.QBrush(QtGui.QColor(0,255,0))
                    
                else:
                # Sinon on laisse le fond par défaut
                    
                    return QtGui.QBrush(QtGui.QColor(240,240,240))
                    
            elif role == QtCore.Qt.EditRole:
            # permet d'éviter que, lorsque l'on édite une cellule, le contenu ne soit remplacé par 0
                
                return self._donnees_pour_affichage[index.row()]["montant"]
                
            elif role == QtCore.Qt.DisplayRole:
            # Si c'est pour de l'affichage on récupère seulement les données
                
                if index.column() == 0:
                    
                    return self._donnees_pour_affichage[index.row()]["titre"]
                    
                elif index.column() == 1:
                    
                    return self._donnees_pour_affichage[index.row()]["montant"]
                    
        return None

    # ===========================================
    def headerData(self, col, orientation, role):
        """
            Méthode qui permet de remplir la première ligne du TableView avec les en-tetês du dataframe
        """
        
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            
            return self._header[col]
            
        return None

    # =====================
    def flags(self, index):
        """
            Méthode qui permet de configurer les opérations possibles sur les cellules (sélection, édition...)
        """
        
        if index.column() == 0:
        # Cas de la colonne contenant le libellé : la cellule est active et on autorise la sélection
            
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
            
        elif index.column() == 1:
        # Cas de la colonne le montant : la cellule est active et on autorise la sélection ainsi que l'édition
            
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable

    # =====================================
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
            
        # Modification de la donnée
        
        # Extraction de l'indice de ligne et conversion de la nouvelle valeur
        ligne = index.row()
        valeur_convertie = np.float64(valeur)              # valeur est un objet QVariant qu'il faut convertir en float via la méthode toFloat, méthode qui retourne un tuple contenant la valeur convertie (en position 0) ainsi qu'un booléen (en position 1)
                                                           # il est ensuite nécessaire de convertir ce float en numpy.float64 pour être cohérent vis-à-vis des données préalablement chargées
        
        # Mise-à-jour de la donnée
        self._donnees[ligne]["montant"] = round(valeur_convertie, 3)   # on arrondi à trois chiffres après la virgule pour éviter les co....... du style : je tape 2.35 et cela affiche 2.34999958
        
        # Mise-à-jour des données pour affichage via la méthode "extraction_des_donnees_pour_affichage"
        self.extraction_des_donnees_pour_affichage()
        
        # Envoi du signal de changement des données
        self.dataChanged.emit(index, index)
        
        # Retour de la méthode
        return True
        

# =================================================================================================
# Utilisation
# =================================================================================================

if __name__ == "__main__":
    
    print("Ce module n'est pas voué à être exécuté seul")
