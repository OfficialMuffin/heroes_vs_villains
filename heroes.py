import random
from character import Character

# List Heroes
heroes = ["Luke", "Leia", "Obi-Wan Kenobi", "Han Solo"]

class Hero(Character):
    def __init__(self, name, ability):
        super().__init__(name, ability)

    def _ability_damage(self):
        """Return damage based on the hero's ability."""
        if self.ability == "Force Push":
            return random.randint(10, 20)
        elif self.ability == "Lightsaber Strike":
            return random.randint(15, 25)
        elif self.ability == "Blaster Shot":
            return random.randint(5, 15)
        elif self.ability == "Grenade Toss":
            return random.randint(20, 30)
        elif self.ability == "Force Mind Trick":
            return random.randint(10, 20)
        elif self.ability == "Lightsaber Defense":
            return random.randint(7, 14)  # Lower damage but provides defensive boost
        elif self.ability == "Quick Draw":
            return random.randint(7, 17)
        elif self.ability == "Blaster Barrage":
            return random.randint(18, 25)
        else:
            return 0  # Default case if ability isn't recognized


def printHeroes():
    for i, hero in enumerate(heroes, start=1):
        print(f"{i}. {hero}")

def randHeroChoice():
    randHero = random.choice(heroes)
    return randHero