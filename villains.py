from random import choice, randint

villains = ["Darth Vader", "Count Dooku", "Darth Sidious", "Darth Maul", "Jango Fett"]
HEALTH = 100

def printVillains():
    for i in range(0, len(villains)):
        print(f"{i + 1}. {villains[i]}")
        
def randVillainChoice():
    randVillain = choice(villains)
    return randVillain

def enemyDamage():
    damage = randint(0, 10)
    return damage