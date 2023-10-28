"""Fichier source de la SAE 1.01 partie 1"""

# Importations
import os
from pathlib import Path

import histoire2foot

# Constantes
CHEMIN_CSV = Path(__file__).parent / "csv"

# Fonctions
def clear() -> None:
    """Nettoie le terminale. En fonction du système d'exploitation, utilise la commande 'cls' ou 'clear'."""
    os.system('cls' if os.name == 'nt' else 'clear')


def recup_fichiers(chemin: Path = CHEMIN_CSV) -> list:
    """Retourne la liste des fichier csv dans l'emplacement passé en paramètre.

    Args:
        chemin (str, optional): Emplacement des fichiers csv. Defaults to "".

    Returns:
        list: La liste des fichiers csv.
    """

    liste_fichiers = [] # Invariant de boucle: liste les fichiers csv déjà parcourus dans le dossier

    for fichier in os.listdir(chemin):
        if fichier.endswith(".csv"):
            liste_fichiers.append(fichier)

    return liste_fichiers


def demander_entier(texte: str, minimum: int = float("-inf"), maximum: int = float("inf")) -> int:
    """Demande un entier à l'utilisateur dans une certaine intervalle, 
    boucle tant que l'utilisateur ne rentre pas un entier valide.

    Args:
        texte (str): Texte à afficher à l'utilisateur.
        minimum (int, optional): Minimum de l'intervalle inclu. Defaults to float("-inf").
        minimum (int, optional): Maximum de l'intervalle inclu. Defaults to float("inf").

    Returns:
        int: L'entier que l'utilisateur à rentré.
    """

    reponse = input(texte)

    # Demande à l'utilisteur un nouveau nombre, tant que celui-ci n'est pas un entier ou n'est pas dans l'intervalle
    while not histoire2foot.est_un_entier(reponse, minimum, maximum):
        print("Choix invalide.")
        reponse = input(texte)

    return int(reponse)


def afficher_liste_matchs(liste_matchs: list) -> None:
    """Affiche une liste de matchs sous forme de tableau. 

    Args:
        liste_matchs (list): Liste de matchs.
    """
    # Ne fait rien si la liste est vide
    if len(liste_matchs) == 0:
        return 

    # Affiche l'entête, colonne par colonne en les centrant
    print("N°", end=" | ")
    print("Date".center(11), end=" | ")
    print("Equipe 1".center(11), end=" | ")
    print("Equipe 2".center(11), end=" | ")
    print("Score".center(10), end=" | ")
    print("Competition".center(16), end=" | ")
    print("Ville".center(16), end=" | ")
    print("Pays".center(16))
    
    # Affiche les matchs, colonne par colonne en les centrant
    for i, match in enumerate(liste_matchs):
        print(f"{i + 1} ", end=" | ")
        print(match[0].center(11), end=" | ")

        equipe1 = f"{match[1][:8].strip()}..." if len(match[1]) > 13 else match[1]
        print(equipe1.center(11), end=" | ")

        equipe2 = f"{match[2][:8].strip()}..." if len(match[2]) > 13 else match[2]
        print(equipe2.center(11), end=" | ")

        print(f"{match[3]}-{match[4]}".center(10), end=" | ")

        competition = f"{match[5][:11].strip()}..." if len(match[5]) > 15 else match[5]
        print(competition.center(16), end=" | ")

        ville = f"{match[6][:9].strip()}..." if len(match[6]) > 13 else match[6]
        print(ville.center(16), end=" | ")

        pays = f"{match[7][:9].strip()}..." if len(match[7]) > 13 else match[7]
        print(pays.center(16))
        

def afficher_liste_numerotee(liste: list) -> None:
    """Affiche une liste numérotée à partir de 1.

    Args:
        liste (list): Liste à afficher
    """

    for i, fichier in enumerate(liste):
        print(f" {i + 1}. {fichier}")


def afficher_logo() -> None:
    """Affiche le logo du programme."""

    print("""\033[0;34m
    __  ___      __        _          ___   ______            __ 
   / / / (_)____/ /_____  (_)_______ |__ \ / ____/___  ____  / /_
  / /_/ / / ___/ __/ __ \/ / ___/ _ \__/ // /_  / __ \/ __ \/ __/
 / __  / (__  ) /_/ /_/ / / /  /  __/ __// __/ / /_/ / /_/ / /_  
/_/ /_/_/____/\__/\____/_/_/   \___/____/_/    \____/\____/\__/                                                         
\033[0m""")


def menu(liste_matchs: list, logo: bool=True) -> None:
    """Affiche le menu et demande à l'utilisateur quelle action effectuer.

    Args:
        liste_matchs (list): Une liste de matchs
        logo (bool, optional): Affiche le logo. Defaults to True.
    """

    clear()
    afficher_logo()

    # Affiche le menu, avec le titre en couleur
    print("\033[0;34mVoici la liste des actions possibles : \033[0m")
    print(" 1. Consulter les statistiques d'un match")
    print(" 2. Consulter les statistiques d'une équipe")
    print(" 3. Consulter les statistiques d'une compétition")
    print(" 4. Consulter les statistiques d'une ville")
    print(" 5. Consulter les statistiques globales")
    print(" 6. Charger un autre fichier .csv")
    print(" 7. Quitter\n")

    # Demande à l'utilisateur quelle option choisir
    categorie = demander_entier("Que voulez-vous faire (1:6)? ", 1, 7)
    clear()
    match categorie:
        case 1:
            stats_matchs(liste_matchs)
        case 2:
            stats_equipes(liste_matchs)
        case 3:
            stats_competition(liste_matchs)
        case 4:
            stats_ville(liste_matchs)
        case 5:
            stats_globales(liste_matchs)
        case 6:
            charger_csv()
        case _:
            return 


def stats_matchs(liste_matchs: list) -> None:
    """Demande à l'utilisateur une date, affiche tout les matchs de cette date, 
    puis demande à l'utilisateur quel match consulter, et affiche les stats de celui-ci.
    
    Args:
        liste_matchs (list): Une liste de matchs.
    """

    # Demande à l'utilisateur une date
    exemples = list(map(lambda match: match[0], liste_matchs[:3]))
    date = input(f"Entrez une date (Exemples : {', '.join(exemples)}) : ")
    liste_matchs_filtre = list(histoire2foot.rechercher_par_date(liste_matchs, date))

    # Verifie si un match existe à cette date, retourne au menu sinon
    if len(liste_matchs_filtre) == 0:
        print("\nAucun match trouvé.")
        
        # Demande à l'utilisateur si il veut consulter un autre match
        if input("Voulez-vous consulter un autre match (O/N) ? ").lower() == "o":
            stats_matchs(liste_matchs)
        else:
            menu(liste_matchs)

        return
    
    # Affiche les matchs de la date
    print(f"\n\033[0mVoici les matchs du {date} : \033[0m")
    afficher_liste_matchs(liste_matchs_filtre)

    # Demande à l'utilisateur quel match consulter
    numero_match = demander_entier(f"\nQuel match souhaitez-vous consulter (1:{len(liste_matchs_filtre)}) ? ", 1, len(liste_matchs_filtre))
    match = liste_matchs_filtre[numero_match - 1]

    # Recupère les stats du match
    equipe_gagnante = histoire2foot.equipe_gagnante(match)
    equipe_gagnante = "Aucune" if equipe_gagnante is None else equipe_gagnante

    victoire_a_domicile = "Oui" if histoire2foot.victoire_a_domicile(match) else "Non"
    nb_buts = histoire2foot.nb_buts_marques(match)

    # Affiche les stats du match
    print(f"\n\033[0;34m{match[5]} - {match[1]} contre {match[2]} du {match[0]}\033[0m")
    print(f" Score : {match[3]}-{match[4]}")
    print(f" Nombre de buts marqués : {nb_buts}")
    print(f" Equipe gagnante : {equipe_gagnante}")
    print(f" Victoire à domicile : {victoire_a_domicile}\n")
    print(f" Lieu : {match[6]} ({match[7]})")
    
    # Demande à l'utilisateur si il veut consulter un autre match
    if input("\nVoulez-vous consulter un autre match (O/N) ? ").lower() == "o":
        stats_matchs(liste_matchs)
    else:
        menu(liste_matchs)


def stats_equipes(liste_matchs: list) -> None:
    """Demande à l'utilisateur le nom d'une équipe, affiche les stats de l'équipe.

    Args:
        liste_matchs (list): Une liste de matchs.
    """

    liste_equipes = histoire2foot.liste_des_equipes(liste_matchs)
    nom_equipe = input(f"Entrez le nom d'une équipe (Exemples : {', '.join(liste_equipes[:3])}) : ")

    # Verifie si l'équipe existe, retourne au menu sinon
    if nom_equipe not in liste_equipes:
        print("\nCette équipe n'existe pas.")
        
        # Demande à l'utilisateur si il veut consulter une autre équipe
        if input("\nVoulez-vous consulter une autre équipe (O/N) ? ").lower() == "o":
            stats_equipes(liste_matchs)
        else:
            menu(liste_matchs)

        return
    
    # Recupère les stats de l'équipe
    resultats = histoire2foot.resultats_equipe(liste_matchs, nom_equipe)
    
    liste_filtree = filter(lambda match: match[1] == nom_equipe or match[2] == nom_equipe, liste_matchs)
    nb_buts = histoire2foot.nb_but(liste_filtree)
    nb_buts_moyen = histoire2foot.nombre_moyen_buts(liste_filtree)

    premire_victoire = histoire2foot.premiere_victoire(liste_matchs, nom_equipe)
    nb_matchs_sans_defaites = histoire2foot.nb_matchs_sans_defaites(liste_matchs, nom_equipe)
    
    # Affiche les stats de l'équipe
    print(f"\n\033[0;34m{nom_equipe}\033[0m")
    print(f" Nombre de matchs joués : {resultats[0] + resultats[1] + resultats[2]}")
    print(f" Nombre de buts marqués : {nb_buts}")
    print(f" Nombre moyen de buts marqués par match : {nb_buts_moyen}")
    if premire_victoire is not None:
        print(f" Première victoire : {premire_victoire}")
        print(f" Recors de victoires consécutives : {nb_matchs_sans_defaites}")
    
    print(f" Nombre de victoires : {resultats[0]}")
    print(f" Nombre de matchs nuls : {resultats[1]}")
    print(f" Nombre de défaites : {resultats[2]}")

    # Demande à l'utilisateur si il veut consulter une autre équipe
    if input("\nVoulez-vous consulter une autre équipe (O/N) ? ").lower() == "o":
        stats_equipes(liste_matchs)
    else:
        menu(liste_matchs)


def stats_competition(liste_matchs: list) -> None:
    """Demande à l'utilisateur le nom d'une compétition, affiche les stats de la compétition.

    Args:
        liste_matchs (list): Une liste de matchs.
    """

    liste_competitions = list(histoire2foot.ensemble_des_competitions(liste_matchs))
    nom_competition = input(f"Entrez le nom d'une compétition (Exemples : {', '.join(liste_competitions[:3])}  ) : ")

    # Verifie si la compétition existe, retourne au menu sinon
    if nom_competition not in liste_competitions:
        print("\nCette compétition n'existe pas.")
        
        # Demande à l'utilisateur si il veut consulter une autre compétition
        if input("\nVoulez-vous consulter une autre compétition (O/N) ? ").lower() == "o":
            stats_competition(liste_matchs)
        else:
            menu(liste_matchs)

        return
    
    # Fait l'affichage des stats de la compétition
    print(f"\n{nom_competition}")
    afficher_stats(list(filter(lambda match: match[5] == nom_competition, liste_matchs)))

    # Demande à l'utilisateur si il veut consulter une autre compétition
    if input("\nVoulez-vous consulter une autre compétition (O/N) ? ").lower() == "o":
        stats_competition(liste_matchs)
    else:
        menu(liste_matchs)


def stats_ville(liste_matchs: list) -> None:
    """Demande à l'utilisateur le nom d'une ville, affiche les stats de la ville.

    Args:
        liste_matchs (list): Une liste de matchs.
    """

    liste_villes = list(histoire2foot.ensemble_des_villes(liste_matchs))
    nom_ville = input(f"Entrez le nom d'une ville (Exemples : {', '.join(liste_villes[:3])}) : ")

    # Verifie si la ville existe, retourne au menu sinon
    if nom_ville not in liste_villes:
        print("\nCette ville n'existe pas.")
        
        # Demande à l'utilisateur si il veut consulter une autre ville
        if input("\nVoulez-vous consulter une autre ville (O/N) ? ").lower() == "o":
            stats_ville(liste_matchs)
        else:
            menu(liste_matchs)

        return
    
    # Fait l'affichage des stats de la ville
    print(f"\n{nom_ville}")
    afficher_stats(list(filter(lambda match: match[6] == nom_ville, liste_matchs)))

    # Demande à l'utilisateur si il veut consulter une autre ville
    if input("Voulez-vous consulter une autre ville (O/N) ? ").lower() == "o":
        stats_ville(liste_matchs)
    else:
        menu(liste_matchs)


def afficher_stats(liste_matchs: list) -> None:
    """Affiche les statistiques d'une liste de matchs.

    Args:
        liste_matchs (list): Une liste de matchs.
    """

    nb_matchs = len(liste_matchs)
    nb_buts = histoire2foot.nb_but(liste_matchs)
    nombre_moyen_buts = round(histoire2foot.nombre_moyen_buts(liste_matchs), 3)

    matchs_spectaculaires = histoire2foot.matchs_spectaculaires(liste_matchs)
    plus_gros_scores = histoire2foot.plus_gros_scores(liste_matchs)
    meilleures_equipes = histoire2foot.meilleures_equipes(liste_matchs)

    # Affiche les stats des matchs
    print(f" Nombre de matchs joués : {nb_matchs}")
    print(f" Nombre de buts marqués : {nb_buts}")
    print(f" Nombre moyen de buts par match : {nombre_moyen_buts}")

    print(f"\nLes matchs avec le plus grand nombre de buts marqués : ")
    afficher_liste_matchs(matchs_spectaculaires)


    print(f"\nLes matchs avec le plus grand écart entre le gagnant et le perdant sont : ")
    afficher_liste_matchs(plus_gros_scores)

    print(f"\nLes équipe avec le moins de défaites sont : ")
    afficher_liste_numerotee(meilleures_equipes)


def stats_globales(liste_matchs: list) -> None:
    """Affiche les statistiques globales.

    Args:
        liste_matchs (list): Une liste de matchs.
    """

    # Affiche les stats globales
    print("\033[0;34mVoici les statistiques globales : \033[0m")
    afficher_stats(liste_matchs)
    input("\nAppuyez sur entrée pour revenir au menu ")
    menu(liste_matchs)


def charger_csv() -> None:
    """Affiche les fichiers csv disponibles, charge celui choisi par l'utilisateur, et affiche le menu."""

    # Affiche la liste des fichiers
    liste_fichiers = recup_fichiers()

    if len(liste_fichiers) == 0:
        print("\033[91mAucun fichier .csv trouvé. \033[0m")
        return

    print("\033[0;34mVoici la liste des fichiers .csv disponibles : \033[0m")
    afficher_liste_numerotee(liste_fichiers)

    # Demande à l'utilisateur quel fichier choisir
    numero_fichier = demander_entier(f"\nQuel fichier .csv souhaitez-vous consulter (1:{len(liste_fichiers)}) ? ", 1, len(liste_fichiers))

    # Charge le fichier
    liste_matchs = histoire2foot.charger_matchs(CHEMIN_CSV / liste_fichiers[numero_fichier - 1])
    print(f"{len(liste_matchs)} matchs chargés.")

    menu(liste_matchs)

# ici votre programme principal
def programme_principal() -> None:
    """Programme principal."""

    clear()
    afficher_logo()
    charger_csv()

# Execution du programme principal
if __name__ == "__main__":
    programme_principal()
