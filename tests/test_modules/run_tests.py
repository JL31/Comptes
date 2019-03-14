# coding: utf-8

""" Module qui xxx """

# =================================================================================================
# Paramètres globaux
# =================================================================================================

__author__ = "Julien LEPAIN"
__version__ = 1.0


# =================================================================================================
# Import des librairies
# =================================================================================================

from unittest import TestLoader, TextTestRunner

# =================================================================================================
# Classes
# =================================================================================================

# =================================================================================================
# Fonctions
# =================================================================================================

# =================================================================================================
# Utilisation
# =================================================================================================

if __name__ == "__main__":

    tests_suite = TestLoader().discover(".")
    TextTestRunner(verbosity=1).run(tests_suite)
