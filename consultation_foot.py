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

# ici votre programme principal
def programme_principal():
    clear()
    print("""\033[0;34m
    __  ___      __        _          ___   ______            __ 
   / / / (_)____/ /_____  (_)_______ |__ \ / ____/___  ____  / /_
  / /_/ / / ___/ __/ __ \/ / ___/ _ \__/ // /_  / __ \/ __ \/ __/
 / __  / (__  ) /_/ /_/ / / /  /  __/ __// __/ / /_/ / /_/ / /_  
/_/ /_/_/____/\__/\____/_/_/   \___/____/_/    \____/\____/\__/                                                         
\033[0m""")
    
    liste_fichiers = recup_fichiers()
    
    if len(liste_fichiers) == 0:
        print("\033[91mAucun fichier .csv trouvé. \033[0m")
        sys.exit()

    print("Voici la liste des fichiers .csv disponibles: ")
    for i, fichier in enumerate(recup_fichiers()):
        print(f" {i + 1}. {fichier}")

    input("\nQuel fichier .csv souhaitez-vous consulter ? ")

if __name__ == "__main__":
    programme_principal()
    