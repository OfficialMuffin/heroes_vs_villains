from random import random

# List Heroes
heroes = ["Luke", "Leia", "Obi-Wan Kenobi", "Han Solo"]

def printHeroes():
    for i in range(0, len(heroes)):
        print(f"{i + 1}. {heroes[i]}")
        
def randHeroChoice():
    randHero = random.choice(heroes)
    return randHero