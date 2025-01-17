import random
from config import DEFAULT_HEALTH, DAMAGE_RANGE
from character import Character

villains = ["Darth Vader", "Count Dooku", "Darth Sidious", "Darth Maul", "Jango Fett"]

HEALTH = DEFAULT_HEALTH



class Villain(Character):
    def __init__(self, name, ability):
        super().__init__(name, ability)

    def _ability_damage(self):
        """Return damage based on the villain's ability."""
        if self.ability == "Force Choke":
            return random.randint(10, 20)
        elif self.ability == "Lightning Strike":
            return random.randint(12, 18)
        elif self.ability == "Dark Side Blast":
            return random.randint(15, 25)
        elif self.ability == "Double Saber Attack":
            return random.randint(10, 20)
        elif self.ability == "Explosive Rocket":
            return random.randint(20, 30)
        else:
            return 0  # Default case if ability isn't recognized


def printVillains():
    for i, villain in enumerate(villains, start=1):
        print(f"{i}. {villain}")
        
def randVillainChoice():
    randVillain = random.choice(villains)
    return randVillain

def enemyDamage():
    damage = random.randint(*DAMAGE_RANGE)
    return damage