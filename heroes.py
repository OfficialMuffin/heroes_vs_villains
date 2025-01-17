from random import choice

# List Heroes
heroes = ["Luke", "Leia", "Obi-Wan Kenobi", "Han Solo"]

def printHeroes():
    for i, hero in enumerate(heroes, start=1):
        print(f"{i}. {hero}")
        
def randHeroChoice():
    randHero = choice(heroes)
    return randHero