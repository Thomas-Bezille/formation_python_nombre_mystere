import random
import sys

MIN = 0
MAX = 100
NBR_MYSTERY = random.randint(MIN, MAX)
life = 5

print(f"*** Devinez le nombre mystère entre {MIN} et {MAX} ***")
while True:
    try_nbr = input("Devine le nombre: ")
    
    if not try_nbr.isdigit():
        print("Veuillez entrer un nombre valide.")
        continue
    elif int(try_nbr) < MIN or int(try_nbr) > MAX:
        print(f"Le nombre doit être entre {MIN} et {MAX}.")
        continue
    elif int(try_nbr) < NBR_MYSTERY:
        print(f"Le nombre mystère est plus grand que {try_nbr}.")
        life -= 1
        print(f"Il vous reste {life} essais.")
    elif int(try_nbr) > NBR_MYSTERY:
        print(f"Le nombre mystère est plus petit que {try_nbr}.")
        life -= 1
        print(f"Il vous reste {life} essais.")
    elif int(try_nbr) == NBR_MYSTERY:
        print(f"Bravo! Le nombre mystère est bien {NBR_MYSTERY}.")
        sys.exit("Fin du jeu.")