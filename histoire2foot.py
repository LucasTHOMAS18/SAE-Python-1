"""Fichier source de la SAE 1.01 partie 1
    Historique des matchs de football internationaux
    """

# ---------------------------------------------------------------------------------------------
# Exemples de données pour vous aider à faire des tests
# ---------------------------------------------------------------------------------------------
    
# exemples de matchs de foot
match1 = ('2021-06-28', 'France', 'Switzerland', 3, 3, 'UEFA Euro', 'Bucharest', 'Romania', True)
match2 = ('1998-07-12', 'France', 'Brazil', 3, 0, 'FIFA World Cup', 'Saint-Denis', 'France', False)
match3 = ('1978-04-05', 'Germany', 'Brazil', 0, 1, 'Friendly', 'Hamburg', 'Germany', False)

# exemples de listes de matchs de foot
liste1 = [('1970-04-08', 'France', 'Bulgaria', 1, 1, 'Friendly', 'Rouen', 'France', False), 
        ('1970-04-28', 'France', 'Romania', 2, 0, 'Friendly', 'Reims', 'France', False), 
        ('1970-09-05', 'France', 'Czechoslovakia', 3, 0, 'Friendly', 'Nice', 'France', False), 
        ('1970-11-11', 'France', 'Norway', 3, 1, 'UEFA Euro qualification', 'Lyon', 'France', False)
        ]
liste2 = [('1901-03-09', 'England', 'Northern Ireland', 3, 0, 'British Championship', 'Southampton', 'England', False), 
        ('1901-03-18', 'England', 'Wales', 6, 0, 'British Championship', 'Newcastle', 'England', False), 
        ('1901-03-30', 'England', 'Scotland', 2, 2, 'British Championship', 'London', 'England', False), 
        ('1902-05-03', 'England', 'Scotland', 2, 2, 'British Championship', 'Birmingham', 'England', False), 
        ('1903-02-14', 'England', 'Northern Ireland', 4, 0, 'British Championship', 'Wolverhampton', 'England', False), 
        ('1903-03-02', 'England', 'Wales', 2, 1, 'British Championship', 'Portsmouth', 'England', False), 
        ('1903-04-04', 'England', 'Scotland', 1, 2, 'British Championship', 'Sheffield', 'England', False), 
        ('1905-02-25', 'England', 'Northern Ireland', 1, 1, 'British Championship', 'Middlesbrough', 'England', False), 
        ('1905-03-27', 'England', 'Wales', 3, 1, 'British Championship', 'Liverpool', 'England', False), 
        ('1905-04-01', 'England', 'Scotland', 1, 0, 'British Championship', 'London', 'England', False), 
        ('1907-02-16', 'England', 'Northern Ireland', 1, 0, 'British Championship', 'Liverpool', 'England', False), 
        ('1907-03-18', 'England', 'Wales', 1, 1, 'British Championship', 'London', 'England', False), 
        ('1907-04-06', 'England', 'Scotland', 1, 1, 'British Championship', 'Newcastle', 'England', False), 
        ('1909-02-13', 'England', 'Northern Ireland', 4, 0, 'British Championship', 'Bradford', 'England', False), 
        ('1909-03-15', 'England', 'Wales', 2, 0, 'British Championship', 'Nottingham', 'England', False), 
        ('1909-04-03', 'England', 'Scotland', 2, 0, 'British Championship', 'London', 'England', False)
        ]
liste3 = [('1901-03-30', 'Belgium', 'France', 1, 2, 'Friendly', 'Bruxelles', 'Belgium', False),
        ('1901-03-30', 'England', 'Scotland', 2, 2, 'British Championship', 'London', 'England', False),
        ('1903-04-04', 'Brazil', 'Argentina', 3, 0, 'Friendly', 'Sao Paulo', 'Brazil', False),
        ('1903-04-04', 'England', 'Scotland', 1, 2, 'British Championship', 'Sheffield', 'England', False), 
        ('1970-09-05', 'France', 'Czechoslovakia', 3, 0, 'Friendly', 'Nice', 'France', False), 
        ('1970-11-11', 'France', 'Norway', 3, 1, 'UEFA Euro qualification', 'Lyon', 'France', False)
        ]
liste4 = [('1978-03-19', 'Argentina', 'Peru', 2, 1, 'Copa Ramón Castilla', 'Buenos Aires', 'Argentina', False), 
        ('1978-03-29', 'Argentina', 'Bulgaria', 3, 1, 'Friendly', 'Buenos Aires', 'Argentina', False), 
        ('1978-04-05', 'Argentina', 'Romania', 2, 0, 'Friendly', 'Buenos Aires', 'Argentina', False), 
        ('1978-05-03', 'Argentina', 'Uruguay', 3, 0, 'Friendly', 'Buenos Aires', 'Argentina', False), 
        ('1978-06-01', 'Germany', 'Poland', 0, 0, 'FIFA World Cup', 'Buenos Aires', 'Argentina', True), 
        ('1978-06-02', 'Argentina', 'Hungary', 2, 1, 'FIFA World Cup', 'Buenos Aires', 'Argentina', False), 
        ('1978-06-02', 'France', 'Italy', 1, 2, 'FIFA World Cup', 'Mar del Plata', 'Argentina', True), 
        ('1978-06-02', 'Mexico', 'Tunisia', 1, 3, 'FIFA World Cup', 'Rosario', 'Argentina', True), 
        ('1978-06-03', 'Austria', 'Spain', 2, 1, 'FIFA World Cup', 'Buenos Aires', 'Argentina', True), 
        ('1978-06-03', 'Brazil', 'Sweden', 1, 1, 'FIFA World Cup', 'Mar del Plata', 'Argentina', True), 
        ('1978-06-03', 'Iran', 'Netherlands', 0, 3, 'FIFA World Cup', 'Mendoza', 'Argentina', True), 
        ('1978-06-03', 'Peru', 'Scotland', 3, 1, 'FIFA World Cup', 'Córdoba', 'Argentina', True), 
        ('1978-06-06', 'Argentina', 'France', 2, 1, 'FIFA World Cup', 'Buenos Aires', 'Argentina', False), 
        ('1978-06-06', 'Germany', 'Mexico', 6, 0, 'FIFA World Cup', 'Córdoba', 'Argentina', True), 
        ('1978-06-06', 'Hungary', 'Italy', 1, 3, 'FIFA World Cup', 'Mar del Plata', 'Argentina', True), 
        ('1978-06-06', 'Poland', 'Tunisia', 1, 0, 'FIFA World Cup', 'Rosario', 'Argentina', True), 
        ('1978-06-07', 'Austria', 'Sweden', 1, 0, 'FIFA World Cup', 'Buenos Aires', 'Argentina', True), 
        ('1978-06-07', 'Brazil', 'Spain', 0, 0, 'FIFA World Cup', 'Mar del Plata', 'Argentina', True), 
        ('1978-06-07', 'Iran', 'Scotland', 1, 1, 'FIFA World Cup', 'Córdoba', 'Argentina', True), 
        ('1978-06-07', 'Netherlands', 'Peru', 0, 0, 'FIFA World Cup', 'Mendoza', 'Argentina', True), 
        ('1978-06-10', 'Argentina', 'Italy', 0, 1, 'FIFA World Cup', 'Buenos Aires', 'Argentina', False), 
        ('1978-06-10', 'France', 'Hungary', 3, 1, 'FIFA World Cup', 'Mar del Plata', 'Argentina', True), 
        ('1978-06-10', 'Germany', 'Poland', 1, 3, 'FIFA World Cup', 'Rosario', 'Argentina', True), 
        ('1978-06-11', 'Austria', 'Brazil', 0, 1, 'FIFA World Cup', 'Mar del Plata', 'Argentina', True), 
        ('1978-06-11', 'Iran', 'Peru', 1, 4, 'FIFA World Cup', 'Córdoba', 'Argentina', True), 
        ('1978-06-11', 'Netherlands', 'Scotland', 2, 3, 'FIFA World Cup', 'Mendoza', 'Argentina', True), 
        ('1978-06-11', 'Spain', 'Sweden', 1, 0, 'FIFA World Cup', 'Buenos Aires', 'Argentina', True), 
        ('1978-06-14', 'Argentina', 'Poland', 2, 0, 'FIFA World Cup', 'Rosario', 'Argentina', False), 
        ('1978-06-14', 'Austria', 'Netherlands', 1, 5, 'FIFA World Cup', 'Córdoba', 'Argentina', True), 
        ('1978-06-14', 'Brazil', 'Peru', 3, 0, 'FIFA World Cup', 'Mendoza', 'Argentina', True), 
        ('1978-06-14', 'Germany', 'Italy', 0, 0, 'FIFA World Cup', 'Buenos Aires', 'Argentina', True), 
        ('1978-06-18', 'Argentina', 'Brazil', 0, 0, 'FIFA World Cup', 'Rosario', 'Argentina', False), 
        ('1978-06-18', 'Austria', 'Italy', 0, 1, 'FIFA World Cup', 'Buenos Aires', 'Argentina', True), 
        ('1978-06-18', 'Germany', 'Netherlands', 2, 2, 'FIFA World Cup', 'Córdoba', 'Argentina', True), 
        ('1978-06-18', 'Peru', 'Poland', 0, 1, 'FIFA World Cup', 'Mendoza', 'Argentina', True), 
        ('1978-06-21', 'Argentina', 'Peru', 6, 0, 'FIFA World Cup', 'Rosario', 'Argentina', False), 
        ('1978-06-21', 'Austria', 'Germany', 3, 2, 'FIFA World Cup', 'Córdoba', 'Argentina', True), 
        ('1978-06-21', 'Brazil', 'Poland', 3, 1, 'FIFA World Cup', 'Mendoza', 'Argentina', True), 
        ('1978-06-21', 'Italy', 'Netherlands', 1, 2, 'FIFA World Cup', 'Buenos Aires', 'Argentina', True), 
        ('1978-06-24', 'Brazil', 'Italy', 2, 1, 'FIFA World Cup', 'Buenos Aires', 'Argentina', True), 
        ('1978-06-25', 'Argentina', 'Netherlands', 3, 1, 'FIFA World Cup', 'Buenos Aires', 'Argentina', False)
]

# -----------------------------------------------------------------------------------------------------
# listes des fonctions à implémenter
# -----------------------------------------------------------------------------------------------------

# Fonctions à implémenter dont les tests sont fournis
def equipe_gagnante(match):
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


def victoire_a_domicile(match):
    """indique si le match correspond à une victoire à domicile

    Args:
        match (tuple): un match

    Returns:
        bool: True si le match ne se déroule pas en terrain neutre et que l'équipe qui reçoit a gagné
    """    

    return equipe_gagnante(match) == match[7]


def nb_buts_marques(match):
    """indique le nombre total de buts marqués lors de ce match

    Args:
        match (tuple): un match

    Returns:
        int: le nombre de buts du match 
    """    

    return match[3] + match[4]


def matchs_ville(liste_matchs, ville):
    """retourne la liste des matchs qui se sont déroulés dans une ville donnée
    
    Args:
        liste_matchs (list): une liste de matchs
        ville (str): le nom d'une ville

    Returns:
        list: la liste des matchs qui se sont déroulé dans la ville ville    
    """

    return [match for match in liste_matchs if match[6] == ville]


def nombre_moyen_buts(liste_matchs, cle=lambda _: True): # Ajout du paramètre cle permettant de filtrer les matchs, avec autre chose que la compétition
    """retourne le nombre moyen de buts marqués, qui peut être filtré par la fonction cle
    Args:
        liste_matchs (list): une liste de matchs
        cle (function, optional): une fonction qui permet de filtrer les matchs. Par défaut, lambda _: True (tous les matchs)
    
    Returns:
        float: le nombre moyen de buts marqués, filtrés par la fonction cle
    """

    nb_match = 0
    nb_but = 0

    for match in liste_matchs:
        if cle(match):
            nb_match += 1
            nb_but += match[3] + match[4]

    if nb_match == 0:
        return 0.0
    
    return nb_but / nb_match


def est_bien_trie(liste_matchs):
    """vérifie si une liste de matchs est bien trié dans l'ordre chronologique
       puis pour les matchs se déroulant le même jour, dans l'ordre alphabétique
       des équipes locales

    Args:
        liste_matchs (list): une liste de matchs

    Returns:
        bool: True si la liste est bien triée et False sinon
    """

    for i in range(1, len(liste_matchs)):
        match = liste_matchs[i]
        match_precedent = liste_matchs[i-1]
        if match[0] + match[1] +  match[2] < match_precedent[0] + match_precedent[1] + match[2]:
            return False

    return True


def fusionner_matchs(liste_matchs1, liste_matchs2):
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
        if liste_matchs1[i][0] + liste_matchs1[i][1] + liste_matchs1[i][2] < liste_matchs2[j][0] + liste_matchs2[j][1] + liste_matchs1[i][2]:
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


def resultats_equipe(liste_matchs, equipe):
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


def plus_gros_scores(liste_matchs, cle=lambda _: True): # Ajout du paramètre cle permettant de filtrer les matchs
    """retourne la liste des matchs pour lesquels l'écart de buts entre le vainqueur et le perdant est le plus grand

    Args:
        liste_matchs (list): une liste de matchs
        cle (function, optional): une fonction qui permet de filtrer les matchs. Par défaut, lambda _: True (tous les matchs)

    Returns:
        list: la liste des matchs avec le plus grand écart entre vainqueur et perdant
    """    

    return max_liste(filter(cle, liste_matchs), cle=lambda match: abs(match[3] - match[4]))

def liste_des_equipes(liste_matchs):
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


def nb_matchs_sans_defaites(liste_matchs, equipe):
    """retourne le plus grand nombre de matchs consécutifs sans défaite pour une equipe donnée.

    Args:
        liste_matchs (list): une liste de matchs
        equipe (str): le nom d'une équipe (pays)

    Returns:
        int: le plus grand nombre de matchs consécutifs sans défaite du pays nom_pays
    """
    # TODO refaire cette fonction
    max_nb_victoires = 0
    nb_victoires = 0
    
    for match in liste_matchs:
        if equipe_gagnante(match) == equipe:
            nb_victoires += 1

        elif equipe == match[1] or equipe == match[2]:
            if nb_victoires > max_nb_victoires:
                max_nb_victoires = nb_victoires
            
            nb_victoires = 0

    if nb_victoires > max_nb_victoires:
        max_nb_victoires = nb_victoires

    return max_nb_victoires

import csv


def charger_matchs(nom_fichier):
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

def sauver_matchs(liste_matchs,nom_fichier):
    """sauvegarde dans un fichier au format CSV une liste de matchs

    Args:
        liste_matchs (list): la liste des matchs à sauvegarder
        nom_fichier (str): nom du fichier CSV

    Returns:
        None: cette fonction ne retourne rien
    """    
    
    with open(nom_fichier, "w", newline="") as fichier_csv:
        writer = csv.writer(fichier_csv)
        writer.writerow(["date", "home_team", "away_team", "home_score", "away_score", "tournament", "city", "country", "neutral"])

        for match in liste_matchs:
            writer.writerow(match)

# Fonctions à implémenter dont il faut également implémenter les tests
def plus_de_victoires_que_defaites(liste_matchs, equipe):
    """vérifie si une équipe donnée a obtenu plus de victoires que de défaites
    
    Args:
        liste_matchs (list): une liste de matchs
        equipe (str): le nom d'une équipe (pays)

    Returns:
        bool: True si l'equipe a obtenu plus de victoires que de défaites
    """
    
    resultats = resultats_equipe(liste_matchs, equipe)
    return resultats[0] > resultats[2]


def matchs_spectaculaires(liste_matchs, cle=lambda _: True): # Ajout du paramètre cle permettant de filtrer les matchs
    """retourne la liste des matchs les plus spectaculaires, c'est à dire les
    matchs dont le nombre total de buts marqués est le plus grand. On peut filtrer les matchs avec la fonction cle.

    Args:
        liste_matchs (list): une liste de matchs
        cle (function, optional): une fonction qui permet de filtrer les matchs. Par défaut, lambda _: True (tous les matchs)

    Returns:
        list: la liste des matchs les plus spectaculaires
    """

    return max_liste(liste_matchs, lambda match: match[3] + match[4] if cle(match) else 0)


def meilleures_equipes(liste_matchs, cle=lambda _: True): # Ajout du paramètre cle permettant de filtrer les matchs
    """retourne la liste des équipes de la liste qui ont le plus petit nombre de defaites.
    On peut filtrer les matchs avec la fonction cle.

    Args:
        liste_matchs (list): une liste de matchs
        cle (function, optional): une fonction qui permet de filtrer les matchs. Par défaut, lambda _: True (toutes les matchs)

    Returns:
        list: la liste des équipes qui ont le plus petit nombre de defaites (l'ordre n'est pas garanti)
    """

    equipes = {} # Invariant de boucle : le dictionnaire des équipes ayant le plus petit nombre de défaites parmi les equipes déjà parcourus.
    minimum = liste_matchs[0][1] # Invairant de boucle : l'equipe avec le moins de défaites parmi les equipes déjà parcourus.

    for match in liste_matchs:
        if not cle(match): # Filtrage des matchs
            continue
        
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

def liste_des_competitions(liste_matchs: list) -> set:
    """Retourne la liste des compétitions présentes dans la liste de matchs.

    Args:
        liste_matchs (list): Une liste de matchs

    Returns:
        set: Un ensemble contenant les noms des compétitions
    """
    
    return set(map(lambda match: match[5], liste_matchs))

def liste_des_villes(liste_matchs: list) -> set:
    """Retourne la liste des villes présentes dans la liste de matchs.

    Args:
        liste_matchs (list): Une liste de matchs

    Returns:
        set: Un ensemble contenant les noms des villes
    """

    return set(map (lambda match: match[6], liste_matchs))


def rechercher_par_date(liste_matchs: list, date: str) -> list:
    """Retourne la liste des matchs s'étant déroulés à la date passée en paramètre.

    Args:
        liste_matchs (list): Une liste de matchs
        date (str): Date au format AAAA-MM-JJ

    Returns:
        list: La liste des matchs s'étant déroulés à la date passée en paramètre
    """

    return list(filter(lambda match: match[0] == date, liste_matchs))


def max_liste(liste, cle=lambda x: x):
    """Retourne une liste d'éléments de la liste d'entrée qui ont la valeur maximale de l'attribut spécifié par la fonction clé.

    Args:
        liste (list): La liste d'entrée.
        cle (function, optional): La fonction utilisée pour extraire la valeur de l'attribut de chaque élément. Par défaut, lambda x: x.

    Returns:
        list: Une liste d'éléments de la liste d'entrée qui ont la valeur maximale de l'attribut spécifié par la fonction clé.
    """

    maximum = float("-inf")
    res = []

    for elem in liste:
        valeur_attribut = cle(elem)
        if valeur_attribut > maximum:
            res = [elem]
            maximum = valeur_attribut

        elif valeur_attribut == maximum:
            res.append(elem)

    return res


def nb_but(liste_matchs: list, cle=lambda _: True) -> int:
    """Retourne le nombre de buts marqués lors de la compétition passée en paramètre.

    Args:
        liste_matchs (list): Une liste de matchs
        cle (function, optional): La fonction utilisée pour filtrer les matchs. Par défaut, lambda _: True.

    Returns:
        int: Le nombre de buts marqués lors de la compétition passée en paramètre.
    """

    nb_buts = 0 # Invariant de boucle : le nombre de buts des matchs déjà parcourus ayant eu lieu lors de la compétition passée en paramètre.
    for match in liste_matchs:
        if cle(match):
            nb_buts += nb_buts_marques(match)

    return nb_buts


def nb_matchs(liste_matchs: list, cle=lambda _: True) -> int:
    """Retourne le nombre de matchs ayant eu lieu lors de la compétition passée en paramètre.

    Args:
        liste_matchs (list): Une liste de matchs
        cle (function, optional): La fonction utilisée pour filtrer les matchs. Par défaut, lambda _: True.

    Returns:
        int: Le nombre de matchs ayant eu lieu lors de la compétition passée en paramètre.
    """

    nb_matchs = 0 # Invariant de boucle : le nombre de matchs déjà parcourus ayant eu lieu lors de la compétition passée en paramètre.
    for match in liste_matchs:
        if cle(match):
            nb_matchs += 1

    return nb_matchs