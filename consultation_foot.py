import os
import sys
from pathlib import Path

import histoire2foot

# Constantes
CHEMIN_CSV = Path(__file__).parent / "csv"

# Fonctions
def clear() -> None:
    """Nettoie le terminale."""
    os.system('cls' if os.name == 'nt' else 'clear')


def recup_fichiers(chemin: Path = CHEMIN_CSV) -> list:
    """Retourne la liste des fichier csv dans l'emplacement passé en paramètre.

    Args:
        chemin (str, optional): Emplacement des fichiers csv. Defaults to "".

    Returns:
        list: La liste des fichiers csv.
    """

    liste_fichiers = []

    for fichier in os.listdir(chemin):
        if fichier.endswith(".csv"):
            liste_fichiers.append(fichier)

    return liste_fichiers


def demander_entier(texte: str, debut: int = float("-inf"), fin: int = float("inf")) -> int:
    """Demande un entier à l'utilisateur dans une certaine intervalle, 
    boucle tant que l'utilisateur ne rentre pas un entier valide.

    Args:
        texte (str): Texte à afficher à l'utilisateur.
        debut (float, optional): Debut de l'intervalle inclu. Defaults to float("-inf").
        fin (float, optional): Fin de l'intervalle inclu. Defaults to float("inf").

    Returns:
        int: L'entier que l'utilisateur à rentré.
    """

    reponse = input(texte)

    while not reponse.isnumeric() or debut > int(reponse) or int(reponse) > fin:
        print("Choix invalide.")
        reponse = input(texte)

    return int(reponse)


def afficher_liste_numerotee(liste: list) -> None:
    """Affiche une liste numérotée.

    Args:
        liste (list): Liste.
    """

    for i, fichier in enumerate(liste):
        print(f" {i + 1}. {fichier}")


def stats_matchs(liste_matchs: list):
    pass


def stats_equipes(liste_matchs: list):
    pass


def stats_competition(liste_matchs: list):
    pass


# ici votre programme principal
def programme_principal():
    # Affichage du titre
    clear()
    print("""\033[0;34m
    __  ___      __        _          ___   ______            __ 
   / / / (_)____/ /_____  (_)_______ |__ \ / ____/___  ____  / /_
  / /_/ / / ___/ __/ __ \/ / ___/ _ \__/ // /_  / __ \/ __ \/ __/
 / __  / (__  ) /_/ /_/ / / /  /  __/ __// __/ / /_/ / /_/ / /_  
/_/ /_/_/____/\__/\____/_/_/   \___/____/_/    \____/\____/\__/                                                         
\033[0m""")

    # Affiche la liste des fichiers
    liste_fichiers = recup_fichiers(chemin=Path(__file__) / "csv")

    if len(liste_fichiers) == 0:
        print("\033[91mAucun fichier .csv trouvé. \033[0m")
        sys.exit()

    print("Voici la liste des fichiers .csv disponibles : ")
    afficher_liste_numerotee(liste_fichiers)

    # Demande à l'utilisateur quel fichier choisir
    numero_fichier = demander_entier("\nQuel fichier .csv souhaitez-vous consulter ? ", 1, len(liste_fichiers))

    # Charge le fichier
    liste_matchs = histoire2foot.charger_matchs(CHEMIN_CSV / liste_fichiers[numero_fichier - 1])
    print(f"{len(liste_fichiers)} matchs chargés. \n")
    
    # Affiche le menu
    print("\nVoici la liste des actions possibles : ")
    print(" 1. Consulter les statistiques d'un match")
    print(" 2. Consulter les statistiques d'une équipe")
    print(" 3. Consulter les statistiques d'une compétition\n")

    # Demande à l'utilisateur quelle option choisir
    categorie = demander_entier("Que voulez-vous faire ? ", 1, 3)
    [stats_matchs, stats_equipes, stats_competition][categorie - 1](liste_matchs)


if __name__ == "__main__":
    programme_principal()
