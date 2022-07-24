# coding: utf-8

""" Module qui contient la classe ModeleDepenses pour Y """


# =================================================================================================
# Paramètres globaux
# =================================================================================================

__all__ = [
    "ModeleDepenses",
    "ComboBoxDelegate"
]


# =================================================================================================
# Import des librairies
# =================================================================================================

from typing import List

from PyQt5 import QtGui, QtCore, QtWidgets
import numpy as np


# =================================================================================================
# Classes
# =================================================================================================


# ==============================================
class ComboBoxDelegate(QtWidgets.QItemDelegate):
    """
        Classes qui permet de créer des QComboBox dans la dernière colonne des dépenses
    """

    liste_des_moyens_de_paiements: List[str] = [
        "CB",
        "chèque",
        "virement bancaire",
        "elle",
        "Virement depuis Livret A",
        "Virement vers Livret A"
    ]

    # ======================================================
    def createEditor(self, parent, option, index):
        """
            xxx

            :param parent: parent
            :type parent:

            :param option:
            :type option:

            :param index:
            :type index: QIndex

            :return:
            :rtype:
        """

        editor = QtGui.QComboBox(parent)
        editor.addItems(self.liste_des_moyens_de_paiements)

        return editor

    # =====================================
    def setEditorData(self, editor, index):
        """
            xxx

            :param editor:
            :type editor:

            :param index:
            :type index: QIndex
        """

        value = index.model().data(index, QtCore.Qt.EditRole)
        editor.setCurrentIndex(editor.findText(value))

# ===============================================
class ModeleDepenses(QtCore.QAbstractTableModel):
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
        
        self._header = ["Date", "Libellé", "Montant (en €)", "Moyen de paiement"]
        self._nom_des_colonnes = { 0: "date",
                                   1: "titre",
                                   2: "montant",
                                   3: "moyen_de_paiement"
                                 }
        self._somme_des_depenses = 0.0

        # Appel de la méthode qui permet d'extraire les données utiles pour l'affichage
        self.extraction_des_donnees_pour_affichage()

    # ==============================================
    def extraction_des_donnees_pour_affichage(self):
        """
           Méthode qui permet d'extraire, dans les données, celles utiles pour l'affichage 
        """
        
        self._donnees_pour_affichage = [ {"date": element["date"], "titre": element["titre"], "montant": float(element["montant"]), "moyen_de_paiement": element["moyen_de_paiement"] } for indice, element in enumerate(self._donnees) ]

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

    # ===========================
    @property
    def somme_des_depenses(self):
        """
            Propriété qui permet de récupérer la somme des dépenses
        """
        
        return self._somme_des_depenses

    # =======================================
    def calculer_la_somme_des_depenses(self):
        """
            Méthode qui permet de calculer la somme des dépenses
        """
        
        self._somme_des_depenses = sum([ float(element["montant"]) for indice, element in enumerate(self._donnees) ])

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

                return self._donnees_pour_affichage[index.row()][self._nom_des_colonnes[index.column()]]
                
            elif role == QtCore.Qt.DisplayRole:
            # Si le rôle correspond à de l'affichage
                
                return self._donnees_pour_affichage[index.row()][self._nom_des_colonnes[index.column()]]
                
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
            Méthode qui permet de configurer les opérations possibles sur les cellules (sélection, édition, ...)
        """
        
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
        
        # Extraction de l'indice de ligne et de la colonne et conversion de la nouvelle valeur si besoin
        ligne = index.row()
        colonne = index.column()

        # Mise-à-jour de la donnée
        if colonne in [0, 1, 3]:

            self._donnees[ligne][self._nom_des_colonnes[colonne]] = valeur

        elif colonne == 2:
            
            valeur_convertie = np.float64(valeur)           # valeur est un objet QVariant qu'il faut convertir en float via la méthode toFloat, méthode qui retourne un tuple contenant la valeur convertie (en position 0) ainsi qu'un booléen (en position 1)
                                                            # il est ensuite nécessaire de convertir ce float en numpy.float64 pour être cohérent vis-à-vis des données préalablement chargées
            print(type(valeur_convertie))
            self._donnees[ligne][self._nom_des_colonnes[colonne]] = round(valeur_convertie, 3)   # on arrondi à trois chiffres après la virgule pour éviter les co....... du style : je tape 2.35 et cela affiche 2.34999958
            
        
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
