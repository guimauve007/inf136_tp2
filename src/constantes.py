# Identifiants du joueur courant
JOUEUR = 0
ORDINATEUR = 1

# Limites de la taille d'une flotte de navires
FLOTTE_TAILLE_MIN = 4
FLOTTE_TAILLE_MAX = 6

# Dimensions de la grille de jeu
LARGEUR_GRILLE = 10
HAUTEUR_GRILLE = 10

# Codes pour l'orientation des navires
NORD = 0                # Représente l'orientation nord d'un navire
SUD = 1                 # Représente l'orientation sud d'un navire
EST = 2                 # Représente l'orientation est d'un navire
OUEST = 3               # Représente l'orientation ouest d'un navire

# Codes de cellules pour les différents états de la grille de jeu
CELLULE_VIDE = 0        # Représente une cellule vide (c.-à-d. de l'eau)
TIR_MANQUE = 1          # Représente une cellule dans laquelle il y a eu un tir manqué
BATEAU_VIVANT = 2       # Représente une portion de bateau non atteinte
BATEAU_ATTEINT = 3      # Représente une position de bateau atteinte
MUR_GAUCHE_DROIT = 4    # Représente un mur sur les côtés gauche et droit
MUR_HAUT_BAS = 5        # Représente un mur sur les côtés haut et bas
MUR_COIN = 6            # Représente les coins de la grille
POINTE_NORD = 7         # Représente un navire qui pointe vers le Nord
POINTE_SUD = 8          # Représente un navire qui pointe vers le Sud
POINTE_EST = 9          # Représente un navire qui pointe vers l'est
POINTE_OUEST = 10       # Représente un navire qui pointe vers l'ouest

# Types de navires
PORTE_AVION = 0
CROISEUR = 1
CONTRE_TORPILLEUR = 2
TORPILLEUR = 3

# Nombre de cases occupées par chacun des navires
VIE_PORTE_AVION = 5
VIE_CROISEUR = 4
VIE_CONTRE_TORPILLEUR = 3
VIE_TORPILLEUR = 2

# Dictionnaire qui relie l'identifiant d'un navire à sa taille
VIE_NAVIRES = {PORTE_AVION: VIE_PORTE_AVION,
               CROISEUR: VIE_CROISEUR,
               CONTRE_TORPILLEUR: VIE_CONTRE_TORPILLEUR,
               TORPILLEUR: VIE_TORPILLEUR}

# Symboles qui représentent les différents états de la grille lors de l'affichage
SYMBOLE_CELLULE_VIDE = '   '        # Représente une cellule vide (c.-à-d. de l'eau)
SYMBOLE_TIR_MANQUE = ' ¤ '          # Représente une cellule dans laquelle il y a eu un tir manqué
SYMBOLE_BATEAU_VIVANT = ' □ '       # Représente une portion de bateau non atteinte
SYMBOLE_BATEAU_ATTEINT = ' × '      # Représente une position de bateau atteinte
SYMBOLE_MUR_GAUCHE_DROIT = ' | '    # Représente un mur sur les côtés gauche et droit
SYMBOLE_MUR_HAUT_BAS = '———'        # Représente un mur sur les côtés haut et bas
SYMBOLE_MUR_COIN = ' + '            # Représente les coins de la grille
SYMBOLE_POINTE_NORD = ' ^ '         # Représente un navire qui pointe vers le Nord
SYMBOLE_POINTE_SUD = ' ⌄ '          # Représente un navire qui pointe vers le Sud
SYMBOLE_POINTE_EST = ' > '          # Représente un navire qui pointe vers l'est
SYMBOLE_POINTE_OUEST = ' < '        # Représente un navire qui pointe vers l'ouest

# Dictionnaire qui relie les constantes de la grille à leurs symboles
SYMBOLES_GRILLE = {CELLULE_VIDE: SYMBOLE_CELLULE_VIDE,
                   TIR_MANQUE: SYMBOLE_TIR_MANQUE,
                   BATEAU_VIVANT: SYMBOLE_BATEAU_VIVANT,
                   BATEAU_ATTEINT: SYMBOLE_BATEAU_ATTEINT,
                   MUR_GAUCHE_DROIT: SYMBOLE_MUR_GAUCHE_DROIT,
                   MUR_HAUT_BAS: SYMBOLE_MUR_HAUT_BAS,
                   MUR_COIN: SYMBOLE_MUR_COIN,
                   POINTE_NORD: SYMBOLE_POINTE_NORD,
                   POINTE_SUD: SYMBOLE_POINTE_SUD,
                   POINTE_EST: SYMBOLE_POINTE_EST,
                   POINTE_OUEST: SYMBOLE_POINTE_OUEST}
