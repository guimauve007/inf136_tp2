from constantes import JOUEUR
from constantes import ORDINATEUR
from constantes import HAUTEUR_GRILLE
from constantes import LARGEUR_GRILLE
from flotte import flotte_calculer_vie


def jeu_afficher_jouer_courant(identifiant_courant):

    if identifiant_courant == JOUEUR:
        print('C\'est au tour du joueur')

    elif identifiant_courant == ORDINATEUR:
        print('C\'est au tour de l\'ordinateur')


"""
    Saisit la position du tir du joueur et redemande jusqu'à ce que la saisit soit valide.

    Arguments :
        Aucun.

    Retourne  :
       i --> (int) : i représente la hauteur du tir saisit par l'utilisateur
       j --> (int) : j représente la largeur du tir saisit par l'utilisateur
"""


def jeu_joueur_saisir_position_tir():

    # Saisit de la hauteur du tir
    i = input(int('Saisissez la hauteur de votre tir : '))

    # Redemander la saisit si la valeur saisit n'est pas dans la grille de jeux
    #
    while i > HAUTEUR_GRILLE and i > 1:
        i = input(int('Saisissez la hauteur de votre tir : '))

    j = input(int('Saisissez la largueur de votre tir : '))

    while j > LARGEUR_GRILLE and j > 1:
        i = input(int('Saisissez la largueur de votre tir : '))

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
    vie_flotte_1 = {flotte_calculer_vie(flotte_1)}
    vie_flotte_2 = {flotte_calculer_vie(flotte_2)}

    # Comparer la vie des flottes 1 et 2 avec un booléen.
    if vie_flotte_1 == 0 or vie_flotte_2 == 0:

        # Retourne Vrai si la partie est terminée, c'est-à-dire lorsque la vie d'une des deux flottes correspond à 0.
        return True

    else:

        # Retourner Faux si la partie continue.
        return False


def jeu_afficher_vainqueur(flotte_joueur):
    """
    Annonce le vainqueur de la partie en affichant le message final.

    Arguments :
        flotte_joueur [list] : correspond à la flotte du joueur

    Retourne :
        Rien.
    """

    # pas sur de cette etape a voir faut il appeler l'autre fonction ou faire une somme
    if flotte_joueur == 0 :

        # Afficher le message vainqueur de l'ordinateur contre le joueur.
        print('C\'est l"ordinateur qui a gagné! Désolé, il faudrait se pratiquer davantage.')

    else:

        # Afficher le message vainqueur du joueur contre l'oridnateur.
        print('C\'est le joueur qui a gagné. Félicitations!')

