from navire import navire_generer_aleatoire
from random import randint
from constantes import FLOTTE_TAILLE_MIN, FLOTTE_TAILLE_MAX



def flotte_generer_aleatoire():
    """
    Génère une flotte de navires aléatoires.

    Arguments :
        Aucuns.

    Retourne  :
        [list] : une flotte de navires aléatoires.
    """

    liste_flotte = []

    # Obtenir une quantité de navires à générer.
    taille_flotte = randint(FLOTTE_TAILLE_MIN, FLOTTE_TAILLE_MAX)

    # Ajouter les navires à la flotte.
    for i in range(taille_flotte):
        liste_flotte.append(navire_generer_aleatoire())

    # Retourner la liste créée.
    return liste_flotte
