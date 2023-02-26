# Importer la librairie deepdiff pour comparer des structures imbriquées
from deepdiff import DeepDiff

# Importer la fonction seed() pour fixer la graine aléatoire
from random import seed

# Constantes utilisées pour les états de la grille
from constantes import MUR_COIN
from constantes import MUR_HAUT_BAS
from constantes import MUR_GAUCHE_DROIT
from constantes import CELLULE_VIDE
from constantes import TIR_MANQUE
from constantes import BATEAU_VIVANT
from constantes import BATEAU_ATTEINT
from constantes import POINTE_NORD
from constantes import POINTE_SUD
from constantes import POINTE_EST
from constantes import POINTE_OUEST

# Constantes utilisées pour l'orientation des navires
from constantes import NORD
from constantes import SUD
from constantes import EST
from constantes import OUEST

# Importer les fonctions à tester
from grille import grille_initialiser
from grille import grille_dessiner
from grille import grille_afficher
from grille import grille_generer_position_aleatoire
from grille import grille_generer_position_aleatoire_valide
from grille import grille_navire_est_valide
from grille import grille_generer_orientation_aleatoire_valide
from grille import grille_ajouter_navire
from grille import grille_gestionnaire_tir
from grille import grille_adversaire_gestionnaire_tir


def test_grille_initialiser_1():
    # Générer une grille 4x4
    grille_obtenue = grille_initialiser(4, 4)

    # Générer la grille que l'on s'attend à recevoir
    grille_attendue = [[MUR_COIN, MUR_HAUT_BAS, MUR_HAUT_BAS, MUR_COIN],
                       [MUR_GAUCHE_DROIT, CELLULE_VIDE, CELLULE_VIDE, MUR_GAUCHE_DROIT],
                       [MUR_GAUCHE_DROIT, CELLULE_VIDE, CELLULE_VIDE, MUR_GAUCHE_DROIT],
                       [MUR_COIN, MUR_HAUT_BAS, MUR_HAUT_BAS, MUR_COIN]]

    assert len(DeepDiff(grille_obtenue, grille_attendue)) == 0


def test_grille_initialiser_2():
    # Générer une grille 5x5
    grille_obtenue = grille_initialiser(5, 5)

    # Générer la grille que l'on s'attend à recevoir
    grille_attendue = [[MUR_COIN, MUR_HAUT_BAS, MUR_HAUT_BAS, MUR_HAUT_BAS, MUR_COIN],
                       [MUR_GAUCHE_DROIT, CELLULE_VIDE, CELLULE_VIDE, CELLULE_VIDE, MUR_GAUCHE_DROIT],
                       [MUR_GAUCHE_DROIT, CELLULE_VIDE, CELLULE_VIDE, CELLULE_VIDE, MUR_GAUCHE_DROIT],
                       [MUR_GAUCHE_DROIT, CELLULE_VIDE, CELLULE_VIDE, CELLULE_VIDE, MUR_GAUCHE_DROIT],
                       [MUR_COIN, MUR_HAUT_BAS, MUR_HAUT_BAS, MUR_HAUT_BAS, MUR_COIN]]

    assert len(DeepDiff(grille_obtenue, grille_attendue)) == 0


def test_grille_dessiner_1():
    # Générer une grille 5x5
    grille_codes = grille_initialiser(5, 5)

    # Insérer tous les symboles que l'on s'attend à trouver
    grille_codes[1][1] = CELLULE_VIDE
    grille_codes[1][2] = TIR_MANQUE
    grille_codes[1][3] = BATEAU_VIVANT

    grille_codes[2][1] = BATEAU_ATTEINT
    grille_codes[2][2] = POINTE_NORD
    grille_codes[2][3] = POINTE_SUD

    grille_codes[3][1] = POINTE_EST
    grille_codes[3][2] = POINTE_OUEST

    # Dessiner la grille (c.-à-d. transformer en symboles)
    grille_symboles = grille_dessiner(grille_codes)

    # Générer la grille que l'on s'attend à recevoir
    grille_attendue = [' + ————————— + ',
                       ' |     ¤  □  | ',
                       ' |  ×  ^  ⌄  | ',
                       ' |  >  <     | ',
                       ' + ————————— + ']

    assert len(DeepDiff(grille_symboles, grille_attendue)) == 0


def test_grille_dessiner_2():
    # Générer une grille 5x5
    grille_codes = grille_initialiser(6, 6)

    # Insérer tous les symboles que l'on s'attend à trouver
    grille_codes[1][1] = CELLULE_VIDE
    grille_codes[1][2] = TIR_MANQUE
    grille_codes[1][3] = BATEAU_VIVANT
    grille_codes[1][4] = BATEAU_ATTEINT

    grille_codes[2][1] = POINTE_NORD
    grille_codes[2][2] = POINTE_SUD
    grille_codes[2][3] = POINTE_EST
    grille_codes[2][4] = POINTE_OUEST

    # Dessiner la grille (c.-à-d. transformer en symboles)
    grille_symboles = grille_dessiner(grille_codes)

    # Générer la grille que l'on s'attend à recevoir
    grille_attendue = [' + ———————————— + ',
                       ' |     ¤  □  ×  | ',
                       ' |  ^  ⌄  >  <  | ',
                       ' |              | ',
                       ' |              | ',
                       ' + ———————————— + ']

    assert len(DeepDiff(grille_symboles, grille_attendue)) == 0


def test_grille_afficher_1(capsys):
    # Générer une grille de codes 6x6
    grille_codes = grille_initialiser(4, 4)

    # Afficher la grille et capturer la sortie
    grille_afficher(grille_codes)

    # Grille de référence
    grille_str = '       1  2  \n' \
                 '    + —————— + \n' \
                 '  1 |        | \n' \
                 '  2 |        | \n' \
                 '    + —————— + \n'

    # Capturer le contenu de stdout
    contenu_stdout = capsys.readouterr()

    assert contenu_stdout.out == grille_str


def test_grille_afficher_2(capsys):
    # Générer une grille de codes 6x6
    grille_codes = grille_initialiser(6, 6)

    # Insérer tous les symboles que l'on s'attend à trouver
    grille_codes[1][1] = CELLULE_VIDE
    grille_codes[1][2] = TIR_MANQUE
    grille_codes[1][3] = BATEAU_VIVANT
    grille_codes[1][4] = BATEAU_ATTEINT

    grille_codes[2][1] = POINTE_NORD
    grille_codes[2][2] = POINTE_SUD
    grille_codes[2][3] = POINTE_EST
    grille_codes[2][4] = POINTE_OUEST

    # Afficher la grille et capturer la sortie
    grille_afficher(grille_codes)

    # Grille de référence
    grille_str = '       1  2  3  4  \n' \
                 '    + ———————————— + \n' \
                 '  1 |     ¤  □  ×  | \n' \
                 '  2 |  ^  ⌄  >  <  | \n' \
                 '  3 |              | \n' \
                 '  4 |              | \n' \
                 '    + ———————————— + \n'

    # Capturer le contenu de stdout
    contenu_stdout = capsys.readouterr()

    assert contenu_stdout.out == grille_str


def test_generer_position_aleatoire():
    # Fixer la graine aléatoire
    seed(1)

    # Récupérer les positions aléatoires générées par la fonction testée
    i_obtenu, j_obtenu = grille_generer_position_aleatoire(grille_initialiser(6, 6))

    # Positions attendues
    i_attendu = 2
    j_attendu = 1

    assert i_obtenu == i_attendu and j_obtenu == j_attendu


def test_grille_cellule_est_vide():
    # Grille de référence dont le centre est vide
    grille_jeu = grille_initialiser(6, 6)

    # Vérifier que le centre ne contient que des cellules vides
    for i in range(1, 5):
        for j in range(1, 5):
            if grille_jeu[i][j] != CELLULE_VIDE:
                return False

    return True


def test_grille_generer_position_aleatoire_valide_1():
    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    # Remplir le tableau d'artéfacts
    grille_jeu[1][1] = TIR_MANQUE
    grille_jeu[1][2] = BATEAU_ATTEINT
    grille_jeu[1][3] = BATEAU_VIVANT

    grille_jeu[2][1] = POINTE_NORD
    grille_jeu[2][3] = POINTE_SUD

    grille_jeu[3][1] = POINTE_EST
    grille_jeu[3][2] = POINTE_OUEST
    grille_jeu[3][3] = TIR_MANQUE

    # Fixer la graine aléatoire
    seed(0)

    # Générer des positions avec la fonction à tester
    i_obtenu, j_obtenu = grille_generer_position_aleatoire_valide(grille_jeu)

    # Seul le centre du tableau est vide
    i_attendu = 2
    j_attendu = 2

    assert i_obtenu == i_attendu and j_obtenu == j_attendu


def test_grille_generer_position_aleatoire_valide_2():
    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    # Remplir le tableau entier d'artéfacts
    grille_jeu[1][1] = TIR_MANQUE
    grille_jeu[1][2] = TIR_MANQUE
    grille_jeu[1][3] = TIR_MANQUE

    grille_jeu[2][1] = TIR_MANQUE
    grille_jeu[2][2] = TIR_MANQUE
    grille_jeu[2][3] = TIR_MANQUE

    grille_jeu[3][1] = TIR_MANQUE
    grille_jeu[3][2] = TIR_MANQUE
    grille_jeu[3][3] = TIR_MANQUE

    try:

        # La fonction doit échouer puisqu'il n'y a aucune position valide
        _, _ = grille_generer_position_aleatoire_valide(grille_jeu)

    except AssertionError as err:

        assert err.args[0] == 'Nombre d\'itérations maximal atteint.'
        return

    assert False, 'Aucune erreur ne fut déclenchée'


def test_grille_navire_est_valide_1():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    assert not grille_navire_est_valide(grille_jeu, 1, 1, SUD, 3)


def test_grille_navire_est_valide_2():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    assert not grille_navire_est_valide(grille_jeu, 1, 1, EST, 3)


def test_grille_navire_est_valide_3():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    assert not grille_navire_est_valide(grille_jeu, 4, 4, NORD, 3)


def test_grille_navire_est_valide_4():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    assert not grille_navire_est_valide(grille_jeu, 4, 4, OUEST, 3)


def test_grille_navire_est_valide_5():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    assert not grille_navire_est_valide(grille_jeu, 1, 1, SUD, 2)


def test_grille_navire_est_valide_6():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    assert not grille_navire_est_valide(grille_jeu, 1, 1, EST, 2)


def test_grille_navire_est_valide_7():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    assert not grille_navire_est_valide(grille_jeu, 4, 4, NORD, 2)


def test_grille_navire_est_valide_8():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    assert not grille_navire_est_valide(grille_jeu, 4, 4, OUEST, 2)


def test_grille_navire_est_valide_9():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    # Ajouter un obstacle pour interférence
    grille_jeu[1][1] = TIR_MANQUE

    assert not grille_navire_est_valide(grille_jeu, 1, 1, NORD, 2)


def test_grille_navire_est_valide_10():
    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    # Ajouter un obstacle pour interférence
    grille_jeu[2][1] = TIR_MANQUE

    assert not grille_navire_est_valide(grille_jeu, 1, 1, NORD, 2)


def test_grille_navire_est_valide_11():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    # Ajouter un obstacle pour interférence
    grille_jeu[1][1] = TIR_MANQUE

    assert not grille_navire_est_valide(grille_jeu, 1, 1, OUEST, 2)


def test_grille_navire_est_valide_12():
    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    # Ajouter un obstacle pour interférence
    grille_jeu[1][2] = TIR_MANQUE

    assert not grille_navire_est_valide(grille_jeu, 1, 1, OUEST, 2)


def test_grille_navire_est_valide_13():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    # Ajouter un obstacle pour interférence
    grille_jeu[1][1] = TIR_MANQUE

    assert not grille_navire_est_valide(grille_jeu, 1, 2, EST, 2)


def test_grille_navire_est_valide_14():
    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    # Ajouter un obstacle pour interférence
    grille_jeu[1][2] = TIR_MANQUE

    assert not grille_navire_est_valide(grille_jeu, 1, 2, EST, 2)


def test_grille_navire_est_valide_15():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    # Ajouter un obstacle pour interférence
    grille_jeu[1][1] = TIR_MANQUE

    assert not grille_navire_est_valide(grille_jeu, 2, 1, SUD, 2)


def test_grille_navire_est_valide_16():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    # Ajouter un obstacle pour interférence
    grille_jeu[2][1] = TIR_MANQUE

    assert not grille_navire_est_valide(grille_jeu, 2, 1, SUD, 2)


def test_grille_navire_est_valide_17():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    # Ajouter un obstacle pour interférence
    grille_jeu[1][1] = TIR_MANQUE

    assert grille_navire_est_valide(grille_jeu, 1, 2, OUEST, 2)


def test_grille_navire_est_valide_18():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    # Ajouter un obstacle pour interférence
    grille_jeu[1][1] = TIR_MANQUE

    assert grille_navire_est_valide(grille_jeu, 2, 1, OUEST, 2)


def test_grille_generer_orientation_aleatoire_valide_1():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    # Remplir le tableau d'artéfacts pour qu'il ne reste que la position NORD de valide
    grille_jeu[1][1] = BATEAU_VIVANT
    grille_jeu[2][1] = BATEAU_VIVANT
    grille_jeu[3][1] = BATEAU_VIVANT

    grille_jeu[3][3] = BATEAU_VIVANT
    grille_jeu[3][3] = BATEAU_VIVANT
    grille_jeu[3][3] = BATEAU_VIVANT

    # Générer une orientation aléatoire
    orientation_obtenue = grille_generer_orientation_aleatoire_valide(grille_jeu, 1, 2, 3)

    # Il ne reste que la position NORD de valide
    orientation_attendue = NORD

    assert orientation_attendue == orientation_obtenue


def test_grille_generer_orientation_aleatoire_valide_2():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    # Remplir le tableau d'artéfacts pour qu'il ne reste que la position SUD de valide
    grille_jeu[1][1] = BATEAU_VIVANT
    grille_jeu[2][1] = BATEAU_VIVANT
    grille_jeu[3][1] = BATEAU_VIVANT

    grille_jeu[3][3] = BATEAU_VIVANT
    grille_jeu[3][3] = BATEAU_VIVANT
    grille_jeu[3][3] = BATEAU_VIVANT

    # Générer une orientation aléatoire
    orientation_obtenue = grille_generer_orientation_aleatoire_valide(grille_jeu, 3, 2, 3)

    # Il ne reste que la position SUD de valide
    orientation_attendue = SUD

    assert orientation_attendue == orientation_obtenue


def test_grille_generer_orientation_aleatoire_valide_3():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    # Remplir le tableau d'artéfacts pour qu'il ne reste que la position OUEST de valide
    grille_jeu[1][1] = BATEAU_VIVANT
    grille_jeu[1][2] = BATEAU_VIVANT
    grille_jeu[1][3] = BATEAU_VIVANT

    grille_jeu[3][1] = BATEAU_VIVANT
    grille_jeu[3][2] = BATEAU_VIVANT
    grille_jeu[3][3] = BATEAU_VIVANT

    # Générer une orientation aléatoire
    orientation_obtenue = grille_generer_orientation_aleatoire_valide(grille_jeu, 2, 1, 3)

    # Il ne reste que la position OUEST de valide
    orientation_attendue = OUEST

    assert orientation_attendue == orientation_obtenue


def test_grille_generer_orientation_aleatoire_valide_4():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    # Remplir le tableau d'artéfacts pour qu'il ne reste que la position EST de valide
    grille_jeu[1][1] = BATEAU_VIVANT
    grille_jeu[1][2] = BATEAU_VIVANT
    grille_jeu[1][3] = BATEAU_VIVANT

    grille_jeu[3][1] = BATEAU_VIVANT
    grille_jeu[3][2] = BATEAU_VIVANT
    grille_jeu[3][3] = BATEAU_VIVANT

    # Générer une orientation aléatoire
    orientation_obtenue = grille_generer_orientation_aleatoire_valide(grille_jeu, 2, 3, 3)

    # Il ne reste que la position EST de valide
    orientation_attendue = EST

    assert orientation_attendue == orientation_obtenue


def test_grille_generer_orientation_aleatoire_valide_5():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    # Remplir le tableau entier d'artéfacts pour qu'il ne reste plus d'orientation valide
    grille_jeu[1][1] = BATEAU_VIVANT
    grille_jeu[1][2] = BATEAU_VIVANT
    grille_jeu[1][3] = BATEAU_VIVANT

    grille_jeu[2][1] = BATEAU_VIVANT
    grille_jeu[2][2] = BATEAU_VIVANT
    grille_jeu[2][3] = BATEAU_VIVANT

    grille_jeu[3][1] = BATEAU_VIVANT
    grille_jeu[3][2] = BATEAU_VIVANT
    grille_jeu[3][3] = BATEAU_VIVANT

    try:

        # La fonction doit échouer puisqu'il n'y a aucune orientation valide
        _ = grille_generer_orientation_aleatoire_valide(grille_jeu, 2, 3, 3)

    except AssertionError as err:

        assert err.args[0] == 'Nombre d\'itérations maximal atteint.'
        return

    assert False, 'Aucune erreur ne fut déclenchée'


def test_grille_ajouter_navire_1():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    # Navire de référence
    navire = {'taille': 2, 'vie': 2, 'i': 1, 'j': 1, 'orientation': OUEST, 'positions': [(1, 1), (1, 2)]}

    # Ajouter le navire à la grille de jeu
    grille_ajouter_navire(grille_jeu, navire)

    # Générer la grille attendue
    grille_attendue = grille_initialiser(5, 5)

    grille_attendue[1][1] = POINTE_OUEST
    grille_attendue[1][2] = BATEAU_VIVANT

    assert len(DeepDiff(grille_jeu, grille_attendue)) == 0


def test_grille_ajouter_navire_2():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    # Navire de référence
    navire = {'taille': 2, 'vie': 2, 'i': 1, 'j': 1, 'orientation': NORD, 'positions': [(1, 1), (2, 1)]}

    # Ajouter le navire à la grille de jeu
    grille_ajouter_navire(grille_jeu, navire)

    # Générer la grille attendue
    grille_attendue = grille_initialiser(5, 5)

    grille_attendue[1][1] = POINTE_NORD
    grille_attendue[2][1] = BATEAU_VIVANT

    assert len(DeepDiff(grille_jeu, grille_attendue)) == 0


def test_grille_ajouter_navire_3():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    # Navire de référence
    navire = {'taille': 2, 'vie': 2, 'i': 1, 'j': 2, 'orientation': EST, 'positions': [(1, 2), (1, 1)]}

    # Ajouter le navire à la grille de jeu
    grille_ajouter_navire(grille_jeu, navire)

    # Générer la grille attendue
    grille_attendue = grille_initialiser(5, 5)

    grille_attendue[1][1] = BATEAU_VIVANT
    grille_attendue[1][2] = POINTE_EST

    assert len(DeepDiff(grille_jeu, grille_attendue)) == 0


def test_grille_ajouter_navire_4():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    # Navire de référence
    navire = {'taille': 2, 'vie': 2, 'i': 2, 'j': 1, 'orientation': SUD, 'positions': [(2, 1), (1, 1)]}

    # Ajouter le navire à la grille de jeu
    grille_ajouter_navire(grille_jeu, navire)

    # Générer la grille attendue
    grille_attendue = grille_initialiser(5, 5)

    grille_attendue[1][1] = BATEAU_VIVANT
    grille_attendue[2][1] = POINTE_SUD

    assert len(DeepDiff(grille_jeu, grille_attendue)) == 0


def test_grille_gestionnaire_tir_1():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    # Ajouter un navire
    grille_jeu[1][1] = BATEAU_VIVANT
    grille_jeu[2][1] = BATEAU_VIVANT

    # Tirer sur le navire
    grille_gestionnaire_tir(grille_jeu, 1, 1)

    # Grille de référence
    grille_reference = grille_initialiser(5, 5)

    # Ajouter un navire
    grille_reference[1][1] = BATEAU_ATTEINT
    grille_reference[2][1] = BATEAU_VIVANT

    assert len(DeepDiff(grille_jeu, grille_reference)) == 0


def test_grille_gestionnaire_tir_2():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    # Ajouter un navire
    grille_jeu[1][1] = BATEAU_VIVANT
    grille_jeu[2][1] = BATEAU_VIVANT

    # Tirer sur le navire
    grille_gestionnaire_tir(grille_jeu, 1, 2)

    # Grille de référence
    grille_reference = grille_initialiser(5, 5)

    # Ajouter un navire
    grille_reference[1][1] = BATEAU_VIVANT
    grille_reference[2][1] = BATEAU_VIVANT
    grille_reference[1][2] = TIR_MANQUE

    assert len(DeepDiff(grille_jeu, grille_reference)) == 0


def test_grille_adversaire_gestionnaire_tir_1():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    # Ajouter un navire
    grille_jeu[1][1] = BATEAU_VIVANT
    grille_jeu[2][1] = BATEAU_VIVANT

    # Tirer sur le navire
    grille_adversaire_gestionnaire_tir(grille_jeu, 1, 1, True)

    # Grille de référence
    grille_reference = grille_initialiser(5, 5)

    # Ajouter un navire
    grille_reference[1][1] = BATEAU_ATTEINT
    grille_reference[2][1] = BATEAU_VIVANT

    assert len(DeepDiff(grille_jeu, grille_reference)) == 0


def test_grille_adversaire_gestionnaire_tir_2():

    # Grille de référence
    grille_jeu = grille_initialiser(5, 5)

    # Ajouter un navire
    grille_jeu[1][1] = BATEAU_VIVANT
    grille_jeu[2][1] = BATEAU_VIVANT

    # Tirer sur le navire
    grille_adversaire_gestionnaire_tir(grille_jeu, 1, 2, False)

    # Grille de référence
    grille_reference = grille_initialiser(5, 5)

    # Ajouter un navire
    grille_reference[1][1] = BATEAU_VIVANT
    grille_reference[2][1] = BATEAU_VIVANT
    grille_reference[1][2] = TIR_MANQUE

    assert len(DeepDiff(grille_jeu, grille_reference)) == 0
