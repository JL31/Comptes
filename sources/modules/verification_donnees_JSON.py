# coding: utf-8

""" Module qui contient la classe VerificationDonneesJSON pour Y """


# =================================================================================================
# Paramètres globaux
# =================================================================================================

__author__ = "Julien LEPAIN"
__version__ = 1.0
__all__ = ["VerificationDonneesJSON"]


# =================================================================================================
# Import des librairies
# =================================================================================================

import os
from datetime import datetime


# =================================================================================================
# Classes
# =================================================================================================

# ====================================
class VerificationDonneesJSON(object):
    """
        Classe de vérification du contenu d'un fichier de données au format JSON pour Y
    """

    # =====================================
    def __init__(self, contenu_du_fichier):
        """
            Constructeur de la classe
        """
        
        # Attributs
        
        self._contenu_du_fichier = contenu_du_fichier
        
        self._date_de_mise_a_jour = ""
        self._date_de_mise_a_jour_datetime = None
        self._annee = ""
        
        self._liste_des_cles = None
        self._liste_des_mois = None
        self._liste_des_elements_indice_en_cours = None
        
        self._mois = ["janvier",
                      "fevrier",
                      "mars",
                      "avril",
                      "mai",
                      "juin",
                      "juillet",
                      "aout",
                      "septembre",
                      "octobre", 
                      "novembre",
                      "decembre"]
        
        self._liste_des_elements = {"prelevements": ["titre", "montant", "statut"],
                                    "epargnes": ["titre", "montant", "statut"],
                                    "depenses": ["date", "titre", "montant", "moyen_de_paiement", "statut"]
                                   }
        
        # Appel à la méthode qui va lancer les vérifications
        
        self.verifications()

    # ============================
    @property
    def date_de_mise_a_jour(self):
        """
            Propriété qui permet de récupérer la date de mise-à-jour
        """
        
        return self._date_de_mise_a_jour

    # ============================================
    @property
    def date_de_mise_a_jour_format_datetime(self):
        """
            Propriété qui permet de récupérer la date de mise-à-jour au format datetime
        """
        
        return self._date_de_mise_a_jour_datetime

    # ==============
    @property
    def annee(self):
        """
            Propriété qui permet de récupérer l'année
        """
        
        return self._annee

    # =======================
    @property
    def liste_des_mois(self):
        """
            Propriété qui permet de récupérer la liste des mois
        """
        
        return self._liste_des_mois
        
    # =========================================
    def verification_date_de_mise_a_jour(self):
        """
            Méthode qui permet de vérifier que le fichier contient bien la date de mise-à-jour
        """
        
        try:
            
            self._date_de_mise_a_jour = self._contenu_du_fichier["date_de_mise_a_jour"]
            
        except KeyError:
            
            message_d_erreur = ('La date de mise-à-jour ne figure pas dans le fichier.'
                                'Veuillez le vérifier.'
                                'Pour rappel le fichier doit contenir une ligne selon l\'exemple suivant : "date_de_mise_a_jour":"01/01/2019"')
            raise KeyError(message_d_erreur)
            
        else:
            
            self._date_de_mise_a_jour_datetime = datetime.strptime(self._date_de_mise_a_jour, "%d/%m/%Y")

    # ===========================
    def verification_annee(self):
        """
            Méthode qui permet de vérifier que le fichier contient bien l'année
        """
        
        try:
            
            self._annee = self._contenu_du_fichier["annee"]
            
        except KeyError:
            
            message_d_erreur = ('L\'année ne figure pas dans le fichier.'
                                'Veuillez le vérifier.'
                                'Pour rappel le fichier doit contenir une ligne selon l\'exemple suivant : "annee":2019')
            raise KeyError(message_d_erreur)

    # ==========================================
    def recuperation_de_la_liste_des_mois(self):
        """
            Méthode qui permet de récupérer la liste des mois
        """
        
        self._liste_des_mois = [ cle for indice, cle in enumerate(self._liste_des_cles) if cle not in ["date_de_mise_a_jour", "annee"] ]

    # ==============================
    def verification_des_mois(self):
        """
            Méthode qui permet de vérifier les mois présents dans le fichier
        """
        
        # Récupération des clés dans e contenu du fichier
        self._liste_des_cles = self._contenu_du_fichier.keys()
        
        # Récupération, dans la liste des clés, de celles qui concernent seulement les mois
        self.recuperation_de_la_liste_des_mois()
        
        # Si le nombre de clés, dans la liste précédente, est inférieure à 12 c'est qu'il manque des mois
        # Une nouvelle liste, contenant les mois manquants, est créée
        if len(self._liste_des_mois) < 12:
            
            liste_des_mois_manquants = [ mois for indice, mois in enumerate(self._mois) if mois not in self._liste_des_mois ]
            
        else:
            
            liste_des_mois_manquants = []
            
        # Remplissage par défaut des mois vides
        
        for indice, mois in enumerate(liste_des_mois_manquants):
            
            self._contenu_du_fichier[mois] = {}
            self._contenu_du_fichier[mois]["montant_paye"] = 0.0
            self._contenu_du_fichier[mois]["prelevements"] = []
            self._contenu_du_fichier[mois]["epargnes"] = []
            self._contenu_du_fichier[mois]["depenses"] = []
            
        # Mise-à-jour de la liste qui contient les mois
        self.recuperation_de_la_liste_des_mois()

    # ==================================
    def verification_montant_paye(self):
        """
            Méthode qui permet de vérifier que le montant de la paye existe pour chaque mois
            S'il n'existe pas on le créé et on initialise sa valeur à 0
        """
        
        for indice, mois in enumerate(self._liste_des_mois):
            
            try:
                
                self._contenu_du_fichier[mois]["montant_paye"]
                
            except KeyError:
                
                self._contenu_du_fichier[mois]["montant_paye"] = 0.0

    # ================================
    def verification_categories(self):
        """
            Méthode qui permet de vérififer la présence des trois catégories (prélèvements, épargnes, dépenses) dans chaque mois
            Si l'une des catégories n'existe pas elle est créée et initialisé avec une liste vide
        """
        
        for indice, mois in enumerate(self._liste_des_mois):
            
            # Catégorie prélèvements
            try:
                
                self._contenu_du_fichier[mois]["prelevements"]
                
            except KeyError:
                
                self._contenu_du_fichier[mois]["prelevements"] = []
                
            # Catégorie épargnes
            try:
                
                self._contenu_du_fichier[mois]["epargnes"]
                
            except KeyError:
                
                self._contenu_du_fichier[mois]["epargnes"] = []
                
            # Catégorie dépenses
            try:
                
                self._contenu_du_fichier[mois]["depenses"]
                
            except KeyError:
                
                self._contenu_du_fichier[mois]["depenses"] = []

    # ========================================================
    def verification_elements(self, mois_en_cours, categorie):
        """
            Méthode qui permet de vérifier que les éléments de l'indice cours pour le mois en cours et la catégorie indiquée en argument sont corrects
        """
        
        # Si l'indice en cours ne contient pas assez d'éléments
        if len(self._liste_des_elements_indice_en_cours) < len(self._liste_des_elements[categorie]):
            
            # On itère sur chaque élément
            for indice, element in enumerate(self._liste_des_elements[categorie]):
                
                # Si l'élément ne figure pas dans la liste des éléments de l'indice en cours
                if element not in self._liste_des_elements_indice_en_cours:
                    
                    message_d_erreur = "Il manque l'élément {} dans la catégorie {} pour le mois {}".format(element, categorie, mois_en_cours)
                    raise KeyError(message_d_erreur)
                    
        # Si l'indice en cours possède trop d'éléments
        elif len(self._liste_des_elements_indice_en_cours) > len(self._liste_des_elements[categorie]):
            
            message_d_erreur = "Il y a trop d'éléments dans la catégorie {} pour le mois {}".format(categorie, mois_en_cours)
            raise KeyError(message_d_erreur)
            
        # Si l'indice en cours possède exactement le nombre d'éléments on vérifie que ce sont les bons, i.e. qu'ils correspondent tous à l'un de ceux figurants dans la liste des éléments pour la catégorie associée
        for indice, element in enumerate(self._liste_des_elements[categorie]):
            
            if element not in self._liste_des_elements_indice_en_cours:
                
                message_d_erreur = "Il manque l'élément {} dans la catégorie {} pour le mois {}".format(element, categorie, mois_en_cours)
                raise KeyError(message_d_erreur)

    # ==========================================
    def verification_categorie(self, categorie):
        """
            Méthode qui permet de vérifier le contenu de la catégorie indiquée en argument
        """
        
        # On itère sur chaque mois
        for indice, mois in enumerate(self._liste_des_mois):
            
            # On itère sur les éléments de la catégorie indiquée en argument du mois en cours
            for indice, element in enumerate(self._contenu_du_fichier[mois][categorie]):
                
                # Récupération de la liste des élément associé à l'indice en cours
                self._liste_des_elements_indice_en_cours = self._contenu_du_fichier[mois][categorie][indice].keys()
                
                # Vérification de la présence des éléments du mois en cours
                self.verification_elements(mois, categorie)

    # ======================
    def verifications(self):
        """
            Méthode qui permet de lancer les différentes vérifications
        """
        
        # Vérification de la présence de la date de mise-à-jour
        self.verification_date_de_mise_a_jour()
        
        # Vérification de la présence de l'année
        self.verification_annee()
        
        # Vérification de la présence d'au moins un mois
        self.verification_des_mois()
        
        # Vérification de la présence du montant de la paye dans chaque mois
        self.verification_montant_paye()
        
        # Vérification de la présence des trois catégories (prélèvements, épargnes, dépenses) dans chaque mois
        self.verification_categories()
        
        # Vérification du contenu de la catégorie prélèvements
        self.verification_categorie("prelevements")
        
        # Vérification du contenu de la catégorie épargnes
        self.verification_categorie("epargnes")
        
        # Vérification du contenu de la catégorie dépenses
        self.verification_categorie("depenses")
        

# =================================================================================================
# Utilisation
# =================================================================================================

if __name__ == "__main__":
    
    print("Ce module n'est pas voué à être exécuté seul")
