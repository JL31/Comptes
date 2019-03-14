# coding: utf-8

""" Module qui contient la classe DupliquerDonneesMois pour Y """

# =================================================================================================
# Paramètres globaux
# =================================================================================================

__author__ = "Julien LEPAIN"
__version__ = 1.0
__all__ = ["DupliquerDonneesMois"]


# =================================================================================================
# Import des librairies
# =================================================================================================

from PyQt4 import QtGui, QtCore
import GUI_Dupliquer_donnees_mois as GUI_Dupliquer_donnees_mois


# =================================================================================================
# Classes
# =================================================================================================

# ==============================================================================
class DupliquerDonneesMois(QtGui.QDialog, GUI_Dupliquer_donnees_mois.Ui_Dialog):
    """
        Classe qui permet d'ouvrir une fenêtre afin de dupliquer les données d'un mois vers un autre dans une catégorie sélectionnée
    """
    
    # ===================================================
    def __init__(self, instance_controleur, parent=None):
        """
            Constructeur de la classe
        """
        
        super(DupliquerDonneesMois, self).__init__(parent)
        self.setupUi(self)

        self._instance_controleur = instance_controleur
        self._donnees = self._instance_controleur.get_donnees()

        self._categorie = u""
        self._mois_source = u""
        self._mois_destination = u""
        
        self._dico_categories = { "Prélèvements": "prelevements",
                                  "Epargnes": "epargnes"
                                }
        
        self._liste_des_mois = ["janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre", "decembre"]
        
        self._dico_des_mois_simple_vers_complexe = { "janvier": "Janvier",
                                                     "fevrier": "Février",
                                                     "mars": "Mars",
                                                     "avril": "Avril",
                                                     "mai": "Mai",
                                                     "juin": "Juin",
                                                     "juillet": "Juillet",
                                                     "aout": "Août",
                                                     "septembre": "Septembre",
                                                     "octobre": "Octobre",
                                                     "novembre": "Novembre",
                                                     "decembre": "Décembre"
                                                   }
        
        self._dico_des_mois_complexe_vers_simple = { "Janvier": "janvier",
                                                     "Février": "fevrier",
                                                     "Mars": "mars",
                                                     "Avril": "avril",
                                                     "Mai": "mai",
                                                     "Juin": "juin",
                                                     "Juillet": "juillet",
                                                     "Août": "aout",
                                                     "Septembre": "septembre",
                                                     "Octobre": "octobre",
                                                     "Novembre": "novembre",
                                                     "Décembre": "decembre"
                                                   }

        # Initialisations
        self.options_de_la_fenetre()
        self.connexion_des_widgets()
        self.mise_a_jour_mois_source()
        
    # ==============================
    def options_de_la_fenetre(self):
        """
            Méthode qui permet de configurer certaines options pour la fenêtre
        """

        pass

    # =============================
    def fenetre_confirmation(self):
        """
            Méthode qui permet d'ouvrir une fenêtre demandant à l'utilisateur de confirmer/d'annuler l'écrasement des données dans le mois sélectionné
        """
        
        # Création de la fénêtre
        self._fenetre_confirmation = QtGui.QMessageBox()
        
        # Paramétrage de la fenêtre
        self._fenetre_confirmation.setWindowTitle("Confirmation")
        self._fenetre_confirmation.setText("Le mois dans lequel vouz voulez écrire des données n'est pas vide.\nVoulez-vous écraser les données existentes ?")
        self._fenetre_confirmation.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        self._fenetre_confirmation.setDefaultButton(QtGui.QMessageBox.No)
        self._fenetre_confirmation.setIcon(QtGui.QMessageBox.Warning)
        
        # Lancement de la fenêtre
        self._choix_confirmation = self._fenetre_confirmation.exec_()
        
    # ==================
    def dupliquer(self):
        """
            Méthode qui permet de dupliquer les données
        """
        
        # Récupération de l'info du QComboBox CB_categorie
        categorie_selectionnee = self.CB_categorie.currentText()
        self._categorie = self._dico_categories[categorie_selectionnee]
        
        # Récupération de l'info du QComboBox CB_source
        mois_source_selectionne = self.CB_mois_source.currentText()
        self._mois_source = self._dico_des_mois_complexe_vers_simple[mois_source_selectionne]
        
        # Récupération de l'info du QComboBox CB_destination
        mois_destination_selectionne = self.CB_mois_destination.currentText()
        self._mois_destination = self._dico_des_mois_complexe_vers_simple[mois_destination_selectionne]
        
        # Vérification du contenu du mois destination pour la catégorie sélectionnée
        if len(self._donnees[self._mois_destination][self._categorie]) > 0:
            
            # Ouverture de la fenêtre de confirmation du choix
            self.fenetre_confirmation()
            
            # Traitement du choix
            if self._choix_confirmation == QtGui.QMessageBox.Yes:

                self._donnees[self._mois_destination][self._categorie] = self._donnees[self._mois_source][self._categorie]

        else:

            self._donnees[self._mois_destination][self._categorie] = self._donnees[self._mois_source][self._categorie]

        # Mise-à-jour des données dans l'instance du controleur
        self._instance_controleur.set_donnees(self._donnees)

        # Fermeture de la fenêtre
        self.accept()

    # ================================
    def mise_a_jour_mois_source(self):
        """
            Méthode qui permet de mettre à jour le QComboBox CB_mois_source en fonction de la catégorie sélectionée
        """
        
        # Initialisation
        self._liste_des_mois_contenant_des_donnees = []
        
        # On itère sur la liste des mois
        for indice, mois in enumerate(self._liste_des_mois):
            
            # On récupère l'info du QComboBox CB_categorie
            categorie_selectionnee = self.CB_categorie.currentText()
            self._categorie = self._dico_categories[categorie_selectionnee]
            
            # On extrait, des données, un sous-set de données pour le mois et la catégorie en cours
            self._extrait_donnees = self._donnees[mois][self._categorie]
            
            # Si le sous-set de données n'est pas vide on ajoute le mois en cours à la liste des mois contenant des données
            if len(self._extrait_donnees) > 0:
                
                self._liste_des_mois_contenant_des_donnees.append(self._dico_des_mois_simple_vers_complexe[mois])
                
        # Nettoyage du QComboBox avant d'ajouter les éléments"
        self.CB_mois_source.clear()
        
        # Ajout des éléments au QComboBox
        self.CB_mois_source.addItems(self._liste_des_mois_contenant_des_donnees)
        
    # ==============================
    def connexion_des_widgets(self):
        """
            Méthode qui permet de connecter les widgets
        """
        
        self.CB_categorie.currentIndexChanged.connect(self.mise_a_jour_mois_source)
        self.B_dupliquer.clicked.connect(self.dupliquer)
        

# =================================================================================================
# Utilisation
# =================================================================================================

if __name__ == "__main__":
    
    print("Ce module n'est pas voué à être exécuté seul")
