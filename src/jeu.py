from constantes import JOUEUR
from constantes import ORDINATEUR
from constantes import HAUTEUR_GRILLE
from constantes import LARGEUR_GRILLE
from flotte import flotte_calculer_vie
from random import randint

def jeu_afficher_joueur_courant(identifiant_courant):
    """
    Affiche un message qui indique le joueur courant.

    Arguments :
        identifiant_courant (int) : indique si c'est le tour de l'ordinateur ou du joueur à jouer

    Retourne :
        Aucun.
    """

    # Si identifiant_courant est égal à la constante JOUEUR,
    # un print indique que c'est le tour au joueur de jouer.
    if identifiant_courant == JOUEUR:
        print('C\'est au tour du joueur')

    # Si identifiant_courant est égal à la constante ORDINATEUR,
    # un print indique que c'est le tour de l'ORDINATEUR jouer.
    elif identifiant_courant == ORDINATEUR:
        print('C\'est au tour de l\'ordinateur')


def jeu_joueur_saisir_position_tir():
    """
    Saisit la position du tir du joueur et redemande jusqu'à ce que la saisit soit valide.

    Arguments :
        Aucun.

    Retourne  :
        i --> (int) : i représente la hauteur du tir saisit par l'utilisateur
        j --> (int) : j représente la largeur du tir saisit par l'utilisateur
    """
    # test
    # Saisit de la hauteur du tir
    i = int(input('Saisissez la hauteur de votre tir : '))

    # Redemander la saisit si la valeur saisit n'est pas dans la grille de jeux
    # la hauteur limite supérieur de la grille de jeux est HAUTEUR GRILLE
    # la hauteur limite inférieur de la grille est 1
    while i > HAUTEUR_GRILLE and i >= 1:
        i = int(input('Saisissez la hauteur de votre tir : '))

    # Saisit de la largeur du tir
    j = int(input('Saisissez la largueur de votre tir : '))

    # Redemander la saisit si la valeur saisit n'est pas dans la grille de jeux
    # la largeur limite supérieur de la grille de jeux est HAUTEUR GRILLE
    # la largeur limite inférieur de la grille est 1
    while j > LARGEUR_GRILLE and j >= 1:
        i = int(input('Saisissez la largueur de votre tir : '))

    # Retourne un tuple représentent les coordonnées (x, y) du tir du joueur
    return i, j


def jeu_ordinateur_saisir_position_tir(grille):
    """
    Génère une position de tir aléatoire pour l'ordinateur tant que la case ne soit pas vide.

    Arguments :
        Aucun.

    Retourne  :
        i --> (int) : i représente la hauteur du tir de l'ordinateur
        j --> (int) : j représente la largeur du tir de l'ordinateur
    """

    # Génère une première position de tir aléatoire avec les coordonnées (i, j)
    i = randint(0, HAUTEUR_GRILLE-1)
    j = randint(0, LARGEUR_GRILLE-1)

    if grille[i][j] == []:
        return i, j

    else:
        while grille[i][j] != [] :
            i = randint(1, HAUTEUR_GRILLE)
            j = randint(1, LARGEUR_GRILLE)

    return i, j


def jeu_est_partie_terminee(flotte_1, flotte_2):
    """
    Détermine si une partie est terminée. Si la vie d'une des flottes est égale à zéro, cela indique que la partie est
    complétée.

    Arguments :
        flotte_1 [list] : une flotte de navires du premier joueur.
        flotte_2 [list] : une flotte de navires du deuxième joueur.

    Retourne  :
        [bool] : indicateur de fin de partie.
    """

    # Calculer la vie des flottes 1 et 2 avec la fonction flotte_calculer_vie.
    vie_flotte_1 = flotte_calculer_vie(flotte_1)
    vie_flotte_2 = flotte_calculer_vie(flotte_2)

    # Comparer la vie des flottes 1 et 2 avec un booléen.
    return vie_flotte_1 == 0 or vie_flotte_2 == 0


def jeu_afficher_vainqueur(flotte_joueur):
    """
    Annonce le vainqueur de la partie en affichant le message final.

    Arguments :
        flotte_joueur [list] : correspond à la flotte du joueur

    Retourne :
        Rien.
    """

    # pas sur de cette etape a voir faut il appeler l'autre fonction ou faire une somme
    if flotte_joueur == 0:

        # Afficher le message vainqueur de l'ordinateur contre le joueur.
        print('C\'est l\'ordinateur qui a gagné!')

    else:

        # Afficher le message vainqueur du joueur contre l'ordinateur.
        print('C\'est le joueur qui a gagné!')
