from constantes import SYMBOLES_GRILLE
from random import randint
# Constantes grille de jeu
MUR_COIN = 6
MUR_GAUCHE_DROIT = 4
MUR_HAUT_BAS = 5
CELLULE_VIDE = 0
LARGEUR_CARACTERES = 3


def grille_initialiser(hauteur, largeur):
    """
    Initialise une grille vierge aux dimensions données.

    Arguments :
        hauteur (int): Nb de cases en hauteur de la grille
        largeur (int): Nb de cases en largeur de la grille

    Retourne  :
        [list] : Grille de jeu vierge.
    """

    # Initialiser le tableau à retourner.
    grille_vierge = []

    # Assignation des lignes
    ligne_haut_bas = [MUR_COIN] + [MUR_HAUT_BAS]*(largeur-2) + [MUR_COIN]
    ligne_milieu = [MUR_GAUCHE_DROIT] + [CELLULE_VIDE]*(largeur-2) + [MUR_GAUCHE_DROIT]

    grille_vierge.append(ligne_haut_bas)
    for i in range(hauteur-2):
        grille_vierge.append(ligne_milieu.copy())
    grille_vierge.append(ligne_haut_bas)

    # Retourner la grille vierge.
    return grille_vierge


def grille_dessiner(grille):
    """
    Crée une grille de symboles [str] à partir de la grille de codes [int] pour l'affichage.

    Arguments :
        grille [list]: Grille de jeu contenant des constantes symboliques

    Retourne  :
        [list] : Grille contenant des symboles.
    """

    grille_symboles = []

    for i in range(len(grille)):
        ligne = ""
        for j in range(len(grille[i])):
            ligne += SYMBOLES_GRILLE[grille[i][j]]
        grille_symboles.append(ligne)

    return grille_symboles


def grille_afficher(grille):
    """
    Affiche une grille de symboles à la ligne de commande avec les numéros de lignes et de colonnes en partant de 1

    Arguments :
        grille [list]: Grille de jeu qui contient des symboles

    Retourne  :
        Rien.
    """

    grille_symboles = grille_dessiner(grille)
    largeur_grille = int(len(grille_symboles[0]) / LARGEUR_CARACTERES)

    # Affiche la première ligne
    print("       ", end='')
    for i in range(1, largeur_grille - 1):
        print(str(i), end='  ')

    # Nouvelle ligne
    print('')

    # Affiche le tableau
    for i in range(len(grille_symboles)):
        if i == 0:
            print('   ' + grille_symboles[i], end='\n')

        elif i == len(grille_symboles) - 1:
            print('   ' + grille_symboles[i], end='\n')

        else:
            print('  ' + str(i) + grille_symboles[i], end='\n')


def grille_generer_position_aleatoire(grille):
    """
    Génère une position aléatoire dans une grille en évitant les bordures

    Arguments :
        grille [list]: Grille de jeu

    Retourne  :
        [tuple]: Une position (i,j) aléatoire
    """

    # Génère une valeur entre 1 et la longueur de la grille(en i) -2 pour éviter la case de la bordure.
    # -2, car len liste est toujours à +1 des valeurs de position et pour éviter la case de bordure.
    i = randint(1, len(grille)-2)

    # Génère une valeur entre 1 et la longueur de la grille (en j) -2 pour éviter la case de la bordure.
    # -2, car len liste est toujours à +1 des valeurs de position et pour éviter la case de bordure.
    j = randint(1, len(grille[0])-2)

    return i, j


def grille_cellule_est_vide():
    pass


def grille_generer_position_aleatoire_valide():
    pass


def grille_navire_est_valide():
    pass


def grille_generer_orientation_aleatoire_valide():
    pass


def grille_ajouter_navire():
    pass


def grille_ajouter_flotte_positions_aleatoires():
    pass


def grille_gestionnaire_tir():
    pass


def grille_adversaire_gestionnaire_tir():
    pass
