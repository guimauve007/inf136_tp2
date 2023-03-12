# Grille de jeu
MUR_COIN = 6
MUR_GAUCHE_DROIT = 4
MUR_HAUT_BAS = 5
CELLULE_VIDE = 0


def grille_generer_position_aleatoire():
    pass


def grille_generer_position_aleatoire_valide():
    pass


def grille_afficher():
    pass


def grille_dessiner():
    pass


def grille_navire_est_valide():
    pass


def grille_generer_orientation_aleatoire_valide():
    pass


def grille_ajouter_navire():
    pass


def grille_gestionnaire_tir():
    pass


def grille_adversaire_gestionnaire_tir():
    pass


def grille_initialiser(hauteur, largeur):

    # Initialiser le tableau à retourner.
    grille_vierge = []
    ligne = [CELLULE_VIDE] * largeur

    # Ajouter les lignes et les colonnes une par une.
    for y in range(hauteur):
        for x in range(largeur):
            if y == 0 or y == hauteur - 1:
                if x == 0 or x == largeur - 1:
                    ligne[x] = MUR_COIN
                else:
                    ligne[x] = MUR_HAUT_BAS

            else:
                if x == 0 or x == largeur - 1:
                    ligne[x] = MUR_GAUCHE_DROIT
                else:
                    ligne[x] = CELLULE_VIDE

        grille_vierge.append(ligne.copy())

    # Retourner la grille vierge.
    return grille_vierge
