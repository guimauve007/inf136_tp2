from constantes import SYMBOLES_GRILLE

# Constantes grille de jeu
MUR_COIN = 6
MUR_GAUCHE_DROIT = 4
MUR_HAUT_BAS = 5
CELLULE_VIDE = 0
LARGEUR_CARACTERES = 3
DEBUT_CHAINE = 1
PREMIERE_LIGNE = 0
PREMIERE_COLONNE = 0
DECALAGE_FIN_TABLEAU = 1


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
    ligne = [CELLULE_VIDE] * largeur

    # Index des lignes
    derniere_ligne = hauteur - DECALAGE_FIN_TABLEAU

    # Index des colonnes
    derniere_colonne = largeur - DECALAGE_FIN_TABLEAU

    # Ajouter les lignes et les colonnes une par une.
    for i in range(hauteur):
        for j in range(largeur):
            if i == PREMIERE_LIGNE or i == derniere_ligne:
                if j == PREMIERE_COLONNE or j == derniere_colonne:
                    ligne[j] = MUR_COIN
                else:
                    ligne[j] = MUR_HAUT_BAS

            else:
                if j == PREMIERE_COLONNE or j == derniere_colonne:
                    ligne[j] = MUR_GAUCHE_DROIT
                else:
                    ligne[j] = CELLULE_VIDE

        grille_vierge.append(ligne.copy())

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
    derniere_ligne = len(grille_symboles) - DECALAGE_FIN_TABLEAU
    largeur_grille = int(len(grille_symboles[PREMIERE_LIGNE]) / LARGEUR_CARACTERES)

    # Affiche la première ligne
    print("       ", end='')
    for i in range(DEBUT_CHAINE, largeur_grille - DECALAGE_FIN_TABLEAU):
        print(str(i), end='  ')

    # Nouvelle ligne
    print('')

    # Affiche le tableau
    for i in range(len(grille_symboles)):
        if i == PREMIERE_LIGNE:
            print('   ' + grille_symboles[i], end='\n')

        elif i == derniere_ligne:
            print('   ' + grille_symboles[i], end='\n')

        else:
            print('  ' + str(i) + grille_symboles[i], end='\n')


def grille_generer_position_aleatoire():
    pass


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
