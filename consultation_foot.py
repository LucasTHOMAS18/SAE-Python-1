import os
import sys

import histoire2foot


# Ici vos fonctions dédiées aux interactions
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def recup_fichiers():
    liste_fichiers = []

    for fichier in os.listdir():
        if fichier.endswith(".csv"):
            liste_fichiers.append(fichier)

    return liste_fichiers

def demander_nombre(texte, debut, fin):
    reponse = input(texte)

    while not reponse.isnumeric() or debut > int(reponse) or int(reponse) > fin:
        print("Choix invalide.")
        reponse = input(texte)
    return reponse

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

    print("Voici la liste des fichiers .csv disponibles: ")
    for i, fichier in enumerate(recup_fichiers()):
        print(f" {i + 1}. {fichier}")
    
    # Demande à l'utilisateur quel fichier choisir
    numero_fichier = int(demander_nombre("\nQuel fichier .csv souhaitez-vous consulter ? ", 1, i+1))

    # Charge le fichier
    fichier = histoire2foot.charger_matchs(liste_fichiers[numero_fichier])
    
if __name__ == "__main__":
    programme_principal()
    