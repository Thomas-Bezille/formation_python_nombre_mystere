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