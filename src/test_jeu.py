# Pour capturer le contenu de stdout
import sys
import io

# Importer les librairies à tester
from jeu import jeu_afficher_joueur_courant
from jeu import jeu_joueur_saisir_position_tir
from jeu import jeu_est_partie_terminee
from jeu import jeu_afficher_vainqueur

# Constantes qui représentent le joueur courant
from constantes import JOUEUR
from constantes import ORDINATEUR


def test_jeu_afficher_joueur_courant_1(capsys):
    """
    Vérifie l'affichage du joueur courant lorsqu'il s'agit du joueur.
    """

    # Appeler la procédure à tester
    jeu_afficher_joueur_courant(JOUEUR)

    # On s'attend à recevoir le message spécifié dans l'énoncé
    resultat_attendu = 'C\'est au tour du joueur\n'

    # Capturer le contenu de stdout
    contenu_stdout = capsys.readouterr()

    assert contenu_stdout.out == resultat_attendu


def test_jeu_afficher_joueur_courant_2(capsys):
    """
    Vérifie l'affichage du joueur courant lorsqu'il s'agit de l'ordinateur.
    """

    # Appeler la procédure à tester
    jeu_afficher_joueur_courant(ORDINATEUR)

    # On s'attend à recevoir le message spécifié dans l'énoncé
    resultat_attendu = 'C\'est au tour de l\'ordinateur\n'

    # Capturer le contenu de stdout
    contenu_stdout = capsys.readouterr()

    assert contenu_stdout.out == resultat_attendu


def test_jeu_joueur_saisir_position_tir_1(capsys):
    """
    Vérifie la position du tir retournée par saisie du joueur.
    """

    # Mettre une position valide dans stdin
    sys.stdin = io.StringIO('1\n1\n')

    # On s'attend à ce qu'il nous retourne la position qu'on lui a fournie
    resultat_attendu = (1, 1)

    # Obtenir la position
    position = jeu_joueur_saisir_position_tir()

    # Capturer le contenu de stdout
    _ = capsys.readouterr()

    assert position == resultat_attendu


def test_jeu_joueur_saisir_position_tir_2(capsys):
    """
    Vérifie l'affichage de la saisie de la position du tir du joueur.
    """

    # Mettre une position valide dans stdin
    sys.stdin = io.StringIO('1\n1\n')

    # On s'attend à ce qu'il nous retourne la position qu'on lui a fournie
    resultat_attendu = 'Saisir la ligne (i) du tir [1, 8]: Saisir la colonne (j) du tir [1, 8]: '

    # Mettre une position valide dans stdin
    sys.stdin = io.StringIO('1\n1\n')

    # Obtenir la position
    _ = jeu_joueur_saisir_position_tir()

    # Capturer le contenu de stdout
    contenu_stdout = capsys.readouterr()

    assert contenu_stdout.out == resultat_attendu


def test_jeu_est_partie_terminee_1():
    """
    Vérifie que la partie n'est pas terminée quand les deux joueurs sont encore en vie.
    """

    # Flottes de test
    flotte_1 = [{'taille': 2, 'vie': 2, 'i': None, 'j': None, 'orientation': None, 'positions': []},
                {'taille': 5, 'vie': 5, 'i': None, 'j': None, 'orientation': None, 'positions': []}]

    flotte_2 = [{'taille': 2, 'vie': 2, 'i': None, 'j': None, 'orientation': None, 'positions': []},
                {'taille': 5, 'vie': 5, 'i': None, 'j': None, 'orientation': None, 'positions': []}]

    # On s'attend à ce que la partie ne soit pas terminée
    resultat_attendu = False

    # Vérifier si la partie est terminée
    est_partie_terminee = jeu_est_partie_terminee(flotte_1, flotte_2)

    assert est_partie_terminee == resultat_attendu


def test_jeu_est_partie_terminee_2():
    """
    Vérifie que la partie est terminée quand le premier joueur n'a plus de vie.
    """

    # Flottes de test
    flotte_1 = [{'taille': 2, 'vie': 2, 'i': None, 'j': None, 'orientation': None, 'positions': []},
                {'taille': 5, 'vie': 0, 'i': None, 'j': None, 'orientation': None, 'positions': []}]

    flotte_2 = [{'taille': 2, 'vie': 2, 'i': None, 'j': None, 'orientation': None, 'positions': []},
                {'taille': 5, 'vie': 5, 'i': None, 'j': None, 'orientation': None, 'positions': []}]

    # On s'attend à ce que la partie ne soit pas terminée
    resultat_attendu = False

    # Vérifier si la partie est terminée
    est_partie_terminee = jeu_est_partie_terminee(flotte_1, flotte_2)

    assert est_partie_terminee == resultat_attendu


def test_jeu_est_partie_terminee_3():
    """
    Vérifie que la partie est terminée quand le deuxième joueur n'a plus de vie.
    """

    # Flottes de test
    flotte_1 = [{'taille': 2, 'vie': 2, 'i': None, 'j': None, 'orientation': None, 'positions': []},
                {'taille': 5, 'vie': 5, 'i': None, 'j': None, 'orientation': None, 'positions': []}]

    flotte_2 = [{'taille': 2, 'vie': 2, 'i': None, 'j': None, 'orientation': None, 'positions': []},
                {'taille': 5, 'vie': 0, 'i': None, 'j': None, 'orientation': None, 'positions': []}]

    # On s'attend à ce que la partie ne soit pas terminée
    resultat_attendu = False

    # Vérifier si la partie est terminée
    est_partie_terminee = jeu_est_partie_terminee(flotte_1, flotte_2)

    assert est_partie_terminee == resultat_attendu


def test_jeu_afficher_vainqueur_1(capsys):
    """
    Vérifie que le bon vainqueur est affiché lorsque c'est le joueur.
    """

    # Afficher le vainqueur avec une flotte joueur qui est encore en vie
    flotte_joueur = [{'taille': 2, 'vie': 2, 'i': None, 'j': None, 'orientation': None, 'positions': []},
                     {'taille': 5, 'vie': 5, 'i': None, 'j': None, 'orientation': None, 'positions': []}]

    jeu_afficher_vainqueur(flotte_joueur)

    # On s'attend à recevoir le message spécifié dans l'énoncé
    resultat_attendu = 'C\'est le joueur qui a gagné!\n'

    # Capturer le contenu de stdout
    contenu_stdout = capsys.readouterr()

    assert contenu_stdout.out == resultat_attendu


def test_jeu_afficher_vainqueur_2(capsys):
    """
    Vérifie que le bon vainqueur est affiché lorsque c'est l'ordinateur.
    """

    # Afficher le vainqueur avec une flotte joueur n'a plus de vie
    flotte_joueur = [{'taille': 2, 'vie': 0, 'i': None, 'j': None, 'orientation': None, 'positions': []},
                     {'taille': 5, 'vie': 0, 'i': None, 'j': None, 'orientation': None, 'positions': []}]

    jeu_afficher_vainqueur(flotte_joueur)

    # On s'attend à recevoir le message spécifié dans l'énoncé
    resultat_attendu = 'C\'est l\'ordinateur qui a gagné!\n'

    # Capturer le contenu de stdout
    contenu_stdout = capsys.readouterr()

    assert contenu_stdout.out == resultat_attendu
