from pathlib import Path

import histoire2foot

# ---------------------------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------------------------
CHEMIN_CSV = Path(__file__).parent / "csv"

# ---------------------------------------------------------------------------------------------
# Exemples de données pour vous aidez à faire des tests
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

def test_equipe_gagnante():
    assert histoire2foot.equipe_gagnante(match1) is None
    assert histoire2foot.equipe_gagnante(match2) == 'France'
    assert histoire2foot.equipe_gagnante(match3) == 'Brazil'

def test_victoire_a_domicile():
    assert not histoire2foot.victoire_a_domicile(match1)
    assert histoire2foot.victoire_a_domicile(match2)
    assert not histoire2foot.victoire_a_domicile(match3)

def test_nb_buts_marques():
    assert histoire2foot.nb_buts_marques(liste1[0]) == 2
    assert histoire2foot.nb_buts_marques(liste1[1]) == 2
    assert histoire2foot.nb_buts_marques(liste1[2]) == 3
    assert histoire2foot.nb_buts_marques(liste1[3]) == 4

def test_matchs_ville():
    assert histoire2foot.matchs_ville(liste1,'Reims') == [('1970-04-28', 'France', 'Romania', 2, 0, 'Friendly', 'Reims', 'France', False)]
    assert histoire2foot.matchs_ville(liste2,'Reims') == []
    assert histoire2foot.matchs_ville(liste2,'Liverpool') == [
        ('1905-03-27', 'England', 'Wales', 3, 1, 'British Championship', 'Liverpool', 'England', False), 
        ('1907-02-16', 'England', 'Northern Ireland', 1, 0, 'British Championship', 'Liverpool', 'England', False)]

def test_nombre_moyen_buts():
    assert histoire2foot.nombre_moyen_buts(liste1, 'Friendly') == 7/3
    assert histoire2foot.nombre_moyen_buts(liste2) == 47/16
    assert histoire2foot.nombre_moyen_buts(liste4, 'FIFA World Cup') == 102/37
    assert histoire2foot.nombre_moyen_buts(liste3, 'Friendly') == 3.0
    assert histoire2foot.nombre_moyen_buts([]) == 0.0
    assert histoire2foot.nombre_moyen_buts([], "Albert") == 0.0

def test_resultats_equipe():
    assert histoire2foot.resultats_equipe(liste1, "France") == (3, 1, 0)
    assert histoire2foot.resultats_equipe(liste1, "Norway") == (0, 0, 1)
    assert histoire2foot.resultats_equipe(liste1, "Bulgaria") == (0, 1, 0)
    assert histoire2foot.resultats_equipe(liste4, "France") == (1, 0, 2)
    assert histoire2foot.resultats_equipe(liste4, "Argentina") == (9, 1, 1)

def test_plus_gros_scores():
    assert histoire2foot.plus_gros_scores(liste1) == [('1970-09-05', 'France', 'Czechoslovakia', 3, 0, 'Friendly', 'Nice', 'France', False)]
    assert histoire2foot.plus_gros_scores(liste2) == [('1901-03-18', 'England', 'Wales', 6, 0, 'British Championship', 'Newcastle', 'England', False)]
    assert histoire2foot.plus_gros_scores(liste3) == [('1903-04-04', 'Brazil', 'Argentina', 3, 0, 'Friendly', 'Sao Paulo', 'Brazil', False), ('1970-09-05', 'France', 'Czechoslovakia', 3, 0, 'Friendly', 'Nice', 'France', False)]
    assert histoire2foot.plus_gros_scores([]) == []

def test_liste_des_equipes():
    res=histoire2foot.liste_des_equipes(liste1)
    res.sort()
    assert res == ['Bulgaria','Czechoslovakia','France', 'Norway','Romania']
    res=histoire2foot.liste_des_equipes(liste2)
    res.sort()
    assert res == ['England', 'Northern Ireland','Scotland', 'Wales']

def test_premiere_victoire():
    assert histoire2foot.premiere_victoire(liste1, "France") == "1970-04-28"
    assert histoire2foot.premiere_victoire(liste1, "England") == None
    assert histoire2foot.premiere_victoire(liste1, "Iran") == None
    assert histoire2foot.premiere_victoire(liste2, "England") == "1901-03-09"
    
def test_nb_matchs_sans_defaites():
    assert histoire2foot.nb_matchs_sans_defaites(liste1, "France") == 3
    assert histoire2foot.nb_matchs_sans_defaites(liste2, "England") == 3
    assert histoire2foot.nb_matchs_sans_defaites(liste3, "Brazil") == 1
    assert histoire2foot.nb_matchs_sans_defaites(liste3, "Belgium") == 0

def test_est_bien_trie():
    assert histoire2foot.est_bien_trie(liste1)
    assert histoire2foot.est_bien_trie(liste2)
    assert histoire2foot.est_bien_trie(liste3)
    assert histoire2foot.est_bien_trie(liste4)
    assert not histoire2foot.est_bien_trie(liste1 + liste2)
    assert histoire2foot.est_bien_trie([])

def test_fusionner_matchs():
    liste_fus = [('1901-03-09', 'England', 'Northern Ireland', 3, 0, 'British Championship', 'Southampton', 'England', False), 
        ('1901-03-18', 'England', 'Wales', 6, 0, 'British Championship', 'Newcastle', 'England', False), 
        ('1901-03-30', 'Belgium', 'France', 1, 2, 'Friendly', 'Bruxelles', 'Belgium', False),
        ('1901-03-30', 'England', 'Scotland', 2, 2, 'British Championship', 'London', 'England', False), 
        ('1902-05-03', 'England', 'Scotland', 2, 2, 'British Championship', 'Birmingham', 'England', False), 
        ('1903-02-14', 'England', 'Northern Ireland', 4, 0, 'British Championship', 'Wolverhampton', 'England', False), 
        ('1903-03-02', 'England', 'Wales', 2, 1, 'British Championship', 'Portsmouth', 'England', False), 
        ('1903-04-04', 'Brazil', 'Argentina', 3, 0, 'Friendly', 'Sao Paulo', 'Brazil', False),
        ('1903-04-04', 'England', 'Scotland', 1, 2, 'British Championship', 'Sheffield', 'England', False), 
        ('1905-02-25', 'England', 'Northern Ireland', 1, 1, 'British Championship', 'Middlesbrough', 'England', False), 
        ('1905-03-27', 'England', 'Wales', 3, 1, 'British Championship', 'Liverpool', 'England', False), 
        ('1905-04-01', 'England', 'Scotland', 1, 0, 'British Championship', 'London', 'England', False), 
        ('1907-02-16', 'England', 'Northern Ireland', 1, 0, 'British Championship', 'Liverpool', 'England', False), 
        ('1907-03-18', 'England', 'Wales', 1, 1, 'British Championship', 'London', 'England', False), 
        ('1907-04-06', 'England', 'Scotland', 1, 1, 'British Championship', 'Newcastle', 'England', False), 
        ('1909-02-13', 'England', 'Northern Ireland', 4, 0, 'British Championship', 'Bradford', 'England', False), 
        ('1909-03-15', 'England', 'Wales', 2, 0, 'British Championship', 'Nottingham', 'England', False), 
        ('1909-04-03', 'England', 'Scotland', 2, 0, 'British Championship', 'London', 'England', False),
        ('1970-09-05', 'France', 'Czechoslovakia', 3, 0, 'Friendly', 'Nice', 'France', False), 
        ('1970-11-11', 'France', 'Norway', 3, 1, 'UEFA Euro qualification', 'Lyon', 'France', False)
        ]
    assert histoire2foot.fusionner_matchs(liste1,liste2) == liste2 + liste1
    assert histoire2foot.fusionner_matchs([],liste3) == liste3
    assert histoire2foot.fusionner_matchs(liste2,liste3) == liste_fus

def test_sauver_charger_matchs():
    histoire2foot.sauver_matchs(liste1, CHEMIN_CSV / "histoire_test.csv")
    assert histoire2foot.charger_matchs(CHEMIN_CSV / "histoire_test.csv") == liste1
    assert histoire2foot.charger_matchs(CHEMIN_CSV / "patrick.owo") == []

# ajouter les tests manquants
def test_plus_de_victoires_que_defaites():
    assert histoire2foot.plus_de_victoires_que_defaites(liste1, "France") == True
    assert histoire2foot.plus_de_victoires_que_defaites(liste2, "Romania") == False
    assert histoire2foot.plus_de_victoires_que_defaites(liste3, "Belgium") == False
    assert histoire2foot.plus_de_victoires_que_defaites(liste4, "Argentina") == True

def test_matchs_spectaculaires():
    assert histoire2foot.matchs_spectaculaires(liste1) == [('1970-11-11', 'France', 'Norway', 3, 1, 'UEFA Euro qualification', 'Lyon', 'France', False)]
    assert histoire2foot.matchs_spectaculaires(liste2) == [('1901-03-18', 'England', 'Wales', 6, 0, 'British Championship', 'Newcastle', 'England', False)]
    assert histoire2foot.matchs_spectaculaires(liste3) == [('1901-03-30', 'England', 'Scotland', 2, 2, 'British Championship', 'London', 'England', False), ('1970-11-11', 'France', 'Norway', 3, 1, 'UEFA Euro qualification', 'Lyon', 'France', False)]
    assert histoire2foot.matchs_spectaculaires(liste4) == [('1978-06-06', 'Germany', 'Mexico', 6, 0, 'FIFA World Cup', 'Córdoba', 'Argentina', True), ('1978-06-14', 'Austria', 'Netherlands', 1, 5, 'FIFA World Cup', 'Córdoba', 'Argentina', True), ('1978-06-21', 'Argentina', 'Peru', 6, 0, 'FIFA World Cup', 'Rosario', 'Argentina', False)]

def test_meilleures_equipes():
    # Conversion en set pour ignorer l'ordre qui n'est pas garanti
    assert set(histoire2foot.meilleures_equipes(liste1)) == {"France", "Bulgaria"}
    assert set(histoire2foot.meilleures_equipes(liste2)) == {"England"}
    assert set(histoire2foot.meilleures_equipes(liste3)) == {"Brazil", "Scotland", "France"}
    assert set(histoire2foot.meilleures_equipes(liste4)) == {"Brazil"}

# test fonction perso
def test_max_liste():
    assert histoire2foot.max_liste([1, 2, 3, 4, 5]) == [5]
    assert histoire2foot.max_liste([1, 2, 3, 5, 5]) == [5, 5]
    assert histoire2foot.max_liste([1, 2, 3, 4, 5], cle=lambda x: -x) == [1]
    assert histoire2foot.max_liste([{'a': 1, 'b': 2}, {'a': 2, 'b': 1}, {'a': 1, 'b': 3}], cle=lambda x: x['a']) == [{'a': 2, 'b': 1}]
    assert histoire2foot.max_liste([{'a': 1, 'b': 2}, {'a': 2, 'b': 1}, {'a': 1, 'b': 3}], cle=lambda x: x['b']) == [{'a': 1, 'b': 3}]
    assert histoire2foot.max_liste([{'a': 1, 'b': 2}, {'a': 2, 'b': 1}, {'a': 1, 'b': 3}], cle=lambda x: x['a'] + x['b']) == [{'a': 1, 'b': 3}]

def test_liste_des_competitions():
    assert histoire2foot.ensemble_des_competitions([]) == set()
    assert histoire2foot.ensemble_des_competitions([match1]) == {'UEFA Euro'}
    assert histoire2foot.ensemble_des_competitions(liste1) == {'Friendly', 'UEFA Euro qualification'}
    assert histoire2foot.ensemble_des_competitions(liste2) == {'British Championship'}
    assert histoire2foot.ensemble_des_competitions(liste3) == {'Friendly', 'British Championship', 'UEFA Euro qualification'}
    assert histoire2foot.ensemble_des_competitions(liste4) == {'FIFA World Cup', 'Copa Ramón Castilla', 'Friendly'}

def test_nb_but():
    assert histoire2foot.nb_but(liste1) == 11
    assert histoire2foot.nb_but(liste2) == 47
    assert histoire2foot.nb_but(liste3) == 20
    assert histoire2foot.nb_but(liste4) == 114

def test_liste_des_villes():
    assert histoire2foot.ensemble_des_villes(liste1) == {'Rouen', 'Reims', 'Nice', 'Lyon'}
    assert histoire2foot.ensemble_des_villes(liste2) == {'Southampton', 'Newcastle', 'London', 'Birmingham', 'Wolverhampton', 'Portsmouth', 'Liverpool', 'Bradford', 'Nottingham', 'Middlesbrough', 'Sheffield', 'Newcastle'}
    assert histoire2foot.ensemble_des_villes(liste3) == {'Bruxelles', 'London', 'Sao Paulo', 'Nice', "Lyon", 'Sheffield'}

def test_rechercher_par_date():
    assert histoire2foot.rechercher_par_date(liste1, '1970-04-28') == [('1970-04-28', 'France', 'Romania', 2, 0, 'Friendly', 'Reims', 'France', False)]
    assert histoire2foot.rechercher_par_date(liste1, '1970-04-29') == []
    assert histoire2foot.rechercher_par_date(liste2, '1901-03-09') == [('1901-03-09', 'England', 'Northern Ireland', 3, 0, 'British Championship', 'Southampton', 'England', False)]
    assert histoire2foot.rechercher_par_date([], '1901-03-10') == []
    assert histoire2foot.rechercher_par_date(liste4, '1978-06-11') == [('1978-06-11', 'Austria', 'Brazil', 0, 1, 'FIFA World Cup', 'Mar del Plata', 'Argentina', True), ('1978-06-11', 'Iran', 'Peru', 1, 4, 'FIFA World Cup', 'Córdoba', 'Argentina', True), ('1978-06-11', 'Netherlands', 'Scotland', 2, 3, 'FIFA World Cup', 'Mendoza', 'Argentina', True),  ('1978-06-11', 'Spain', 'Sweden', 1, 0, 'FIFA World Cup', 'Buenos Aires', 'Argentina', True)]

def test_est_un_entier():
    assert histoire2foot.est_un_entier("621")
    assert not histoire2foot.est_un_entier("3.621")
    assert not histoire2foot.est_un_entier("-1", 0, 1)
    assert not histoire2foot.est_un_entier("2", 0, 1)
    assert histoire2foot.est_un_entier("0", 0, 1)
    assert histoire2foot.est_un_entier("1", 0, 1)
    assert not histoire2foot.est_un_entier("1", 2, 3)
    assert not histoire2foot.est_un_entier("OwO")
    assert not histoire2foot.est_un_entier("Shrek 2", 0, 1)
    assert not histoire2foot.est_un_entier("1970-04-28")
