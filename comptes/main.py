"""
    Module qui permet de lancer l'application
"""

# =================================================================================================
# Import des librairies
# =================================================================================================

# Import des librairies graphiques
from PyQt5 import QtWidgets

# Import des librairies qui contiennent le modèle
from src.controleur import Controleur

# Import des autres librairies
import sys


# =================================================================================================
# Utilisation
# =================================================================================================

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    instance_controleur = Controleur(app)
    app.exec_()

# TODO : pour l'affichage des dépenses :
# TODO : > si c'est un chèque subdiviser la cellule pour mettre, en-dessous mais dans la mêùe cellule, le numéro du chèque
# TODO : > si c'est un virement vers/depuis le livret A subdiviser la cellule pour mettre, en-dessous et dans deux sous-cellules, la date de création du virement puis la date de perception du virement

# TODO : faire une fonction pour gérer l'affichage des valeurs de type monétique
# TODO : > signe - en tout début de cellule,
# TODO : > séparation des milliers, toujours deux chiffres après la virgule même si c'est deux 0

# TODO : code couleur pour les dépenses et les épargnes :
# TODO : > jaune  => virement non réalisé,
# TODO : > orange => virement fait mais non perçu,
# TODO : > vert   => virement perçu

# TODO : pour les prélèvements : tant que la date est vide l'affichage restera en "gris", dès que la date sera renseignée la ligne sera coloriée en vert (cela fera office de "statut")

# TODO : ajouter des logs dans un fichier, un fichier par jour, dans des sous-dossiers (mois -> années)

# TODO : mettre montant_paye et reste sur la même colonne puis, sur la doite, à côté des boutons, mettre le reste, i.e. Prélèvements, Epargne et Dépenses

# TODO : renforcer la validation des dates : en plus de la regex il faudra valider la sélection utilisateur ssi l'utilisateur a indiqué une bonne date (exemple : 30/02/2022)
