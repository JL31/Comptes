"""
    Module qui contient la classe ModeleDepenses pour Y
"""


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

from typing import List, Dict, Tuple

from PyQt5 import QtGui, QtCore, QtWidgets
import numpy as np
from sqlite3 import Connection, Cursor


# =================================================================================================
# Classes
# =================================================================================================


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


class ModeleDepenses(QtCore.QAbstractTableModel):
    """ 
    Classe qui permet de remplir le TableView à partir des données de la catégorie Prélèvements
    """

    def __init__(self, database_connector: Connection, year: int, month: int, parent=None):
        """
        Constructeur de la classe
        """

        QtCore.QAbstractTableModel.__init__(self, parent)

        self._database_connector: Connection = database_connector
        self._year: int = year
        self._month: int = month

        self._donnees_pour_affichage: List[dict] = []
        self._header: List[str] = [
            "Date",
            "Libellé",
            "Montant (en €)",
            "Moyen de paiement"
        ]

        self._nom_des_colonnes: Dict[int, str] = {
            0: "date",
            1: "titre",
            2: "montant",
            3: "moyen_de_paiement"
        }

        self._somme_des_depenses: float = 0.0

        # Appel de la méthode qui permet d'extraire les données utiles pour l'affichage
        # self.extraction_des_donnees_pour_affichage()

    def set_mois(self, mois: int):
        """
        ...
        """

        self._month = mois

    @staticmethod
    def tuple_to_dict_mapping(element: Tuple) -> dict:
        """
        ...
        """

        return {
            "uuid": element[0],
            "libelle": element[1],
            "montant": float(element[2]),
            "type_de_paiement": element[3],
            "date_du_paiement": element[4]
        }

    def extraction_des_donnees_pour_affichage(self):
        """
        Méthode qui permet d'extraire, dans les données, celles utiles pour l'affichage
        """

        # self._donnees_pour_affichage = [
        #     {
        #         "date": element.get("date"),
        #         "titre": element.get("titre"),
        #         "montant": float(element.get("montant")),
        #         "moyen_de_paiement": element.get("moyen_de_paiement")
        #     } for element in self._donnees
        # ]

        request: str = """
    SELECT
        uuid,
        libelle,
        montant,
        type_de_paiement,
        date_du_paiement
    FROM
        depenses
    WHERE
        annee=:year
    AND
        mois=:month
    """

        cur: Cursor = self._database_connector.cursor()
        print(f"{self.__class__.__name__} / extraction_des_donnees_pour_affichage - mois : {self._month}\n\n")
        try:
            cur.execute(
                request,
                {
                    "year": self._year,
                    "month": self._month
                }
            )

            results: List[Tuple] = cur.fetchall()
            self._donnees_pour_affichage: List[dict] = [self.tuple_to_dict_mapping(result) for result in results]

        except Exception as error:
            print(f"{self.__class__.__name__} / extraction_des_donnees_pour_affichage - {error}")

    def get_donnees(self):
        """
        Accesseur des données du modèle (pour l'affichage)
        """

        return self._donnees_pour_affichage

    def set_donnees(self):
        """
        Mise-à-jour des données du modèle (pour l'affichage)
        """

        self.extraction_des_donnees_pour_affichage()
        self.modelReset.emit()

    @property
    def somme_des_depenses(self) -> float:
        """
        Propriété qui permet de récupérer la somme des dépenses
        """

        return sum([float(donnee.get("montant", 0)) for donnee in self._donnees_pour_affichage])

    def rowCount(self, parent=None) -> int:
        """
        Méthode qui permet de compter le nombre de lignes
        """

        return len(self._donnees_pour_affichage)

    def columnCount(self, parent=None) -> int:
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
                if self._donnees_pour_affichage[index.row()]["statut"]:
                    return QtGui.QBrush(QtGui.QColor(0, 255, 0))  # TODO : à placer en paramètre de classe ou autre ?

                # Sinon on laisse le fond par défaut
                else:
                    return QtGui.QBrush(QtGui.QColor(240, 240, 240))  # TODO : à placer en paramètre de classe ou autre ?

            # permet d'éviter que, lorsque l'on édite une cellule, le contenu ne soit remplacé par 0
            elif role == QtCore.Qt.EditRole:
                return self._donnees_pour_affichage[index.row()][self._nom_des_colonnes[index.column()]]

            # Si le rôle correspond à de l'affichage
            elif role == QtCore.Qt.DisplayRole:
                return self._donnees_pour_affichage[index.row()][self._nom_des_colonnes[index.column()]]

        return

    def headerData(self, col, orientation, role):
        """
        Méthode qui permet de remplir la première ligne du TableView avec les en-tetês du dataframe
        """

        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._header[col]

        return None

    def flags(self, index):
        """
        Méthode qui permet de configurer les opérations possibles sur les cellules (sélection, édition, ...)
        """

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

        # Modification de la donnée
        # Extraction de l'indice de ligne et de la colonne et conversion de la nouvelle valeur si besoin
        ligne = index.row()
        colonne = index.column()

        # Mise-à-jour de la donnée
        if colonne in [0, 1, 3]:
            self._donnees_pour_affichage[ligne][self._nom_des_colonnes[colonne]] = valeur

        elif colonne == 2:
            # valeur est un objet QVariant qu'il faut convertir en float via la méthode toFloat, méthode qui retourne un
            # tuple contenant la valeur convertie (en position 0) ainsi qu'un booléen (en position 1)
            valeur_convertie = np.float64(valeur)

            # il est ensuite nécessaire de convertir ce float en numpy.float64 pour être cohérent vis-à-vis des données
            # préalablement chargées
            # on arrondi à trois chiffres après la virgule pour éviter les co....... du style :
            # je tape 2.35 et cela affiche 2.34999958
            print(type(valeur_convertie))
            self._donnees_pour_affichage[ligne][self._nom_des_colonnes[colonne]] = round(valeur_convertie, 3)

        # Mise-à-jour des données pour affichage via la méthode "extraction_des_donnees_pour_affichage"
        self.extraction_des_donnees_pour_affichage()

        # Envoi du signal de changement des données
        self.dataChanged.emit(index, index)

        # Retour de la méthode
        return True
