import constantes
import grille
import jeu
import flotte

if __name__ == "__main__":
    flotte1 = flotte.flotte_generer_aleatoire()
    print(flotte.flotte_calculer_vie(flotte1))



