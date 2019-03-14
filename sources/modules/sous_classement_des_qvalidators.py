# coding: utf-8

""" Module qui contient les classes de sous-classement pour les QValidator pour l'application des comptes """


# =================================================================================================
# Paramètres globaux
# =================================================================================================

__author__ = "Julien LEPAIN"
__version__ = 1.0
__all__ = ["SCQDoubleValidation",
           "SCItemDelegateTVAffichage"]


# =================================================================================================
# Import des librairies
# =================================================================================================

from PyQt4 import QtGui, QtCore


# =================================================================================================
# Classes
# =================================================================================================

# ===============================================
class SCQRegExpValidator(QtGui.QRegExpValidator):
    """
        Classe qui permet de sous-classer la classe QRegExpValidator
    """
    
    # ==============================
    def __init__(self, parent=None):
        """
            Constructeur de la classe
        """
        
        super(SCQRegExpValidator, self).__init__(parent)
        
    # ==========================
    def validate(self, ch, pos):
        """
            Méthode qui retourne la validation à chaque nouveau caractère
        """
        
        if ch not in ['']:
        # on vérifie que la chaîne de caractère n'est pas vide
            
            if pos == 2:
            # on vérifie le jour indiqué
                
                if int(ch) > 31:
                # si le jour indiqué est supérieur à 31 on retourne une entrée invalide (le format doit être tel que spécifié ici)
                    
                    return (QtGui.QValidator.Invalid, pos)
                
            elif pos == 5:
            # on vérifie le mois indiqué
                
                # on extrait de la chaîne de caractère actuelle la partie qui correspond au mois
                ch_extrait = ch.split("/")[1]
                
                if int(ch_extrait) > 12:
                # si le mois indiqué est supérieur à 12 on retourne une entrée invalide (le format doit être tel que spécifié ici)
                    
                    return (QtGui.QValidator.Invalid, pos)
                    
        return QtGui.QRegExpValidator.validate(self, ch, pos)
        
# ================================================
class SCQDoubleValidation(QtGui.QDoubleValidator):
    """
        Classe qui permet de sous-classer la classe QDoubleValidator
    """
    
    # ==================================================================
    def __init__(self, borne_inferieure, borne_superieure, parent=None):
        """
            Constructeur de la classe
        """
        
        super(SCQDoubleValidation, self).__init__(parent)
        self._borne_inferieure = borne_inferieure
        self._borne_superieure = borne_superieure
        
    # ==========================
    def validate(self, ch, pos):
        """
            Méthode qui retourne la validation à chaque nouveau caractère
        """
        
        if ch not in ['']:
            # on vérifie que la chaîne de caractère n'est pas vide
            
            if pos == 1 and ch in ['.']:
                # on vérifie que le premier caractère tapé n'est pas le point ('.')
                # si c'est le cas alors on retourne une entrée invalide (le format doit être tel que spécifié ici)
                
                return (QtGui.QValidator.Invalid, pos)
                
            if pos == 1 and ch in ['-'] and self._borne_inferieure >= 0.0:
                # on vérifie que le premier caractère tapé n'est pas le signe moins ('-') si la borne inférieur est positive
                # si c'est le cas alors on retourne une entrée invalide (le format doit être tel que spécifié ici)
                
                return (QtGui.QValidator.Invalid, pos)
                
            if str(ch).find('e') != -1 or str(ch).find('E') != -1:
                # on vérifie qu'il n'y ait pas les caractères 'e' et 'E' dans la chaîne
                # si c'est le cas alors on retourne une entrée invalide (le format doit être tel que spécifié ici)
                
                return (QtGui.QValidator.Invalid, pos)
                
            try:
                # on essaie de convertir la chaîne de caractères en float
                
                float(ch)
            
            except ValueError:
                # on ne fait rien jsute pour éviter d'avoir une exception ValueError levée
                
                pass
                
            else:
                # on vérifie si l'on se trouve dans le range de valeurs spécifiée
                
                if float(ch) < self._borne_inferieure or float(ch) > self._borne_superieure:
                    # si ce n'est pas le cas alors on retourne une entrée invalide (le format doit être tel que spécifié ici)
                    
                    return (QtGui.QValidator.Invalid, pos)
                    
        return QtGui.QDoubleValidator.validate(self, ch, pos)
        

# =========================================================
class SCItemDelegateTVAffichage(QtGui.QStyledItemDelegate):
    """
        Classe qui permet de sous-classer la classe QStyledItemDelegate pour le TV Affichage
    """

    # ==================================================================================================
    def __init__(self, categorie, borne_inferieure, borne_superieure, nombre_de_decimales, parent=None):
        """
            Constructeur de la classe
        """
        
        super(SCItemDelegateTVAffichage, self).__init__(parent)

        self._categorie = categorie
        self._borne_inf = borne_inferieure
        self._borne_sup = borne_superieure
        self._nombre_de_decimales = nombre_de_decimales

    # ============================================
    def createEditor(self, widget, option, index):
        """
            Méthode qui permet d'affecter un Qvalidator à certaines cellules du TableView
        """
        
        # Vérification de la validité de l'index
        
        if not index.isValid():
            
            return 0
            
        # Récupération du numéro de la colonne active
        
        colonne = index.column()
        
        # Affectation des QValidators selon la colonne active

        if self._categorie in ["prelevements", "epargnes"]:

            if colonne == 1:
                # colonne contenant les montants

                editeur = QtGui.QLineEdit(widget)
                validateur = SCQDoubleValidation(self._borne_inf, self._borne_sup)
                validateur.setDecimals(self._nombre_de_decimales)
                editeur.setValidator(validateur)

                return editeur

        elif self._categorie in ["depenses"]:

            if colonne == 0:
                # colonne contenant les dates

                editeur = QtGui.QLineEdit(widget)
                reg_exp = QtCore.QRegExp("[0-3][0-9]\/[0-1][0-9]\/20[0-9]{2}")
                validateur = SCQRegExpValidator()
                validateur.setRegExp(reg_exp)
                editeur.setValidator(validateur)

                return editeur

            elif colonne == 2:
                # colonne contenant les montants

                editeur = QtGui.QLineEdit(widget)
                validateur = SCQDoubleValidation(self._borne_inf, self._borne_sup)
                validateur.setDecimals(self._nombre_de_decimales)
                editeur.setValidator(validateur)

                return editeur

        return super(SCItemDelegateTVAffichage, self).createEditor(widget, option, index)
        

# =================================================================================================
# Utilisation
# =================================================================================================

if __name__ == "__main__":
    
    print("Ce module n'est pas voué a être exécuté seul")
