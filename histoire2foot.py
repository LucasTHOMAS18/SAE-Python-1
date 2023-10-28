"""Fichier source de la SAE 1.01 partie 1"""
# -----------------------------------------------------------------------------------------------------
# Import des modules
# -----------------------------------------------------------------------------------------------------
from typing import Callable

# -----------------------------------------------------------------------------------------------------
# listes des fonctions à implémenter
# -----------------------------------------------------------------------------------------------------

# Fonctions à implémenter dont les tests sont fournis
def equipe_gagnante(match: tuple) -> str:
    """retourne le nom de l'équipe qui a gagné le match. Si c'est un match nul on retourne None

    Args:
        match (tuple): un match

    Returns:
        str: le nom de l'équipe gagnante (ou None si match nul)
    """

    if match[3] > match[4]:
        return match[1]

    if match[3] < match[4]:
        return match[2]


def victoire_a_domicile(match: tuple) -> bool:
    """indique si le match correspond à une victoire à domicile

    Args:
        match (tuple): un match

    Returns:
        bool: True si le match ne se déroule pas en terrain neutre et que l'équipe qui reçoit a gagné
    """

    return equipe_gagnante(match) == match[7]


def nb_buts_marques(match: tuple) -> int:
    """indique le nombre total de buts marqués lors de ce match

    Args:
        match (tuple): un match

    Returns:
        int: le nombre de buts du match
    """

    return match[3] + match[4]


def matchs_ville(liste_matchs: list, ville: str) -> list:
    """retourne la liste des matchs qui se sont déroulés dans une ville donnée

    Args:
        liste_matchs (list): une liste de matchs
        ville (str): le nom d'une ville

    Returns:
        list: la liste des matchs qui se sont déroulé dans la ville ville
    """

    return [match for match in liste_matchs if match[6] == ville]


def nombre_moyen_buts(liste_matchs: list, nom_competition: str = None) -> float:  
    """retourne le nombre moyen de buts marqués, qui peut être filtré par compétition
    Args:
        liste_matchs (list): une liste de matchs
        nom_competition (str, optional): le nom d'une compétition. Si None, on ne filtre pas par compétition. Defaults to None.

    Returns:
        float: le nombre moyen de buts marqués lors des matchs de la compétition nom_competition (ou de tous les matchs si nom_competition est None)
    """    

    nb_match = 0
    nb_but = 0

    for match in liste_matchs:
        if nom_competition is None or match[5] == nom_competition:
            nb_match += 1
            nb_but += match[3] + match[4]

    if nb_match == 0:
        return 0.0

    return nb_but / nb_match


def est_bien_trie(liste_matchs: list) -> bool:
    """vérifie si une liste de matchs est bien trié dans l'ordre chronologique
       puis pour les matchs se déroulant le même jour, dans l'ordre alphabétique
       des équipes locales

    Args:
        liste_matchs (list): une liste de matchs

    Returns:
        bool: True si la liste est bien triée et False sinon
    """

    for i in range(1, len(liste_matchs)):
        if liste_matchs[i] < liste_matchs[i - 1]:
            return False

    return True


def fusionner_matchs(liste_matchs1: list, liste_matchs2: list) -> list:
    """Fusionne deux listes de matchs triées sans doublons en une liste triée sans doublon
    sachant qu'un même match peut être présent dans les deux listes

    Args:
        liste_matchs1 (list): la première liste de matchs
        liste_matchs2 (list): la seconde liste de matchs

    Returns:
        list: la liste triée sans doublon comportant tous les matchs de liste_matchs1 et liste_matchs2
    """

    res = []
    i = 0
    j = 0

    while i < len(liste_matchs1) and j < len(liste_matchs2):
        if liste_matchs1[i] < liste_matchs2[j]:
            if liste_matchs1[i] not in res:
                res.append(liste_matchs1[i])

            i += 1
        else:
            if liste_matchs2[j] not in res:
                res.append(liste_matchs2[j])

            j += 1

    res += liste_matchs1[i:]
    res += liste_matchs2[j:]

    return res


def resultats_equipe(liste_matchs: list, equipe: str) -> tuple:
    """donne le nombre de victoire, de matchs nuls et de défaites pour une équipe donnée

    Args:
        liste_matchs (list): une liste de matchs
        equipe (str): le nom d'une équipe (pays)

    Returns:
        tuple: un triplet d'entiers contenant le nombre de victoires, nuls et défaites de l'équipe
    """

    nb_victoires = 0
    nb_defaites = 0
    nb_nul = 0

    for match in liste_matchs:
        if equipe == match[1] or equipe == match[2]:
            gagnant = equipe_gagnante(match)

            if gagnant == equipe:
                nb_victoires += 1

            elif gagnant is None:
                nb_nul += 1

            else:
                nb_defaites += 1

    return nb_victoires, nb_nul, nb_defaites


def plus_gros_scores(liste_matchs: list):
    """retourne la liste des matchs pour lesquels l'écart de buts entre le vainqueur et le perdant est le plus grand

    Args:
        liste_matchs (list): une liste de matchs
  
    Returns:
        list: la liste des matchs avec le plus grand écart entre vainqueur et perdant
    """

    return max_liste(liste_matchs, cle=lambda match: abs(match[3] - match[4]))


def liste_des_equipes(liste_matchs :list) -> list:
    """retourne la liste des équipes qui ont participé aux matchs de la liste
    Attention on ne veut voir apparaitre le nom de chaque équipe qu'une seule fois

    Args:
        liste_matchs (list): une liste de matchs

    Returns:
        list: une liste de str contenant le noms des équipes ayant jouer des matchs
    """

    equipes = []

    for match in liste_matchs:
        if match[1] not in equipes:
            equipes.append(match[1])

        if match[2] not in equipes:
            equipes.append(match[2])

    return equipes


def premiere_victoire(liste_matchs, equipe):
    """retourne la date de la première victoire de l'equipe. Si l'equipe n'a jamais gagné de match on retourne None

    Args:
        liste_matchs (list): une liste de matchs
        equipe (str): le nom d'une équipe (pays)

    Returns:
        str: la date de la première victoire de l'equipe
    """

    for match in liste_matchs:
        if equipe_gagnante(match) == equipe:
            return match[0]


def nb_matchs_sans_defaites(liste_matchs: list, equipe: str) -> int:
    """retourne le plus grand nombre de matchs consécutifs sans défaite pour une equipe donnée.

    Args:
        liste_matchs (list): une liste de matchs
        equipe (str): le nom d'une équipe (pays)

    Returns:
        int: le plus grand nombre de matchs consécutifs sans défaite du pays nom_pays
    """

    max_nb_victoires = 0
    nb_victoires = 0

    for match in liste_matchs:
        if equipe == match[1] or equipe == match[2]:
            if equipe_gagnante(match) == equipe:
                nb_victoires += 1

            else:
                if nb_victoires > max_nb_victoires:
                    max_nb_victoires = nb_victoires

                nb_victoires = 0

    if nb_victoires > max_nb_victoires:
        max_nb_victoires = nb_victoires

    return max_nb_victoires


import csv


def charger_matchs(nom_fichier: str) -> list:
    """charge un fichier de matchs donné au format CSV en une liste de matchs

    Args:
        nom_fichier (str): nom du fichier CSV contenant les matchs

    Returns:
        list: la liste des matchs du fichier
    """
    liste = []

    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier_csv:
            reader = csv.reader(fichier_csv)
            next(reader)

            for ligne in reader:
                ligne[3] = int(ligne[3])
                ligne[4] = int(ligne[4])
                ligne[8] = ligne[8].lower() == "true"
                liste.append(tuple(ligne))
    except:
        return []

    return liste


def sauver_matchs(liste_matchs: list, nom_fichier: str) -> None:
    """sauvegarde dans un fichier au format CSV une liste de matchs

    Args:
        liste_matchs (list): la liste des matchs à sauvegarder
        nom_fichier (str): nom du fichier CSV
    """

    try:
        with open(nom_fichier, "w", newline="") as fichier_csv:
            writer = csv.writer(fichier_csv)
            writer.writerow(
                [
                    "date",
                    "home_team",
                    "away_team",
                    "home_score",
                    "away_score",
                    "tournament",
                    "city",
                    "country",
                    "neutral",
                ]
            )

            for match in liste_matchs:
                writer.writerow(match)

    except:
        print("Erreur lors de la sauvegarde des matchs")


# Fonctions à implémenter dont il faut également implémenter les tests
def plus_de_victoires_que_defaites(liste_matchs: list, equipe: str) -> bool:
    """vérifie si une équipe donnée a obtenu plus de victoires que de défaites

    Args:
        liste_matchs (list): une liste de matchs
        equipe (str): le nom d'une équipe (pays)

    Returns:
        bool: True si l'equipe a obtenu plus de victoires que de défaites
    """

    resultats = resultats_equipe(liste_matchs, equipe)
    return resultats[0] > resultats[2]


def matchs_spectaculaires(liste_matchs: list): 
    """retourne la liste des matchs les plus spectaculaires, c'est à dire les
    matchs dont le nombre total de buts marqués est le plus grand.

    Args:
        liste_matchs (list): une liste de matchs

    Returns:
        list: la liste des matchs les plus spectaculaires
    """

    return max_liste(liste_matchs, lambda match: match[3] + match[4])


def meilleures_equipes(liste_matchs: list) -> list:
    """retourne la liste des équipes de la liste qui ont le plus petit nombre de defaites.

    Args:
        liste_matchs (list): une liste de matchs

    Returns:
        list: la liste des équipes qui ont le plus petit nombre de defaites (l'ordre n'est pas garanti)
    """

    equipes = {}  # Invariant de boucle : le dictionnaire des équipes ayant le plus petit nombre de défaites parmi les equipes déjà parcourus.
    minimum = liste_matchs[0][1]  # Invairant de boucle : l'equipe avec le moins de défaites parmi les equipes déjà parcourus.

    for match in liste_matchs:
        defaite_equipe_1 = int(equipe_gagnante(match) not in {match[1], None})
        equipes[match[1]] = equipes.get(match[1], 0) + defaite_equipe_1
        minimum = min(match[1], minimum, key=lambda equipe: equipes[equipe])

        defaite_equipe_2 = int(equipe_gagnante(match) not in {match[2], None})
        equipes[match[2]] = equipes.get(match[2], 0) + defaite_equipe_2
        minimum = min(match[2], minimum, key=lambda equipe: equipes[equipe])

    return [equipe for equipe, nb_defaites in equipes.items() if nb_defaites == equipes[minimum]]


# -----------------------------------------------------------------------------------------------------
# Fonctions supplémentaires
# -----------------------------------------------------------------------------------------------------


def ensemble_des_competitions(liste_matchs: list) -> set:
    """Retourne l'ensemble des compétitions présentes dans la liste de matchs.

    Args:
        liste_matchs (list): Une liste de matchs.

    Returns:
        set: Un ensemble contenant les noms des compétitions.
    """

    return set(map(lambda match: match[5], liste_matchs))


def ensemble_des_villes(liste_matchs: list) -> set:
    """Retourne l'ensemble des villes présentes dans la liste de matchs.

    Args:
        liste_matchs (list): Une liste de matchs.

    Returns:
        set: Un ensemble contenant les noms des villes.
    """
    
    return set(map(lambda match: match[6], liste_matchs))


def rechercher_par_date(liste_matchs: list, date: str) -> list:
    """Retourne la liste des matchs s'étant déroulés à la date passée en paramètre.

    Args:
        liste_matchs (list): Une liste de matchs.
        date (str): Date au format AAAA-MM-JJ.

    Returns:
        list: La liste des matchs s'étant déroulés à la date passée en paramètre.
    """

    return list(filter(lambda match: match[0] == date, liste_matchs))


def max_liste(liste: list, cle: Callable = lambda x: x):
    """Retourne une liste d'éléments de la liste d'entrée qui ont la valeur maximale de l'attribut spécifié par la fonction clé.

    Args:
        liste (list): La liste d'entrée.
        cle (Callable, optional): La fonction utilisée pour extraire la valeur de l'attribut de chaque élément. Par défaut, lambda x: x.

    Returns:
        list: Une liste d'éléments de la liste d'entrée qui ont la valeur maximale de l'attribut spécifié par la fonction clé.
    """

    maximum = float("-inf")  # Invariant de boucle : la valeur maximale de l'attribut spécifié par la fonction clé parmi les éléments déjà parcourus.
    res = []  # Invariant de boucle : la liste des éléments ayant la valeur maximale de l'attribut spécifié par la fonction clé parmi les éléments déjà parcourus.

    for elem in liste:
        valeur_attribut = cle(elem)
        if valeur_attribut > maximum:
            res = [elem]
            maximum = valeur_attribut

        elif valeur_attribut == maximum:
            res.append(elem)

    return res


def nb_but(liste_matchs: list) -> int:
    """Retourne le nombre de buts marqués dans la liste de matchs passée en paramètre.

    Args:
        liste_matchs (list): Une liste de matchs.

    Returns:
        int: Le nombre de buts marqués lors de la compétition passée en paramètre.
    """

    nb_buts = 0  # Invariant de boucle : le nombre de buts des matchs déjà parcourus ayant eu lieu lors de la compétition passée en paramètre.
    for match in liste_matchs:
        nb_buts += nb_buts_marques(match)

    return nb_buts


def est_un_entier(chaine: str,  minimum: int = float("-inf"), maximum: int = float("inf")) -> bool:
    """Retourne True si la chaîne passée en paramètre est un entier compris entre minimum inclu et maximum inclu, False sinon.

    Args:
        chaine (str): La chaîne à tester.
        minimum (int, optional): Le minimum inclu de l'intervalle. Defaults to float("-inf").
        maximum (int, optional): Le maximum inclu de l'intervalle. Defaults to float("inf").

    Returns:
        bool: True si la chaîne passée en paramètre est un entier compris entre minimum et maximum, False sinon.
    """

    # Ignore le signe moins, puis vérifie si la chaîne est un entier compris entre minimum et maximum.
    return chaine.replace("-", "").isnumeric() and minimum <= int(chaine) <= maximum
