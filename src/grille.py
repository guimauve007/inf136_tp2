import navire
import jeu

def grille_initialiser(hauteur,largeur):

    #Initialiser les cases à 0
    ligne = [0] * largeur

    #Initialiser le tableau à retourner
    grille_vierge = []

    #Ajouter les lignes et les colonnes une par une
    for i in range(hauteur):
        grille_vierge.append(ligne.copy())

    #retourner la grille vierge
    return grille_vierge