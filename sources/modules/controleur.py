﻿# coding: utf-8

""" Module qui contient la classe Controleur pour Y """

# =================================================================================================
# Paramètres globaux
# =================================================================================================

__author__ = "Julien LEPAIN"
__version__ = 1.0


# =================================================================================================
# Import des librairies
# =================================================================================================

# Import des librairies graphiques
from PyQt4 import QtGui, QtCore
import GUI_Application as GUI_Application

# Import des librairies qui contiennent le modèle
from lecture_fichier_JSON import LectureFichierJSON
from modele_prelevements import ModelePrelevements
from modele_epargnes import ModeleEpargnes
from modele_depenses import ModeleDepenses, ComboBoxDelegate
from fenetre_intermediaire_pour_les_outils import FenetreIntermediairePourLesOutils
from enregistrement_des_donnees import EnregistrementDesDonnees
from ajout_de_lignes import AjoutDeLignes
from ajout_de_lignes_depenses import AjoutDeLignesDepenses
from dupliquer_donnees_mois import DupliquerDonneesMois
from creer_nouvelle_annee import CreerNouvelleAnnee
from envoi_mail import EnvoiMail
import sous_classement_des_qvalidators as sous_classement_des_qvalidators
from message_d_information import AffichageMessage

# Import des autres librairies
import sys
import os
import shutil
from datetime import datetime


# =================================================================================================
# Classes
# =================================================================================================

# =================================================================
class Controleur(QtGui.QMainWindow, GUI_Application.Ui_MainWindow):
    """
        Classe de lien entre la Vue et le Modèle
    """

    # ===================================
    def __init__(self, app, parent=None):
        """
            Constructeur de la classe
        """
        
        super(Controleur, self).__init__(parent)
        self.setupUi(self)
        
        # Liste des attrbibuts
        
        self._fenetre_intermediaire = None

        self._donnees = None

        self._modele_prelevements = None
        self._modele_epargnes = None
        self._modele_depenses = None
        
        self._liste_des_categories = [ "prelevements",
                                       "epargnes",
                                       "depenses"
                                     ]

        self._liste_des_mois = ["janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre",
                                "decembre"]

        self._dico_liste_des_mois = {  1: "janvier",
                                       2: "fevrier",
                                       3: "mars", 
                                       4: "avril", 
                                       5: "mai",
                                       6: "juin",
                                       7: "juillet",
                                       8: "aout",
                                       9: "septembre",
                                      10: "octobre",
                                      11: "novembre",
                                      12: "decembre"
                                    }
        
        self._dico_des_modeles = { "prelevements": None,
                                   "epargnes": None,
                                   "depenses": None
                                 }
        
        self._categorie_affichee = ""
        
        self._dico_boutons_categories = { "prelevements": self.B_prelevements,
                                          "epargnes": self.B_epargne,
                                          "depenses": self.B_depenses
                                        }
        
        self._dico_boutons_mois = { 1: self.B_janvier,
                                    2: self.B_fevrier,
                                    3: self.B_mars,
                                    4: self.B_avril,
                                    5: self.B_mai,
                                    6: self.B_juin,
                                    7: self.B_juillet,
                                    8: self.B_aout,
                                    9: self.B_septembre,
                                   10: self.B_octobre,
                                   11: self.B_novembre,
                                   12: self.B_decembre
                                  }
        
        self._modification_du_statut = { True: False,
                                         False: True
                                       }
        
        self._type_de_fichier = ""
        
        self._nom_du_fichier_de_configuration = "Configuration.json"
        self._emplacement_absolu_du_fichier_de_configuration = os.path.join(os.path.abspath("../../donnees"), self._nom_du_fichier_de_configuration)

        self._emplacement_du_dossier_des_donnees = os.path.abspath("../../donnees")

        # Liste des méthodes pour initialisation
        
        self.initialisation()
        
    # ====================
    def get_donnees(self):
        """
            Accesseur de l'attribut _donnees

            :return:
            :rtype:
        """

        return self._donnees

    # ============================
    def set_donnees(self, valeur):
        """
            Mutateur de l'attribut _donnees

            :ivar
            :type
        """

        self._donnees = valeur

    # ===============================================
    def get_emplacement_du_dossier_des_donnees(self):
        """
            Accesseur de l'attribut _emplacement_du_dossier_des_donnees

            :return:
            :rtype:
        """

        return self._emplacement_du_dossier_des_donnees

    # =======================
    def initialisation(self):
        """
            Méthode qui permet d'initialiser certains paramètres de la GUI
        """
        
        # Affichage en plein écran
        self.showFullScreen()
        
        # Chargement du fichier de configuration
        self.chargement_du_fichier_de_configuration()
        
        # Chargement des données
        self.chargement_des_donnees()
        
        # Récupération de la date du jour et définition du mois à afficher (pour l'affichage lors de l'ouverture de l'appli)
        self._date_du_jour = datetime.now()
        self._mois_a_afficher = self._dico_liste_des_mois[self._date_du_jour.month]
        
        # Définition des modèles
        self._dico_des_modeles["prelevements"] = ModelePrelevements(self._donnees[self._mois_a_afficher]["prelevements"])
        self._dico_des_modeles["epargnes"] = ModeleEpargnes(self._donnees[self._mois_a_afficher]["epargnes"])
        self._dico_des_modeles["depenses"] = ModeleDepenses(self._donnees[self._mois_a_afficher]["depenses"])
        
        # Création des actions
        self.creation_des_actions()
        
        # Connexion des widgets
        self.connexion_des_widgets()
        
        # Affichages par défaut lors de l'ouverture de l'appli
        self._categorie_affichee = "depenses"
        self.definition_du_mois_a_afficher(self._date_du_jour.month)
        
    # ==========================================
    def mise_a_jour_du_montant_de_la_paye(self):
        """
            Méthode qui permet de mettre à jour le QLineEdit contenant le montant de la paye du mois en cours
        """
        
        # Mise-à-jour du QLineEdit LE_montant_paye
        self.LE_montant_paye.setText(str(self._donnees[self._mois_a_afficher]["montant_paye"]))
        
        # Désactivation du mode édition du QLineEdit
        self.LE_montant_paye.setReadOnly(True)
        
    # =====================================
    def mise_a_jour_montant_depenses(self):
        """
            Méthode qui permet de mettre à jour le QLineEdit contenant les dépenses du mois en cours
        """
        
        # Mise-à-jour des modèles
        self._dico_des_modeles["depenses"].set_donnees(self._donnees[self._mois_a_afficher]["depenses"])
        
        # Calcul de la somme pour les dépenses
        self._dico_des_modeles["depenses"].calculer_la_somme_des_depenses()
        
        # Mise-à-jour du QLineEdit LE_depenses
        self.LE_depenses.setText(str(self._dico_des_modeles["depenses"].somme_des_depenses))

    # ==================================
    def mise_a_jour_montant_reste(self):
        """
            Méthode qui permet de mettre à jour le QLineEdit contenant les dépenses du mois en cours
        """
        
        # Mise-à-jour des modèles
        
        self._dico_des_modeles["prelevements"].set_donnees(self._donnees[self._mois_a_afficher]["prelevements"])
        self._dico_des_modeles["epargnes"].set_donnees(self._donnees[self._mois_a_afficher]["epargnes"])
        
        # Calcul des sommes pour les prélèvements et les épargnes
        
        self._dico_des_modeles["prelevements"].calculer_la_somme_des_prelevements()
        self._dico_des_modeles["epargnes"].calculer_la_somme_des_epargnes()
        
        # Calcul du reste
        
        self._reste = self._donnees[self._mois_a_afficher]["montant_paye"] - self._dico_des_modeles["prelevements"].somme_des_prelevements - self._dico_des_modeles["epargnes"].somme_des_epargnes - self._dico_des_modeles["depenses"].somme_des_depenses
        
        # Mise-en-forme du QLineEdit LE_reste en fonction du reste calculé
        
        if self._reste < 0:
        # Si le reste est négatif on colorie le fond
            
            self.LE_reste.setStyleSheet("background-color: rgb(255,50,0)")
            
        else:
        # Sinon on ne fait rien
            
            self.LE_reste.setStyleSheet("background-color: None")
            
        
        # On modifie l'affichage du QLineEdit LE_reste
        
        self.LE_reste.setText(str(self._reste))

    # ===============================================
    def chargement_du_fichier_de_configuration(self):
        """
            Méthode qui permet de charger le contenu du fichier de configuration
        """
        
        # Chargement du fichier de configuration
        
        self._type_de_fichier = "configuration"
        self._fichier_de_configuration = LectureFichierJSON(self._emplacement_absolu_du_fichier_de_configuration, self._type_de_fichier)
        self._fichier_de_configuration.lecture_du_fichier()
        self._contenu_du_fichier_de_configuration = self._fichier_de_configuration.get_contenu_du_fichier()
        
        # Récupération du nom du fichier contenant les données
        
        self._nom_du_fichier_de_donnees = self._contenu_du_fichier_de_configuration["fichier_contenant_les_donnees"]
        self._emplacement_absolu_du_fichier_de_donnees = os.path.join(self._emplacement_du_dossier_des_donnees, self._nom_du_fichier_de_donnees)

    # ===============================
    def chargement_des_donnees(self):
        """
            Méthode de chargement des données
        """
        
        self._type_de_fichier = "donnees"
        self._lecture_donnees = LectureFichierJSON(self._emplacement_absolu_du_fichier_de_donnees, self._type_de_fichier)
        self._lecture_donnees.lecture_du_fichier()
        self._donnees = self._lecture_donnees.get_contenu_du_fichier()

    # ===================================
    def mise_a_jour_de_l_affichage(self):
        """
            Méthode qui permet de mettre à jour l'affichage
        """
        
        # Mise-à-jour du montant de la paye du mois en cours
        
        self.mise_a_jour_du_montant_de_la_paye()

        # Mise-à-jour du montant des dépenses du mois en cours
        
        self.mise_a_jour_montant_depenses()
        
        # Mise-à-jour du montant du reste du mois en cours
        
        self.mise_a_jour_montant_reste()

    # ============================================
    def definition_du_mois_a_afficher(self, mois):
        """
            Méthode qui permet de déterminer le mois à afficher
        """
        
        # Récupération du mois à afficher sous forme de chaîne de caractères
        
        self._mois_a_afficher = self._dico_liste_des_mois[mois]
        
        # Mise-en-forme du bouton du mois sélectionné
        
        self.mise_en_forme_du_bouton_du_mois_selectionne(mois)
        
        # Connexion du modèle
        
        self.connexion_du_modele(self._categorie_affichee)
        
        # Mise-à-jour de l'affichage
        
        self.mise_a_jour_de_l_affichage()

    # ==========================================================
    def mise_en_forme_du_bouton_du_mois_selectionne(self, mois):
        """
            Méthode qui permet de mettre en forme le bouton du mois sélectionné
        """
        
        for cle in self._dico_boutons_mois.keys():
        # on parcourt les clé du dictionnaire qui contient les références des boutons des mois
            
            if cle == mois:
            # si la clé correspond au bouton qui a été cliqué on colorie ce bouton en un dégradé de orange et on arrondi ses angles
                
                self._dico_boutons_mois[cle].setStyleSheet("background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.511, radius:1.506, fx:0.4995, fy:0.512, stop:0 rgba(255, 102, 0, 255), stop:1 rgba(255, 255, 255, 255)); border-radius: 10px;")
                
            else:
            # sinon on revient au style par défaut
                
                self._dico_boutons_mois[cle].setStyleSheet("background-color: None")

    # =======================================
    def connexion_du_modele(self, categorie):
        """
            Méthode qui permet d'utiliser le modèle passé en argument (categorie) pour l'affichage des données dans l'IHM
        """
        
        # Connexion du modèle passé en argument
        
        self._categorie_affichee = categorie
        
        # Mise-à-jour des modèles selon le mois sélectionné

        self._dico_des_modeles[self._categorie_affichee].set_donnees(self._donnees[self._mois_a_afficher][self._categorie_affichee])

        # Définition, paramétrage et affectation des QValidator pour les cellules

        self.TV_affichage.setItemDelegate(sous_classement_des_qvalidators.SCItemDelegateTVAffichage(self._categorie_affichee, -5000.0, 5000.0, 3))

        # Mise-à-jour de l'affichage
        
        self.TV_affichage.setModel(self._dico_des_modeles[self._categorie_affichee])

        if self._categorie_affichee in ["depenses"]:

            self.cbd = ComboBoxDelegate()
            self.TV_affichage.setItemDelegateForColumn(3, self.cbd)

        # Personnalisation des boutons : mise-en-forme particulière du bouton qui a été cliqué
        
        for cle in self._dico_boutons_categories.keys():
        # on parcourt les clé du dictionnaire qui contient les références des boutons des catégories
            
            if cle in self._categorie_affichee:
            # si la clé correspond au bouton qui a été cliqué on colorie ce bouton en un dégradé de vert et on arrondi ses angles
                
                self._dico_boutons_categories[cle].setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0.948864, x2:1, y2:0, stop:0 rgba(0, 255, 0, 255), stop:1 rgba(255, 255, 255, 255)); border-radius: 10px;")
                
            else:
            # sinon on revient au style par défaut
                
                self._dico_boutons_categories[cle].setStyleSheet("background-color: None")

    # =======================================
    def mise_a_jour_donnees(self, categorie):
        """
            Méthode qui permet de mettre-à-jour les données en récupérant celles du modèle passé en argument
        """
        
        # mise-à-jour des données récupérées dans le modèle
        self._donnees[self._mois_a_afficher][categorie] = self._dico_des_modeles[categorie].get_donnees()
        
        # mise-à-jour de l'affichage
        self.mise_a_jour_de_l_affichage()

    # ==============================
    def connexion_des_widgets(self):
        """
            Méthode qui permet de connecter les widgets
        """
        
        # Connexion des boutons des mois

        self.B_janvier.clicked.connect(lambda: self.definition_du_mois_a_afficher(1))
        self.B_fevrier.clicked.connect(lambda: self.definition_du_mois_a_afficher(2))
        self.B_mars.clicked.connect(lambda: self.definition_du_mois_a_afficher(3))
        self.B_avril.clicked.connect(lambda: self.definition_du_mois_a_afficher(4))
        self.B_mai.clicked.connect(lambda: self.definition_du_mois_a_afficher(5))
        self.B_juin.clicked.connect(lambda: self.definition_du_mois_a_afficher(6))
        self.B_juillet.clicked.connect(lambda: self.definition_du_mois_a_afficher(7))
        self.B_aout.clicked.connect(lambda: self.definition_du_mois_a_afficher(8))
        self.B_septembre.clicked.connect(lambda: self.definition_du_mois_a_afficher(9))
        self.B_octobre.clicked.connect(lambda: self.definition_du_mois_a_afficher(10))
        self.B_novembre.clicked.connect(lambda: self.definition_du_mois_a_afficher(11))
        self.B_decembre.clicked.connect(lambda: self.definition_du_mois_a_afficher(12))
        
        # Connexion des boutons liés au type des données : Prélèvement, Epargne et Dépenses
        
        self.B_prelevements.clicked.connect(lambda: self.connexion_du_modele("prelevements"))
        self.B_epargne.clicked.connect(lambda: self.connexion_du_modele("epargnes"))
        self.B_depenses.clicked.connect(lambda: self.connexion_du_modele("depenses"))
        
        # Connexion du menu contextuel pour le TV_affichage

        # Permet de spécifier que le menu contextuel sera un menu personnalisé
        self.TV_affichage.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        
        # Permet de lier l'action du clic droit à l'appel du menu contextuel qui sera défini via la méthode "menu_contextuel"
        self.TV_affichage.customContextMenuRequested.connect(self.creation_menu_contextuel_TV_affichage)
        
        # Connexion du menu contextuel pour la mise-à-jour du montant de la paye

        # Permet de spécifier que le menu contextuel sera un menu personnalisé
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        
        # Permet de lier l'action du clic droit à l'appel du menu contextuel qui sera défini via la méthode "menu_contextuel"
        self.customContextMenuRequested.connect(self.creation_menu_contextuel_modification_montant_paye)
        
        # Connexion des signaux de changement des données des modèles

        self._dico_des_modeles["prelevements"].dataChanged.connect(lambda: self.mise_a_jour_donnees("prelevements"))
        self._dico_des_modeles["epargnes"].dataChanged.connect(lambda: self.mise_a_jour_donnees("epargnes"))
        self._dico_des_modeles["depenses"].dataChanged.connect(lambda: self.mise_a_jour_donnees("depenses"))

        # Mise en place du QValidator pour le QLineEdit contenant le montant de la paye
        self._validateur_pour_montant_paye = sous_classement_des_qvalidators.SCQDoubleValidation(0.0, 10000.0)
        self._validateur_pour_montant_paye.setDecimals(3)
        self.LE_montant_paye.setValidator(self._validateur_pour_montant_paye)

    # ========================
    def lancement_outils(self):
        """
            Méthode qui permet de lancer l'interface qui gère les outils
        """
        
        self._fenetre_intermediaire = FenetreIntermediairePourLesOutils(self)
        self._fenetre_intermediaire.exec_()

    # =============================
    def creation_des_actions(self):
        """
            Méthode qui permet de créer et gérer des actions
        """
        
        # Création de l'action liée à l'affichage des outils
        
        # Création d'une action associée aux outils
        self._actionOutils = QtGui.QAction("Outils", self)
        
        # Assignation du raccourci clavier "Ctrl + O" à cette action
        self._actionOutils.setShortcut("Ctrl+O")
        
        # Connection de l'action à la méthode "lancement_outils"
        self._actionOutils.triggered.connect(self.lancement_outils)
        
        # Ajout de l'action à un widget : ici c'est l'application elle-même
        # --- en effet, chaque action doit être ajoutée à un widget avant de pouvoir être utilisée
        # -- dans le cas présent, i.e. l'utilisation d'un raccourci clavier, c'est nécessaire
        self.addAction(self._actionOutils)
        

        # Création de l'action liée à la modification du statut, action qui va être liée au menu contextuel lié au TV_affichage
        
        # Création de l'action intitulée "_actionModificationStatut"
        self._actionModificationStatut = QtGui.QAction("Modifier le statut", self)

        # Ajout d'un icône à l'action
        icone_modification_statut = QtGui.QIcon()
        icone_modification_statut.addPixmap(QtGui.QPixmap("../../icones/icone_modification_statut_32_x_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._actionModificationStatut.setIcon(icone_modification_statut )

        # Connection de l'action à la méthode "modification_du_statut"
        self._actionModificationStatut.triggered.connect(self.modification_du_statut)
        
        # Ajout de l'action à un widget : ici c'est l'application elle-même
        self.addAction(self._actionModificationStatut)
        

        # Création de l'action liée à la supression de lignes, action qui va être liée au menu contextuel lié au TV_affichage
        
        # Création de l'action intitulée "_actionSuppressionLignes"
        self._actionSuppressionLignes = QtGui.QAction(u"Supprimer des lignes", self)

        # Ajout d'un icône à l'action
        icone_suppression_lignes = QtGui.QIcon()
        icone_suppression_lignes.addPixmap(QtGui.QPixmap("../../icones/icone_suppression_ligne_32_x_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._actionSuppressionLignes.setIcon(icone_suppression_lignes)

        # Connection de l'action à la méthode "supprimer_des_lignes"
        self._actionSuppressionLignes.triggered.connect(self.supprimer_des_lignes)
        
        # Ajout de l'action à un widget : ici c'est l'application elle-même
        self.addAction(self._actionSuppressionLignes)
        
        
        # Création de l'action liée à la modification du montant de la paye, action qui va être liée au menu contextuel de la fenêtre
        
        # Création de l'action intitulée "_actionModificationMontantPaye"
        self._actionModificationMontantPaye = QtGui.QAction(u"Modification du montant de la paye", self)

        # Ajout d'un icône à l'action
        icone_modification_montant_paye = QtGui.QIcon()
        icone_modification_montant_paye.addPixmap(QtGui.QPixmap("../../icones/icone_modification_montant_32_x_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._actionModificationMontantPaye.setIcon(icone_modification_montant_paye)

        # Connection de l'action à la méthode "modification_du_montant_de_la_paye"
        self._actionModificationMontantPaye.triggered.connect(self.etapes_prealables_a_la_modification_du_montant_de_la_paye)
        
        # Ajout de l'action à un widget : ici c'est l'application elle-même
        self.addAction(self._actionModificationMontantPaye)
        
        
        # Création de l'action liée à l'enregistrement des données, action qui va être liée au menu contextuel de la fenêtre
        
        # Création de l'action intitulée "_actionEnregistrement"
        self._actionEnregistrement = QtGui.QAction(u"Enregistrer les résultats", self)

        # Assignation du raccourci clavier "Ctrl + S" à cette action
        # self._actionEnregistrement.setShortcut("Ctrl+S")              --> désactivé pour le moment

        # Connection de l'action à la méthode "enregistrement_des_resultats"
        self._actionEnregistrement.triggered.connect(self.enregistrement_des_donnees)
        
        # Ajout de l'action à un widget : ici c'est l'application elle-même
        self.addAction(self._actionEnregistrement)
        
        
        # Création de l'action liée à l'ajout de lignes, action qui va être liée au menu contextuel lié au TV_affichage
        
        # Création de l'action intitulée "_actionAjoutLignes"
        self._actionAjoutLignes = QtGui.QAction(u"Ajouter des lignes", self)

        # Ajout d'un icône à l'action
        icone_ajout_lignes = QtGui.QIcon()
        icone_ajout_lignes.addPixmap(QtGui.QPixmap("../../icones/icone_ajout_ligne_32_x_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._actionAjoutLignes.setIcon(icone_ajout_lignes)

        # Connection de l'action à la méthode "ajouter_des_lignes"
        self._actionAjoutLignes.triggered.connect(self.ajouter_des_lignes)
        
        # Ajout de l'action à un widget : ici c'est l'application elle-même
        self.addAction(self._actionAjoutLignes)


        # Changement de catégorie/mois

        self._changer_de_categorie_gauche = QtGui.QAction("Changer de catégorie", self)
        self._changer_de_categorie_gauche.setShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_Left))
        self._changer_de_categorie_gauche.triggered.connect(self.changement_categorie_gauche)
        self.addAction(self._changer_de_categorie_gauche)

        self._changer_de_categorie_droite = QtGui.QAction("Changer de catégorie", self)
        self._changer_de_categorie_droite.setShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_Right))
        self._changer_de_categorie_droite.triggered.connect(self.changement_categorie_droite)
        self.addAction(self._changer_de_categorie_droite)

        self._changer_de_mois_haut = QtGui.QAction("Changer de catégorie", self)
        self._changer_de_mois_haut.setShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_Up))
        self._changer_de_mois_haut.triggered.connect(self.changement_mois_haut)
        self.addAction(self._changer_de_mois_haut)

        self._changer_de_mois_bas = QtGui.QAction("Changer de catégorie", self)
        self._changer_de_mois_bas.setShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_Down))
        self._changer_de_mois_bas.triggered.connect(self.changement_mois_bas)
        self.addAction(self._changer_de_mois_bas)

    # ================================
    def changement_de_categorie(self):
        """
            Méthode qui permet de changer la catégorie à afficher lorsque l'utilisateur à utilisé un raccourci clavier
        """

        self.connexion_du_modele(self._liste_des_categories[self._numero_categorie_a_afficher])

    # ====================================
    def changement_categorie_gauche(self):
        """
            Méthode qui permet de changer la catégorie à afficher lorsque l'utilisateur à utilisé la raccourci clavier Ctrl + flèche de gauche
        """

        numero_categorie_affichee = self._liste_des_categories.index(self._categorie_affichee)

        if numero_categorie_affichee == 0:

            self._numero_categorie_a_afficher = 2

        else:

            self._numero_categorie_a_afficher = numero_categorie_affichee - 1

        self.changement_de_categorie()

    # ====================================
    def changement_categorie_droite(self):
        """
            Méthode qui permet de changer la catégorie à afficher lorsque l'utilisateur à utilisé la raccourci clavier Ctrl + flèche de droite
        """

        numero_categorie_affichee = self._liste_des_categories.index(self._categorie_affichee)

        if numero_categorie_affichee == 2:

            self._numero_categorie_a_afficher = 0

        else:

            self._numero_categorie_a_afficher = numero_categorie_affichee + 1

        self.changement_de_categorie()

    # ===========================
    def changement_de_mois(self):
        """
            Méthode qui permet de changer le mois à afficher lorsque l'utilisateur à utilisé un raccourci clavier
        """

        self.definition_du_mois_a_afficher(self._numero_mois_a_afficher)

    # =============================
    def changement_mois_haut(self):
        """
            Méthode qui permet de changer le mois à afficher lorsque l'utilisateur à utilisé la raccourci clavier Ctrl + flèche du haut
        """

        numero_mois_affiche = self._liste_des_mois.index(self._mois_a_afficher) + 1

        if numero_mois_affiche == 1:

            self._numero_mois_a_afficher = 12

        else:

            self._numero_mois_a_afficher = numero_mois_affiche - 1

        self.changement_de_mois()

    # ============================
    def changement_mois_bas(self):
        """
            Méthode qui permet de changer le mois à afficher lorsque l'utilisateur à utilisé la raccourci clavier Ctrl + flèche du bas
        """

        numero_mois_affiche = self._liste_des_mois.index(self._mois_a_afficher) + 1

        if numero_mois_affiche == 12:

            self._numero_mois_a_afficher = 1

        else:

            self._numero_mois_a_afficher = numero_mois_affiche + 1

        self.changement_de_mois()

    # ==================================================
    @QtCore.pyqtSlot(str)
    def recuperation_de_la_ligne_a_inserer(self, texte):
        """
            Méthode qui permet de mettre à jour les données de la catégorie sélectionnée
            avec les informations renseignées via la fenêtre d'insertion de ligne
        """

        elements_a_inserer = { "titre": texte.split('\t')[0],
                               "montant": float(texte.split('\t')[1]),
                               "statut": False }

        self._donnees[self._mois_a_afficher][self._categorie_affichee].insert(0, elements_a_inserer)
        self.mise_a_jour_donnees(self._categorie_affichee)

    # ===========================================================
    @QtCore.pyqtSlot(str)
    def recuperation_de_la_ligne_a_inserer_depenses(self, texte):
        """
            Méthode qui permet de mettre à jour les données de la catégorie dépenses
            avec les informations renseignées via la fenêtre d'insertion de ligne
        """

        elements_a_inserer = { "date": texte.split('\t')[0],
                               "titre": texte.split('\t')[1],
                               "montant": float(texte.split('\t')[2]),
                               "moyen_de_paiement": texte.split('\t')[3],
                               "statut": False}

        self._donnees[self._mois_a_afficher]["depenses"].insert(0, elements_a_inserer)
        self.mise_a_jour_donnees(self._categorie_affichee)

    # ========================
    def ajout_de_lignes(self):
        """
            Méthode qui permet d'ajouter des lignes dans le TV affichage pour la catégorie prelevements ou epargnes
        """
        
        self._instance_d_ajout_de_lignes = AjoutDeLignes(self._categorie_affichee)
        self._instance_d_ajout_de_lignes.elements_a_inserer.connect(self.recuperation_de_la_ligne_a_inserer)
        self._instance_d_ajout_de_lignes.main()

    # =================================
    def ajout_de_lignes_depenses(self):
        """
            Méthode qui permet d'ajouter des lignes dans le TV affichage pour la catégorie depenses
        """
        
        self._instance_d_ajout_de_lignes = AjoutDeLignesDepenses()
        self._instance_d_ajout_de_lignes.elements_a_inserer.connect(self.recuperation_de_la_ligne_a_inserer_depenses)
        self._instance_d_ajout_de_lignes.main()

    # ===========================
    def ajouter_des_lignes(self):
        """
            Méthode qui permet d'ajouter des lignes dans le TV affichage pour le mois en cours et pour la catégorie sélectionnée
            Si la catégorie sélectionnée est Prélèvements ou Epargnes la fenêtre qui sera chargée sera GUI_Ajout_de_lignes
            Si la catégorie sélectionnée est Dépenses la fenêtre qui sera chargée sera GUI_Ajout_de_lignes_depenses
        """
        
        if self._categorie_affichee in ["prelevements", "epargnes"]:
            
            self.ajout_de_lignes()
            
        elif self._categorie_affichee in ["depenses"]:
            
            self.ajout_de_lignes_depenses()

    # =====================================
    def enregistrement_des_donnees(self):
        """
            Méthode qui permet d'enregistrer les données
        """
        
        self._enregsitrement_des_donnees = EnregistrementDesDonnees(self._emplacement_absolu_du_fichier_de_donnees, self._donnees)
        self._enregsitrement_des_donnees.enregistrement()

        message = "Les données ont été enregistrées"
        self.__essai = AffichageMessage(message)
        self.__essai.exec_()

    # ===============================================
    def envoi_d_une_copie_des_donnees_par_mail(self):
        """
            Méthode qui permet d'envoyer, par mail, une copie du fichier contenant les données
        """

        expediteur = self._contenu_du_fichier_de_configuration["expediteur"]
        destinataire = self._contenu_du_fichier_de_configuration["destinataire"]
        liste_des_fichiers_a_envoyer = [self._emplacement_absolu_du_fichier_de_donnees]

        self._instance_envoi_copie_par_mail = EnvoiMail(expediteur, destinataire, liste_des_fichiers_a_envoyer)
        self._instance_envoi_copie_par_mail.envoi_du_mail()

        message = "Une copie du ficher contenant les données a été envoyée par mail"
        self.__essai = AffichageMessage(message)
        self.__essai.exec_()

    # =====================================
    def creation_d_une_copie_back_up(self):
        """
            Méthode qui permet de créer une copie back up du fichier contenant les données
        """

        self._nom_de_la_copie_du_fichier_de_donnees = os.path.basename(self._emplacement_absolu_du_fichier_de_donnees.split(".")[0] + \
                                                      "_" + \
                                                      datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + \
                                                      "." + \
                                                      os.path.basename(self._emplacement_absolu_du_fichier_de_donnees.split(".")[1]))

        self._emplacement_absolu_de_la_copie_du_fichier_de_donnees = os.path.join(self._contenu_du_fichier_de_configuration["emplacement_absolu_du_dossier_de_back_up"], self._nom_de_la_copie_du_fichier_de_donnees)

        try:
            # On essaye de déplacer le fichier renommé dans le répertoire de destination

            shutil.copy(self._emplacement_absolu_du_fichier_de_donnees, self._emplacement_absolu_de_la_copie_du_fichier_de_donnees)

        except OSError:
            # Il y a eu un problème lors du déplacement du fichier renommé

            message = ("Problème lors du déplacement du fichier : {}"
                       "anciennement : {}"
                       "dans le dossier : {}").format(self._nom_de_la_copie_du_fichier_de_donnees,
                                                       self._emplacement_absolu_du_fichier_de_donnees,
                                                       self._contenu_du_fichier_de_configuration["emplacement_absolu_du_dossier_de_back_up"])
            self.__essai = AffichageMessage(message)
            self.__essai.exec_()

        else:
            # Le fichier a bien été déplacé

            message = ("Une copie du ficher contenant les données a été crée dans le dossier :"
                       "{}").format(self._emplacement_absolu_de_la_copie_du_fichier_de_donnees)
            self.__essai = AffichageMessage(message)
            self.__essai.exec_()

    # ======================================
    def importer_des_donnees(self):
        """
            Méthode qui permet d'importer des donénes depuis des fichiers générés par l'applciation des comptes
        """

        # fichier_a_importer = str(QtGui.QFileDialog.getOpenFileName(filter=self._filtre_fichier_a_importer))           - - - à finir - - -
        self._fichier_a_importer = str(QtGui.QFileDialog.getOpenFileName(filter="*.json"))

        self._type_de_fichier = "donnees_a_importer"
        self._lecture_fichier_importe = LectureFichierJSON(self._fichier_a_importer, self._type_de_fichier)
        self._lecture_fichier_importe.lecture_du_fichier()

        self._donnees_importees = self._lecture_fichier_importe.get_contenu_du_fichier()

        for indice, ligne in enumerate(self._donnees_importees["donnees"]):

            self._donnees[self._mois_a_afficher]["depenses"].insert(0, ligne)

        self.mise_a_jour_donnees(self._categorie_affichee)

        message = "Les données ont été importées avec succès"
        self.__essai = AffichageMessage(message)
        self.__essai.exec_()

    # ======================================
    def creation_d_une_nouvelle_annee(self):
        """
            Méthode qui permet de créer un fichier pour la nouvelle année
        """

        self._instance_creation_nouvelle_annee = CreerNouvelleAnnee(self)
        self._instance_creation_nouvelle_annee.exec_()

        message = "Le fichier pour la nouvelle année a bien été créé"
        self.__essai = AffichageMessage(message)
        self.__essai.exec_()

    # ==========================================
    def duplication_des_donnees_d_un_mois(self):
        """
            Méthode qui permet de dupliquer les données contenues dans un mois vers un autre mois
        """

        self._instance_duplication_mois = DupliquerDonneesMois(self)
        self._instance_duplication_mois.exec_()

        self.mise_a_jour_de_l_affichage()

        message = "Les données ont bien été dupliquées"
        self.__essai = AffichageMessage(message)
        self.__essai.exec_()

    # ===============================
    def modification_du_statut(self):
        """
            Méthode qui permet de modifier le statut associé à une donnée pour la coloration
        """
        
        # Traitement des cellules sélectionnées
        
        # Récupèration de la liste des cellules sélectionnées
        self._cellules_selectionnees = self.TV_affichage.selectedIndexes()
        
        # On itère sur la liste des cellules sélectionnées et on modifie le statut de la ligne associée
        self.lignes_au_statut_modifies = []
        
        for indice, cellule in enumerate(self._cellules_selectionnees):
            
            if cellule.row() not in self.lignes_au_statut_modifies:
            # si la ligne associée à la cellule actuelle ne figure pas dans la liste des lignes dont le statut a déjà été modifié
                
                self._donnees[self._mois_a_afficher][self._categorie_affichee][cellule.row()]["statut"] = self._modification_du_statut[self._donnees[self._mois_a_afficher][self._categorie_affichee][cellule.row()]["statut"]]
                self.lignes_au_statut_modifies.append(cellule.row())
                
        # On modifie les données du modèle actif
        self._dico_des_modeles[self._categorie_affichee].set_donnees(self._donnees[self._mois_a_afficher][self._categorie_affichee])
        
        # Enlève la sélection
        self.TV_affichage.clearSelection()

    # =========================================
    def fenetre_confirmation_suppression(self):
        """
            Méthode qui permet d'ouvrir une fenêtre demandant à l'utilisateur de confirmer/d'annuler la suppression des lignes/cellules sélectionnées
        """
        
        
        # # # # # # # # # # à mettre dans une classe à part ???
        
        
        # Création de la fénêtre
        self._fenetre_suppression = QtGui.QMessageBox()
        
        # Paramétrage de la fenêtre
        self._fenetre_suppression.setWindowTitle("Confirmation avant suppression")
        self._fenetre_suppression.setText("Voulez-vous supprimer les lignes/cellules sélectionnées ?")
        self._fenetre_suppression.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        self._fenetre_suppression.setDefaultButton(QtGui.QMessageBox.No)
        self._fenetre_suppression.setIcon(QtGui.QMessageBox.Warning)
        
        # Lancement de la fenêtre
        self._choix_confirmation_suppression = self._fenetre_suppression.exec_()

    # =============================
    def supprimer_des_lignes(self):
        """
            Méthode qui permet de supprimer des lignes dans le TV_affichage pour le mois en cours et pour la catégorie sélectionnée
        """
        
        # Création et lancemente de la fenêtre de confirmation de suppression
        
        self.fenetre_confirmation_suppression()
        
        # Traitement si l'utilisateur choisi de confirmer la suppression
        
        if self._choix_confirmation_suppression == QtGui.QMessageBox.Yes:
            
            # Traitement des cellules sélectionnées
            
            # Récupèration de la liste des cellules sélectionnées
            self._cellules_selectionnees = self.TV_affichage.selectedIndexes()
            
            # On itère sur la liste des cellules sélectionnées et on supprime la ligne
            self.nbr_de_suppressions = 0
            self.indices_supprimes = []
            
            for indice, cellule in enumerate(self._cellules_selectionnees):
                
                if cellule.row() not in self.indices_supprimes:
                    
                    del(self._donnees[self._mois_a_afficher][self._categorie_affichee][cellule.row() - self.nbr_de_suppressions])
                    self.indices_supprimes.append(cellule.row())
                    self.nbr_de_suppressions += 1
                    
            # Mise-à-jour des modèles selon le mois sélectionné
            
            self._dico_des_modeles[self._categorie_affichee].set_donnees(self._donnees[self._mois_a_afficher][self._categorie_affichee])
            
            # Connexion du modèle
            
            self.connexion_du_modele(self._categorie_affichee)
            
            # Mise-à-jour de l'affichage

            self.mise_a_jour_de_l_affichage()

    # ============================================================
    def modification_du_montant_de_la_paye_dans_les_donnees(self):
        """
            Méthode qui permet de modifier le montant de la paye pour le mois en cours
        """
        
        # Modification, dans les données du mois en cours, du montant de la paye
        self._donnees[self._mois_a_afficher]["montant_paye"] = float(self.LE_montant_paye.text())
        
        # Mise-à-jour de l'affichage
        self.mise_a_jour_du_montant_de_la_paye()
        
        # Mise-à-jour du reste
        self.mise_a_jour_montant_reste()

    # ==================================================================
    def etapes_prealables_a_la_modification_du_montant_de_la_paye(self):
        """
            Méthode qui permet de réaliser les étapes préalables à la modification du montant de la paye pour le mois en cours
        """
        
        # Activation du mode édition du QLineEdit
        self.LE_montant_paye.setReadOnly(False)
        
        # Connexion du QLineEdit à l'appui sur la touche Entrée
        self.LE_montant_paye.returnPressed.connect(self.modification_du_montant_de_la_paye_dans_les_donnees)

    # ===========================================================
    def creation_menu_contextuel_modification_montant_paye(self):
        """
            Méthode qui permet de définir et de lancer le menu contextuel associé au TableView
        """
        
        # Création d'une instance de menu QMenu
        
        self._menu_contextuel_modification_montant_paye = QtGui.QMenu()
        
        # Ajout d'une action dans le menu contextuel
        
        self._menu_contextuel_modification_montant_paye.addAction(self._actionModificationMontantPaye)
        
        # Lancement du menu contextuel
        
        # Lancement du menu contextuel
        # --- l'option QtGui.QCursor.pos() permet d'ouvrir le menu contextuel à l'emplacement du pointeur
        self._menu_contextuel_modification_montant_paye.exec_(QtGui.QCursor.pos())

    # ==============================================
    def creation_menu_contextuel_TV_affichage(self):
        """
            Méthode qui permet de définir et de lancer le menu contextuel associé au TableView
        """

        # Affichage du menu contextuel seulement si la catégorie sélectionnée pour le mois en cours contient des données

        if len(self._donnees[self._mois_a_afficher][self._categorie_affichee]) > 0:

            # Création d'une instance de menu QMenu

            self._menu_contextuel_TV_affichage = QtGui.QMenu()

            # Ajout d'une action dans le menu contextuel

            self._menu_contextuel_TV_affichage.addAction(self._actionAjoutLignes)
            self._menu_contextuel_TV_affichage.addAction(self._actionModificationStatut)
            self._menu_contextuel_TV_affichage.addAction(self._actionSuppressionLignes)

            # Lancement du menu contextuel

            # Lancement du menu contextuel
            # --- l'option QtGui.QCursor.pos() permet d'ouvrir le menu contextuel à l'emplacement du pointeur
            self._menu_contextuel_TV_affichage.exec_(QtGui.QCursor.pos())

    # =============
    def main(self):
        """
            Main de la classe
        """
        
        self.show()
        

# =================================================================================================
# Utilisation
# =================================================================================================

if __name__ == "__main__":
    
    print("Je ne tourne pas seul !")