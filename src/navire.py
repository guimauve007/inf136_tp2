# Générateur de nombres aléatoires uniformément distribués entre bornes
from random import randint

# Directions dans lesquelles pointe un navire
from constantes import NORD
from constantes import SUD
from constantes import EST
from constantes import OUEST

# Types de navires
from constantes import PORTE_AVION
from constantes import TORPILLEUR

# Dictionnaire qui relie l'identifiant d'un navire à sa taille
from constantes import VIE_NAVIRES


def navire_assigner_position(navire, i, j):
    """
    Mutateur de position d'un navire.

    Arguments :
        navire (dict) : Le navire.
        i (int) : Ligne de la position proposée du navire.
        j (int) : Colonne de la position proposée du navire.

    Retourne  :
        Rien.
    """

    navire['i'] = i
    navire['j'] = j


def navire_assigner_orientation(navire, orientation):
    """
    Mutateur de position d'un navire.

    Arguments :
        navire (dict) : Le navire.
        orientation (int) : Un code qui représente l'orientation du navire.

    Retourne  :
        Rien.
    """

    navire['orientation'] = orientation


def navire_obtenir_ligne(navire):
    """
    Accesseur pour la ligne de la position du navire.

    Arguments :
        navire (dict) : Le navire.

    Retourne  :
        (int) : La ligne (i) du navire.
    """

    return navire['i']


def navire_obtenir_colonne(navire):
    """
    Accesseur pour la colonne de la position du navire.

    Arguments :
        navire (dict) : Le navire.

    Retourne  :
        (int) : La colonne (j) du navire.
    """

    return navire['j']


def navire_obtenir_taille(navire):
    """
    Accesseur pour la taille du navire.

    Arguments :
        navire (dict) : Le navire.

    Retourne  :
        (int) : La taille du navire.
    """

    return navire['taille']


def navire_obtenir_orientation(navire):
    """
    Accesseur pour l'orientation du navire.

    Arguments :
        navire (dict) : Le navire.

    Retourne  :
        (int) : L'orientation du navire sous forme de constante entière.
    """

    return navire['orientation']


def navire_obtenir_vie(navire):
    """
    Accesseur pour la vie du navire. La vie d'un navire correspond au nombre de portions (cases) de ce dernier qui
    n'ont pas été atteint par un tir ennemi.

    Arguments :
        navire (dict) : Le navire.

    Retourne  :
        (int) : La vie du navire.
    """

    return navire['vie']


def navire_obtenir_positions(navire):
    """
    Accesseur pour les positions occupées par le navire.

    Arguments :
        navire (dict) : Le navire.

    Retourne  :
        (list) : Les positions occupées par le navire sous forme de liste.
    """

    return navire['positions']


def navire_ajouter_position(navire, nouvelle_position):
    """
    Ajoute une position à la liste de positions occupées par un navire.

    Arguments :
        navire (dict) : Le navire.
        nouvelle_position (tuple) : Position (i,j) à ajouter.

    Retourne  :
        Rien.
    """

    navire['positions'].append(nouvelle_position)


def navire_decrementer_vie(navire):
    """
    Décrémente la vie d'un navire d'une unité.

    Arguments :
        navire (dict) : Le navire.

    Retourne  :
        Rien.
    """

    # S'assurer que le navire est toujours en vie
    assert navire_obtenir_vie(navire) > 0, 'La vie d\'un navire ne peut pas être négative'

    navire['vie'] -= 1


def navire_calculer_positions(navire):
    """
    Calcule les positions du navire en fonction de la position de sa tête, de son
    orientation et de sa longueur. Les positions sont stockées sous formes de
    tuples (i, j) dans une liste.

    Arguments :
        navire (dict)  : Un navire.

    Retourne  :
        Rien.
    """

    # Extraire les propriétés du navire
    i = navire_obtenir_ligne(navire)
    j = navire_obtenir_colonne(navire)
    taille = navire_obtenir_taille(navire)
    orientation = navire_obtenir_orientation(navire)

    # Calculer chacune des positions et les ajouter à la liste de positions
    if orientation == NORD:
        for k in range(taille):
            navire_ajouter_position(navire, (i + k, j))

    elif orientation == SUD:
        for k in range(taille):
            navire_ajouter_position(navire, (i - k, j))

    elif orientation == EST:
        for k in range(taille):
            navire_ajouter_position(navire, (i, j - k))

    elif orientation == OUEST:
        for k in range(taille):
            navire_ajouter_position(navire, (i, j + k))


def navire_generer(identifiant):
    """
    Génère un navire à partir d'un identifiant.

    Arguments :
        identifiant (int) : L'identifiant unique du navire à générer.

    Retourne  :
        (dict) : Le navire.
    """

    return {'taille': VIE_NAVIRES[identifiant],
            'vie': VIE_NAVIRES[identifiant],
            'i': None,
            'j': None,
            'orientation': None,
            'positions': []}


def navire_generer_aleatoire():
    """
    Génère un navire aléatoire.

    Arguments :
        Aucuns.

    Retourne  :
        (dict) : Le navire.
    """

    # Générer un navire aléatoire à partir d'un identifiant aléatoire
    return navire_generer(randint(PORTE_AVION, TORPILLEUR))
