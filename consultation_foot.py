import os
import sys

import histoire2foot


# Ici vos fonctions dédiées aux interactions
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def recup_fichiers():
    liste_fichiers = []

    for fichier in os.listdir():
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


def stats_matchs():
    pass


def stats_equipes():
    pass


def stats_competition():
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
    liste_fichiers = recup_fichiers()

    if len(liste_fichiers) == 0:
        print("\033[91mAucun fichier .csv trouvé. \033[0m")
        sys.exit()

    print("Voici la liste des fichiers .csv disponibles : ")
    for i, fichier in enumerate(recup_fichiers()):
        print(f" {i + 1}. {fichier}")

    # Demande à l'utilisateur quel fichier choisir
    numero_fichier = demander_entier("\nQuel fichier .csv souhaitez-vous consulter ? ", 1, len(liste_fichiers))

    # Charge le fichier
    fichier = histoire2foot.charger_matchs(liste_fichiers[numero_fichier - 1])

    # Affiche le menu
    print("\nVoici la liste des actions possibles : ")
    print(" 1. Consulter les statistiques d'un match")
    print(" 2. Consulter les statistiques d'une équipe")
    print(" 3. Consulter les statistiques d'une compétition")

    # Demande à l'utilisateur quelle option choisir
    categorie = demander_entier("Que voulez-vous faire ? ", 1, 3)
    [stats_matchs, stats_equipes, stats_competition][categorie]()


if __name__ == "__main__":
    programme_principal()
