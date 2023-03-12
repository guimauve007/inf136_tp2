from navire import navire_generer_aleatoire
from navire import navire_obtenir_positions
from navire import navire_obtenir_vie
from navire import navire_decrementer_vie
from random import randint
from constantes import FLOTTE_TAILLE_MIN, FLOTTE_TAILLE_MAX, I_TIR, J_TIR


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


def flotte_calculer_vie(flotte):
    """
    Calcule la 'vie' d'un joueur à partir de sa flotte.

    Arguments :
        flotte [list]: Une flotte de navires.
        liste_flotte.append(navire_generer_aleatoire())

    Retourne  :
        (int) : Somme des champs 'vie' des navires de la flotte.
    """

    somme_vie = 0
    for i in range(len(flotte)):
        somme_vie += navire_obtenir_vie(flotte[i])
    return somme_vie


def flotte_gestionnaire_tir(flotte, i_tir, j_tir):
    """
    Met une flotte à jour par suite d'un tir à une position donnée.
    Si un navire est atteint, la position du tir est supprimée de
    la liste des positions qu'il occupe et sa vie est décrémentée d'une unité.

    Arguments :
        flotte [list]: Une flotte de navires.
        i_tir (int) : La ligne du tir
        j_tir (int) : La colonne du tir

    Retourne  :
        (bool) : Indicateur de succès du tir à atteindre une cible.
    """

    for i in range(len(flotte)):
        positions = navire_obtenir_positions(flotte[i])
        for j in range(len(positions)):
            if (positions[j][I_TIR] == i_tir) & (positions[j][J_TIR] == j_tir):
                del positions[j]
                navire_decrementer_vie(flotte[i])
                return True

    # Si aucun navire touché
    return False
