"""
    Module qui contient les classes de sous-classement pour les QValidator pour l'application des comptes
"""

# =================================================================================================
# Paramètres globaux
# =================================================================================================

__all__ = [
    "SCQDoubleValidation",
    "SCItemDelegateTVAffichage"
]


# =================================================================================================
# Import des librairies
# =================================================================================================

from PyQt5 import QtGui, QtCore, QtWidgets
from datetime import datetime


# =================================================================================================
# Classes
# =================================================================================================

class SCQRegExpValidator(QtGui.QRegExpValidator):
    """
    Classe qui permet de sous-classer la classe QRegExpValidator
    """
    
    def __init__(self, parent=None):
        """
        Constructeur de la classe
        """
        
        super(SCQRegExpValidator, self).__init__(parent)
        
    def validate(self, ch, pos):
        """
        Méthode qui retourne la validation à chaque nouveau caractère
        """

        # on vérifie que la chaîne de caractère n'est pas vide
        if ch not in ['']:
            # on vérifie le jour indiqué
            if pos == 2:
                # si le jour indiqué est supérieur à 31 on retourne une entrée invalide, le format doit être tel que
                # spécifié ici
                if int(ch) > 31:
                    return QtGui.QValidator.Invalid, pos
            # on vérifie le mois indiqué
            elif pos == 5:
                # on extrait de la chaîne de caractère actuelle la partie qui correspond au mois
                ch_extrait = ch.split("/")[1]

                # si le mois indiqué est supérieur à 12 on retourne une entrée invalide, le format doit être tel que
                # spécifié ici
                if int(ch_extrait) > 12:
                    return QtGui.QValidator.Invalid, pos

            # https: // stackoverflow.com / questions / 69351364 / how - to - get - validate - result - qt
            # try:
            #     datetime.strptime(valeur, "%d/%m/%Y")
            # except ValueError:
            #     return QtGui.QValidator.Invalid, pos

        return QtGui.QRegExpValidator.validate(self, ch, pos)


class SCQDoubleValidation(QtGui.QDoubleValidator):
    """
    Classe qui permet de sous-classer la classe QDoubleValidator
    """
    
    def __init__(self, borne_inferieure, borne_superieure, parent=None):
        """
        Constructeur de la classe
        """

        super(SCQDoubleValidation, self).__init__(parent)
        self._borne_inferieure = borne_inferieure
        self._borne_superieure = borne_superieure

    def validate(self, ch, pos):
        """
        Méthode qui retourne la validation à chaque nouveau caractère
        """

        # on vérifie que la chaîne de caractère n'est pas vide
        if ch:

            # on vérifie que le premier caractère tapé n'est pas le point ('.') : si c'est le cas alors on retourne une
            # entrée invalide
            if ch[0] == '.':
                return QtGui.QValidator.Invalid, ch, pos

            # on vérifie que le premier caractère tapé n'est pas le signe moins ('-') si la borne inférieure est
            # positive : si c'est le cas alors on retourne une entrée invalide
            if ch[0] == '-' and self._borne_inferieure >= 0.0:
                return QtGui.QValidator.Invalid, ch, pos

            # on vérifie qu'il n'y ait pas les caractères 'e' et 'E' dans la chaîne : si c'est le cas alors on retourne
            # une entrée invalide
            if ch.find('e') != -1 or ch.find('E') != -1:
                return QtGui.QValidator.Invalid, ch, pos

            # on essaie de convertir la chaîne de caractères en float
            try:
                float(ch)
            except ValueError:
                return QtGui.QValidator.Invalid, ch, pos
            # on vérifie si l'on se trouve dans le range de valeurs spécifiée : si ce n'est pas le cas alors on retourne
            # une entrée invalide
            else:
                if float(ch) < self._borne_inferieure or float(ch) > self._borne_superieure:
                    return QtGui.QValidator.Invalid, ch, pos

        return QtGui.QDoubleValidator.validate(self, ch, pos)


class SCItemDelegateTVAffichage(QtWidgets.QStyledItemDelegate):
    """
    Classe qui permet de sous-classer la classe QStyledItemDelegate pour le TV Affichage
    """

    def __init__(self, categorie, borne_inferieure, borne_superieure, nombre_de_decimales, parent=None):
        """
        Constructeur de la classe
        """
        
        super(SCItemDelegateTVAffichage, self).__init__(parent)

        self._categorie = categorie
        self._borne_inf = borne_inferieure
        self._borne_sup = borne_superieure
        self._nombre_de_decimales = nombre_de_decimales

    def createEditor(self, widget, option, index):
        """
        Méthode qui permet d'affecter un Qvalidator à certaines cellules du TableView
        """

        # Vérification de la validité de l'index
        if not index.isValid():
            return 0

        # Récupération du numéro de la colonne active
        colonne: int = index.column()

        # Affectation des QValidators selon la colonne active
        if self._categorie in ["prelevements"]:
            # colonne contenant les montants
            if colonne == 1:
                editeur = QtWidgets.QLineEdit(widget)
                validateur = SCQDoubleValidation(self._borne_inf, self._borne_sup)
                validateur.setDecimals(self._nombre_de_decimales)
                editeur.setValidator(validateur)
                return editeur

        elif self._categorie in ["epargnes"]:
            # colonne contenant les montants
            if colonne == 2:
                editeur = QtWidgets.QLineEdit(widget)
                validateur = SCQDoubleValidation(self._borne_inf, self._borne_sup)
                validateur.setDecimals(self._nombre_de_decimales)
                editeur.setValidator(validateur)
                return editeur

            elif colonne in [3, 4]:
                editeur = QtWidgets.QLineEdit(widget)
                reg_exp = QtCore.QRegExp("^(3[0-1]|[1-2]\d|0[1-9])\/(1[0-2]|0[1-9])\/20\d{2}$")
                validateur = SCQRegExpValidator()
                validateur.setRegExp(reg_exp)
                editeur.setValidator(validateur)
                return editeur

        elif self._categorie in ["depenses"]:
            # colonne contenant les dates
            if colonne == 0:
                editeur = QtWidgets.QLineEdit(widget)
                reg_exp = QtCore.QRegExp("^(3[0-1]|[1-2]\d|0[1-9])\/(1[0-2]|0[1-9])\/20\d{2}$")
                validateur = SCQRegExpValidator()
                validateur.setRegExp(reg_exp)
                editeur.setValidator(validateur)
                return editeur

            # colonne contenant les montants
            elif colonne == 2:
                editeur = QtWidgets.QLineEdit(widget)
                validateur = SCQDoubleValidation(self._borne_inf, self._borne_sup)
                validateur.setDecimals(self._nombre_de_decimales)
                editeur.setValidator(validateur)
                return editeur

        return super(SCItemDelegateTVAffichage, self).createEditor(widget, option, index)
