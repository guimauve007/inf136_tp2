# Importer la librairie deepdiff pour comparer des structures imbriquées
from deepdiff import DeepDiff

# Importer la fonction seed() pour fixer la graine aléatoire
from random import seed

# Importer les fonctions à tester
from flotte import flotte_generer_aleatoire
from flotte import flotte_calculer_vie
from flotte import flotte_gestionnaire_tir


def test_flotte_generer_aleatoire():
    """
    Vérifie la génération aléatoire d'une flotte.
    """

    # Fixer la graine aléatoire
    seed(0)

    # Générer une flotte aléatoire avec la graine aléatoire fixée
    flotte = flotte_generer_aleatoire()

    # La flotte qu'on s'attend à recevoir
    flotte_attendue = [{'taille': 2, 'vie': 2, 'i': None, 'j': None, 'orientation': None, 'positions': []},
                       {'taille': 5, 'vie': 5, 'i': None, 'j': None, 'orientation': None, 'positions': []},
                       {'taille': 3, 'vie': 3, 'i': None, 'j': None, 'orientation': None, 'positions': []},
                       {'taille': 2, 'vie': 2, 'i': None, 'j': None, 'orientation': None, 'positions': []}]

    assert len(DeepDiff(flotte, flotte_attendue, ignore_order=True)) == 0


def test_flotte_calculer_vie():
    """
    Vérifie le calcul de la vie d'une flotte.
    """

    # Flotte de test
    flotte = [{'taille': 2, 'vie': 2, 'i': None, 'j': None, 'orientation': None, 'positions': []},
              {'taille': 5, 'vie': 5, 'i': None, 'j': None, 'orientation': None, 'positions': []},
              {'taille': 3, 'vie': 3, 'i': None, 'j': None, 'orientation': None, 'positions': []},
              {'taille': 2, 'vie': 2, 'i': None, 'j': None, 'orientation': None, 'positions': []}]

    # La flotte aléatoire générée à l'en-tête du fichier est 12
    resultat_attendu = 12

    assert flotte_calculer_vie(flotte) == resultat_attendu


def test_flotte_gestionnaire_tir_1():
    """
    Vérifie si une cible est atteinte lorsqu'elle le doit.
    """

    # Flotte de test
    flotte = [{'taille': 2, 'vie': 2, 'i': None, 'j': None, 'orientation': None, 'positions': [(0, 0), (0, 1)]},
              {'taille': 5, 'vie': 5, 'i': None, 'j': None, 'orientation': None, 'positions': [(1, 0), (1, 1)]}]

    # On s'attend à atteindre le premier navire
    resultat_attendu = True

    # La position du tir
    i = 0
    j = 0

    assert flotte_gestionnaire_tir(flotte, i, j) == resultat_attendu


def test_flotte_gestionnaire_tir_2():
    """
    Vérifie si une cible est atteinte lorsqu'elle ne le doit pas.
    """

    # Flotte de test
    flotte = [{'taille': 2, 'vie': 2, 'i': None, 'j': None, 'orientation': None, 'positions': [(0, 0), (0, 1)]},
              {'taille': 5, 'vie': 5, 'i': None, 'j': None, 'orientation': None, 'positions': [(1, 0), (1, 1)]}]

    # On s'attend à atteindre le premier navire
    resultat_attendu = False

    # La position du tir
    i = 0
    j = 2

    assert flotte_gestionnaire_tir(flotte, i, j) == resultat_attendu


def test_flotte_gestionnaire_tir_3():
    """
    Vérifie si la vie d'un navire est décrémentée d'une unité lorsqu'un navire est atteint.
    """

    # Flotte de test
    flotte = [{'taille': 2, 'vie': 2, 'i': None, 'j': None, 'orientation': None, 'positions': [(0, 0), (0, 1)]},
              {'taille': 5, 'vie': 5, 'i': None, 'j': None, 'orientation': None, 'positions': [(1, 0), (1, 1)]}]

    # La position du tir
    i = 0
    j = 0

    # Sauvegarder la vie des navires
    vie_navire_1 = flotte[0]['vie']

    # On s'attend à ce que la vie soit décrémentée d'une unité
    resultat_attendu = vie_navire_1 - 1

    # Effectuer le tir
    _ = flotte_gestionnaire_tir(flotte, i, j)

    assert flotte[0]['vie'] == resultat_attendu


def test_flotte_gestionnaire_tir_4():
    """
    Vérifie que seul le navire ciblé est atteint et que les autres ne le sont pas.
    """

    # Flotte de test
    flotte = [{'taille': 2, 'vie': 2, 'i': None, 'j': None, 'orientation': None, 'positions': [(0, 0), (0, 1)]},
              {'taille': 5, 'vie': 5, 'i': None, 'j': None, 'orientation': None, 'positions': [(1, 0), (1, 1)]}]

    # La position du tir
    i = 0
    j = 0

    # On s'attend à ce que le second navire demeure intact
    resultat_attendu = flotte[1]['vie']

    # Effectuer le tir
    _ = flotte_gestionnaire_tir(flotte, i, j)

    assert flotte[1]['vie'] == resultat_attendu


def test_flotte_gestionnaire_tir_5():
    """
    Vérifie si la position touchée par un tir est supprimée de la liste de positions d'un navire.
    """

    # Flotte de test
    flotte = [{'taille': 2, 'vie': 2, 'i': None, 'j': None, 'orientation': None, 'positions': [(0, 0), (0, 1)]},
              {'taille': 5, 'vie': 5, 'i': None, 'j': None, 'orientation': None, 'positions': [(1, 0), (1, 1)]}]

    # La position du tir
    i = 0
    j = 0

    # On s'attend à ce que la première position soit retirée
    resultat_attendu = [(0, 1)]

    # Effectuer le tir
    _ = flotte_gestionnaire_tir(flotte, i, j)

    assert len(DeepDiff(flotte[0]['positions'], resultat_attendu)) == 0


def test_flotte_gestionnaire_tir_6():
    """
    Vérifie si la position touchée par un tir est supprimée de la liste de positions d'un navire.
    """

    # Flotte de test
    flotte = [{'taille': 2, 'vie': 2, 'i': None, 'j': None, 'orientation': None, 'positions': [(0, 0), (0, 1)]},
              {'taille': 5, 'vie': 5, 'i': None, 'j': None, 'orientation': None, 'positions': [(1, 0), (1, 1)]}]

    # La position du tir
    i = 0
    j = 0

    # On s'attend à ce que la première position soit retirée
    resultat_attendu = [(1, 0), (1, 1)]

    # Effectuer le tir
    _ = flotte_gestionnaire_tir(flotte, i, j)

    assert len(DeepDiff(flotte[1]['positions'], resultat_attendu)) == 0
