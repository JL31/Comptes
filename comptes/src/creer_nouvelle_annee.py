# coding: utf-8

""" Module qui contient la classe CreerNouvelleAnnee pour Y """

# =================================================================================================
# Paramètres globaux
# =================================================================================================

__author__ = "Julien LEPAIN"
__version__ = 1.0
__all__ = ["CreerNouvelleAnnee"]

# =================================================================================================
# Import des librairies
# =================================================================================================

from PyQt5 import QtGui, QtCore, QtWidgets
import ihm.creer_nouvelle_annee as GUI_Creer_nouvelle_annee
from src.enregistrement_des_donnees import EnregistrementDesDonnees
import os
from datetime import datetime

# =================================================================================================
# Classes
# =================================================================================================

# ==============================================================================
class CreerNouvelleAnnee(QtWidgets.QDialog, GUI_Creer_nouvelle_annee.Ui_Dialog):
    """
        Classe qui permet d'ouvrir une fenêtre afin de créer un fichier de données pour l'année suivante
    """

    # ===================================================
    def __init__(self, instance_controleur, parent=None):
        """
            Constructeur de la classe
        """

        super(CreerNouvelleAnnee, self).__init__(parent)
        self.setupUi(self)

        self._instance_controleur = instance_controleur

        self._donnees = self._instance_controleur.get_donnees()
        self._emplacement_du_dossier_des_donnees = self._instance_controleur.get_emplacement_du_dossier_des_donnees()

        self._choix_utilisateur = False

        self._dico_choix_utilisateur = { False: True,
                                         True: False
                                        }

        self._liste_des_mois = ["janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre",
                                "novembre", "decembre"]

        self._dico_des_mois_simple_vers_complexe = {"janvier": "Janvier",
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

        self._dico_des_mois_complexe_vers_simple = {"Janvier": "janvier",
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

        self.options_de_la_fenetre()
        self.connexion_des_widgets()

    # ==============================
    def options_de_la_fenetre(self):
        """
            Méthode qui permet de configurer certaines options pour la fenêtre
        """

        self.l_mois.setEnabled(False)
        self.CB_mois.setEnabled(False)

    # ==================================
    def gestion_choix_utilisateur(self):
        """
            Méthode qui permet de récupérer le choix de l'utilisateur,
            de remplir la QComboBox CB_mois,
            de mettre en forme le QButton B_choix,
            d'activer/de désactiver les QWidgets relatifs à la sélection du mois
        """

        # Récupération du choix de l'utilisateur
        self._choix_utilisateur = self._dico_choix_utilisateur[self._choix_utilisateur]

        # Le choix de l'utilisateur est à True : l'utilisateur souhaite utiliser des données de l'année en cours
        if self._choix_utilisateur:

            # Activation des QWidgets relatifs à la sélection du mois
            self.l_mois.setEnabled(True)
            self.CB_mois.setEnabled(True)

            # Mise-en-forme du QButton B_choix
            self.B_choix.setText("OUI")
            self.B_choix.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0.948864, x2:1, y2:0, stop:0 rgba(0, 255, 0, 255), stop:1 rgba(255, 255, 255, 255)); border-radius: 4px;")

            # Remplissage du QComboBox CB_mois

                # Initialisation
            self._liste_des_mois_contenant_des_donnees = []

                # On itère sur la liste des mois
            for indice, mois in enumerate(self._liste_des_mois):

                # On extrait, des données, un sous-set de données pour le mois et les catégories prelevements et epargnes
                self._extrait_donnees_prelevements = self._donnees[mois]["prelevements"]
                self._extrait_donnees_epargnes = self._donnees[mois]["epargnes"]

                # Si le sous-set de données n'est pas vide on ajoute le mois en cours à la liste des mois contenant des données
                if len(self._extrait_donnees_prelevements) > 0 and len(self._extrait_donnees_epargnes) > 0:

                    self._liste_des_mois_contenant_des_donnees.append(self._dico_des_mois_simple_vers_complexe[mois])

                # Nettoyage du QComboBox avant d'ajouter les éléments
            self.CB_mois.clear()

                # Ajout des éléments au QComboBox
            self.CB_mois.addItems(self._liste_des_mois_contenant_des_donnees)

        # Le choix de l'utilisateur est à False : l'utilisateur souhaite une année sans données
        else:

            # Désactivation des QWidgets relatifs à la sélection du mois
            self.l_mois.setEnabled(False)
            self.CB_mois.setEnabled(False)

            # Mise-en-forme du QButton B_choix
            self.B_choix.setText("NON")
            self.B_choix.setStyleSheet("")

            # Nettoyage du QComboBox CB_mois
            self.CB_mois.clear()

    # =============================
    def fenetre_confirmation(self):
        """
            Méthode qui permet d'ouvrir une fenêtre demandant à l'utilisateur de confirmer/d'annuler l'écrasement du fichier de la nouvelle année
        """

        # Création de la fénêtre
        self._fenetre_confirmation = QtGui.QMessageBox()

        # Paramétrage de la fenêtre
        self._fenetre_confirmation.setWindowTitle("Confirmation")
        self._fenetre_confirmation.setText(
            "Le fichier {} existe déjà.\nVoulez-vous l'écraser ?".format(self._nom_du_fichier))
        self._fenetre_confirmation.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        self._fenetre_confirmation.setDefaultButton(QtGui.QMessageBox.No)
        self._fenetre_confirmation.setIcon(QtGui.QMessageBox.Warning)

        # Lancement de la fenêtre
        self._choix_confirmation = self._fenetre_confirmation.exec_()

    # ====================
    def creer_annee(self):
        """
            Méthode qui permet de créer le fichier de données pour l'année suivante
        """


        # morceler cette méthode en plusieurs méthodes ???


        # Récupération du chiffre de l'année actuelle et calcul de celui de la nouvelle année
        annee_actuelle = self._donnees["annee"]
        nouvelle_annee = int(annee_actuelle) + 1

        # Récupération de la date du jour pour la définition de la date de mise-à-jour des nouvelles données
        date_du_jour = datetime.now()

        # Modification de la date de mise-à-jour des données
        date_du_jour_formatee = datetime.strftime(date_du_jour, "%d/%m/%Y")

        # Définition du nom du fichier pour la nouvelle année
        self._nom_du_fichier = "Donnees_" + str(nouvelle_annee) + ".json"
        emplacement_du_fichier = os.path.join(self._emplacement_du_dossier_des_donnees, self._nom_du_fichier)

        # Initialisation pour l'écriture du fichier
        ecriture = False

        # Vérification de l'existence du ficher à créer

        if os.path.isfile(emplacement_du_fichier):
            # le ficheir a créer existe déjà : on demande à l'utilisateur s'il souhaite écraser le fichier existant

            # Ouverture de la fenêtre de confirmation
            self.fenetre_confirmation()

            # Gestion du choix du joueur via la fenêtre de confirmation
            if self._choix_confirmation == QtGui.QMessageBox.Yes:

                ecriture = True

        else:
            # le ficheir a créer n'existe pas : il faut le créer

            ecriture = True

        # Ecriture du fichier contenant les données pour la nouvelle annee
        if ecriture:

            self._donnees_a_ecrire = {}
            self._donnees_a_ecrire["annee"] = nouvelle_annee
            self._donnees_a_ecrire["date_de_mise_a_jour"] = date_du_jour_formatee

            # Si l'utilisateur souhaite utiliser des données de l'année actuelle on récupère le mois concerné dans la QComboBox
            if self._choix_utilisateur:

                mois_selectionne = str(self.CB_mois.currentText())
                cle_mois_selectionne = self._dico_des_mois_complexe_vers_simple[mois_selectionne]
                self._donnees_a_ecrire["janvier"] = self._donnees[cle_mois_selectionne]

            # Sinon on initialise le mois de Janvier de l'année suivante avec des catégories vides
            else:

                self._donnees_a_ecrire["janvier"] = { "montant_paye": 0.0,
                                                      "prelevements": [],
                                                      "epargnes": [],
                                                      "depenses": []
                                                    }

            # Enregistrement des données dans le fichier de la nouvelle année
            self._instance_d_enregistrement_des_resultats = EnregistrementDesDonnees(emplacement_du_fichier, self._donnees_a_ecrire)
            self._instance_d_enregistrement_des_resultats.enregistrement()

            # Signal pour fermer la fenêtre
            self.accept()

    # ==============================
    def connexion_des_widgets(self):
        """
            Méthode qui permet de connecter les widgets
        """

        self.B_choix.clicked.connect(self.gestion_choix_utilisateur)
        self.B_creer.clicked.connect(self.creer_annee)

# =================================================================================================
# Utilisation
# =================================================================================================

if __name__ == "__main__":

    print("Je ne tourne pas seul !")
