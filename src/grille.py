from constantes import SYMBOLES_GRILLE

# Grille de jeu
MUR_COIN = 6
MUR_GAUCHE_DROIT = 4
MUR_HAUT_BAS = 5
CELLULE_VIDE = 0


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
    PREMIERE_LIGNE = 0
    DERNIERE_LIGNE = hauteur - 1

    # Index des colonnes
    PREMIERE_COLONNE = 0
    DERNIERE_COLONNE = largeur - 1

    # Ajouter les lignes et les colonnes une par une.
    for i in range(hauteur):
        for j in range(largeur):
            if i == PREMIERE_LIGNE or i == DERNIERE_LIGNE:
                if j == PREMIERE_COLONNE or j == DERNIERE_COLONNE:
                    ligne[j] = MUR_COIN
                else:
                    ligne[j] = MUR_HAUT_BAS

            else:
                if j == PREMIERE_COLONNE or j == DERNIERE_COLONNE:
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
        ligne = []
        for j in range(len(grille[i])):
            ligne.append(SYMBOLES_GRILLE[grille[i][j]])
        grille_symboles.append(ligne.copy())

    return grille_symboles


def grille_afficher(grille):
    """
    Affiche une grille de symboles à la ligne de commande avec les numéros de lignes et de colonnes en partant de 1

    Arguments :
        grille [list]: Grille de jeu qui contient des symboles

    Retourne  :
        Rien.
    """

    PREMIERE_LIGNE = 0
    DERNIERE_LIGNE = len(grille) - 1
    LARGEUR_GRILLE = len(grille[PREMIERE_LIGNE])
    DEBUT_CHAINE = 1

    # Affiche la première ligne
    print("       ", end='')
    for i in range(DEBUT_CHAINE, LARGEUR_GRILLE - 1):
        print(str(i), end='  ')

    # Nouvelle ligne
    print('')

    # Affiche le tableau
    for i in range(len(grille)):
        chaine_caracteres = ""
        if i == PREMIERE_LIGNE:
            print('   ' + chaine_caracteres.join(grille[i]), end='\n')

        elif i == DERNIERE_LIGNE:
            print('   ' + chaine_caracteres.join(grille[i]), end='\n')

        else:
            print(f'  {i}' + chaine_caracteres.join(grille[i]), end='\n')


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
