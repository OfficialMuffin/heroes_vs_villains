from random import choice

# List Heroes
heroes = ["Luke", "Leia", "Obi-Wan Kenobi", "Han Solo"]

def printHeroes():
    for i in range(0, len(heroes)):
        print(f"{i + 1}. {heroes[i]}")
        
def randHeroChoice():
    randHero = choice(heroes)
    return randHero