from random import randint
from config import DEFAULT_HEALTH, DAMAGE_RANGE

HEALTH = DEFAULT_HEALTH

def playerDamage():
    damage = randint(*DAMAGE_RANGE)
    return damage