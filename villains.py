from random import choice, randint
from config import DEFAULT_HEALTH, DAMAGE_RANGE

villains = ["Darth Vader", "Count Dooku", "Darth Sidious", "Darth Maul", "Jango Fett"]

HEALTH = DEFAULT_HEALTH

def printVillains():
    for i, villain in enumerate(villains, start=1):
        print(f"{i}. {villain}")
        
def randVillainChoice():
    randVillain = choice(villains)
    return randVillain

def enemyDamage():
    damage = randint(*DAMAGE_RANGE)
    return damage