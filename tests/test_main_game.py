# tests/test_main_game.py

import pytest

# Supposons que vous ayez une fonction main() dans main-game.py qui lance le jeu.
# Nous allons tester si cette fonction peut être appelée sans erreur.

def test_main_game_execution():
    try:
        # Si la fonction principale de votre jeu se trouve dans main_game.py,
        # assurez-vous de l'importer ici. Par exemple :
        import main_game  # Remplacez par le nom réel de votre fichier

        # Appelons la fonction main qui lance le jeu
        main_game.main()  # Remplacez par la fonction qui démarre le jeu
    except Exception as e:
        # Si une erreur se produit, le test échoue
        pytest.fail(f"Le jeu a échoué à s'exécuter : {e}")
