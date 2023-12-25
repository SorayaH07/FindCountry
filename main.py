# -----------------------------------
#          → Find Capital
# -----------------------------------
#   Last update : 17/12/23
#   By : HAJJAR Soraya & SAGE Laurine
#

import random
from colorama import Fore, Back, Style


def game_loop(capitals_list, country_list, score, used_nb):
    nb = random.randint(0, len(capitals_list) - 1)
    while nb in used_nb:
        nb = random.randint(0, len(capitals_list) - 1)
    used_nb.append(nb)
    print(Fore.MAGENTA + f"Le premier charactère doit être en majuscule" + Style.RESET_ALL)
    print("---------------------------------")
    entry = input(f"Quelle est la capitale de/du {country_list[nb]}? → ")
    if capitals_list[nb] == entry:
        print(f"---------------------------------")
        print(Fore.GREEN + f"Bien joué ! +1 point → Ton score actuel est de {score + 1}")
        print(Style.RESET_ALL)
        return 1
    else:
        print(f"---------------------------------")
        print(Fore.RED + f"Dommage ce n'est pas la bonne réponse → -1 point → Ton score actuel est de {score - 1}")
        print(Style.RESET_ALL)
        return -1


def game_start(capitals_list, country_list):
    used_nb = []
    round_count = 0
    score = 0
    while round_count < 10:
        score += game_loop(capitals_list, country_list, score, used_nb)
        round_count += 1
    if score < 0:
        print("\n---------------------------------\nTon score est négatif, mais on va te sauver")
        score = 0
    print(f"GAME OVER\nVoilà ton score {score}\n----------------------------------")
    entry = input("\nSouhaitez-vous recommencer ? (O/N) → ")
    if entry == 'O':
        print("Rebienvenue !")
        game_start(capitals_list, country_list)
    else:
        print("Merci d'avoir joué à bientôt !")
        return


capitals = []
country = []
i = 0
# -----------CAPTIALS------------
file = open("captials.txt", "r")
for line in file.readlines():
    capitals.append(line.strip())
    i += 1
file.close()
# -----------COUNTRY-------------
file = open("country.txt", "r")
for line in file.readlines():
    country.append(line.strip())
    i += 1
file.close()

if len(capitals) != len(country):
    print("ERROR → Il n'y a pas le même nombre de pays et de capitales dans les fichiers [country.txt & capitals.txt]")
    exit(1)


game_start(capitals, country)
