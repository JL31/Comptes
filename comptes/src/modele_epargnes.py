"""
    Module qui contient la classe ModeleEpargnes pour Y
"""


# =================================================================================================
# Paramètres globaux
# =================================================================================================

__all__ = [
    "ModeleEpargnes"
]


# =================================================================================================
# Import des librairies
# =================================================================================================

from PyQt5 import QtCore, QtGui
import numpy as np
from typing import List, Tuple, Union, Optional
from sqlite3 import Connection, Cursor


# =================================================================================================
# Classes
# =================================================================================================

class ModeleEpargnes(QtCore.QAbstractTableModel):
    """ 
    Classe qui permet de remplir le TableView à partir des données de la catégorie Epargnes
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
            "uuid",
            "Libellé",
            "Montant (en €)",
            "Date de création du virement",
            "Date à laquelle le virement a été effectué"
        ]
        self._liste_des_valeurs_a_diviser: List[str] = [
            "Taxe_habitation",
            "Taxe_fonciere"
        ]
        self._somme_des_epargnes: float = 0.0

    def set_mois(self, mois: int):
        """
        ...
        """

        print(f"{self.__class__.__name__} / set_mois - mois : {self._month} (avant)")
        self._month = mois
        print(f"{self.__class__.__name__} / set_mois - mois : {self._month} (après, mois = {mois})")

    @staticmethod
    def tuple_to_dict_mapping(element: Tuple) -> dict:
        """
        ...
        """

        return {
            "uuid": element[0],
            "libelle": element[1],
            "montant": float(element[2]),
            "date_de_creation_du_virement": element[3],
            "date_virement_effectue": element[4]
        }

    def extraction_des_donnees_pour_affichage(self):
        """
       Méthode qui permet d'extraire, dans les données, celles utiles pour l'affichage
        """

        request: str = """
    SELECT
        uuid,
        libelle,
        montant,
        date_de_creation_du_virement,
        date_virement_effectue
    FROM
        epargnes
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

    def get_donnees(self) -> List[dict]:
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
    def somme_des_epargnes(self) -> float:
        """
        Propriété qui permet de récupérer la somme des épargnes
        """

        return sum([donnee.get("montant", 0.0) for donnee in self._donnees_pour_affichage])

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

    def data(self, index: QtCore.QModelIndex, role=QtCore.Qt.DisplayRole) -> Union[QtGui.QBrush, str, float, None]:
        """
        Méthode qui permet de remplir le TableVIew
        """

        index_row: int = index.row()
        index_column: int = index.column()

        # L'index est valide
        if index.isValid():

            # Si le rôle correspond au traitement du contenu de la cellule  ---> à vérifier !
            if role == QtCore.Qt.BackgroundRole:

                # Si le statut est à True on colorie la cellule en vert
                if self._donnees_pour_affichage[index_row].get("date_de_creation_du_virement") and self._donnees_pour_affichage[index_row].get("date_virement_effectue"):
                    return QtGui.QBrush(QtGui.QColor(0, 255, 0))

                elif self._donnees_pour_affichage[index_row].get("date_de_creation_du_virement"):
                    return QtGui.QBrush(QtGui.QColor(255, 0, 0))

                # Sinon on laisse le fond par défaut
                else:
                    return QtGui.QBrush(QtGui.QColor(240, 240, 240))

            # permet d'éviter que, lorsque l'on édite une cellule, le contenu ne soit remplacé par 0
            elif role == QtCore.Qt.EditRole:
                return self._donnees_pour_affichage[index.row()].get("montant")

            # Si le rôle correspond à de l'affichage
            elif role == QtCore.Qt.DisplayRole:
                # Si l'on se situe sur la première colonne on récupère l'uuid'
                if index_column == 0:
                    return self._donnees_pour_affichage[index_row].get("uuid")

                # Si l'on se situe sur la première colonne on récupère le libellé
                if index_column == 1:
                    return self._donnees_pour_affichage[index_row].get("libelle")

                # Sinon on récupère le montant
                elif index_column == 2:
                    return self._donnees_pour_affichage[index_row].get("montant")

                # Sinon on récupère la date de création du virement
                elif index_column == 3:
                    return self._donnees_pour_affichage[index_row].get("date_de_creation_du_virement")

                # Sinon on récupère la date à laquelle le virement est effectué
                elif index_column == 4:
                    return self._donnees_pour_affichage[index_row].get("date_virement_effectue")

        return

    def headerData(self, col, orientation, role) -> Optional[str]:
        """
        Méthode qui permet de remplir la première ligne du TableView avec les en-tetês du dataframe
        """

        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._header[col]

        return

    # def flags(self, index: QtCore.QModelIndex) -> Union[QtCore.Qt.ItemIsEnabled, QtCore.Qt.ItemIsSelectable, QtCore.Qt.ItemIsEditable]:
    def flags(self, index: QtCore.QModelIndex):
        """
        Méthode qui permet de configurer les opérations possibles sur les cellules (sélection, édition, ...)
        """

        index_column: int = index.column()

        # Cas de la colonne contenant l'uuid' :
        # >> la cellule est présente mais invisible, non sélectionnable et non éditable
        if index_column == 0:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

        # Cas de la colonne contenant le libellé :
        # >> la cellule est active et on autorise la sélection
        if index_column == 1:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

        # Cas de la colonne contenant soit :
        # - le montant
        # - la date de création du virement
        # - la date à laquelle le virement a été effectué
        # >> la cellule est active et on autorise la sélection ainsi que l'édition
        elif index_column in [2, 3, 4]:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable

    def setData(self, index: QtCore.QModelIndex, valeur: str, role: int) -> bool:
        """
        Méthode qui permet de modifier les données lorsque l'utilisateur a modifié la valeur d'une cellule
        """

        # TODO : faire une validation des dates ici via un try/except datetime (car la regex ne couvrira pas tous les cas :D)

        # Index invalide
        if not index.isValid():
            return False

        # Rôle invalide
        if role != QtCore.Qt.EditRole:
            return False

        # Modification de la donnée
        # Extraction de l'indice de ligne et conversion de la nouvelle valeur
        # valeur est un objet QVariant qu'il faut convertir en float via la méthode toFloat, méthode qui retourne un
        # tuple contenant la valeur convertie (en position 0) ainsi qu'un booléen (en position 1)
        # il est ensuite nécessaire de convertir ce float en numpy.float64 pour être cohérent vis-à-vis des données
        # préalablement chargées
        ligne: int = index.row()
        colonne: int = index.column()

        converted_value: Union[float, str] = float(valeur) if colonne == 2 else f"'{valeur}'"

        parameters: dict = {
            "uuid": self._donnees_pour_affichage[ligne].get("uuid"),
            "parameter_value": converted_value
        }

        if colonne == 2:
            parameters["parameter_name"] = "montant"
        elif colonne == 3:
            parameters["parameter_name"] = "date_de_creation_du_virement"
        elif colonne == 4:
            parameters["parameter_name"] = "date_virement_effectue"

        # if colonne == 2:
        #     print(valeur)
        #     print(type(valeur))
        #     valeur_convertie = np.float64(valeur)
        #
        #     # Mise-à-jour de la donnée : on arrondi à trois chiffres après la virgule pour éviter les co....... du style :
        #     # je tape 2.35 et cela affiche 2.34999958
        #     self._donnees_pour_affichage[ligne]["montant"] = round(valeur_convertie, 3)
        #
        # elif colonne == 3:
        #     print("là")
        #     print(f"valeur : {valeur}")
        #     self._donnees_pour_affichage[ligne]["date_de_creation_du_virement"] = valeur
        #
        # elif colonne == 4:
        #     self._donnees_pour_affichage[ligne]["date_virement_effectue"] = valeur

        # ...
        self.update_value(**parameters)

        # Mise-à-jour des données pour affichage via la méthode "extraction_des_donnees_pour_affichage"
        self.extraction_des_donnees_pour_affichage()

        # Envoi du signal de changement des données
        self.dataChanged.emit(index, index)

        # Retour de la méthode
        return True

    def update_value(self, uuid: str, parameter_name: str, parameter_value: str):
        """
        ...
        """

        update_parameter: str = f"{parameter_name} = {parameter_value}"

        request: str = f"""
UPDATE
    epargnes
SET
    {update_parameter}
WHERE
    uuid=:uuid
AND
    annee=:year
AND
    mois=:month
"""

        cur: Cursor = self._database_connector.cursor()

        try:
            cur.execute(
                request,
                {
                    "uuid": uuid,
                    "year": self._year,
                    "month": self._month
                }
            )
            self._database_connector.commit()

        except Exception as error:
            print(f"update_value - {error}")
            self._database_connector.rollback()
