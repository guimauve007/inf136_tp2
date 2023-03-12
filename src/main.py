import constantes
import grille
import jeu
import flotte

if __name__ == "__main__":
    grille.grille_afficher(grille.grille_dessiner(grille.grille_initialiser(10, 5)))
