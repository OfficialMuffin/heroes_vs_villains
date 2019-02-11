import random

def randHeroChoice():
    randHero = random.choice(heroChar)
    return randHero

def randVillainChoice():
    randVillain = random.choice(villChar)
    return randVillain

def printHeroes():
    for i in heroChar:
        print(i)

def printVillains():
    for i in villChar:
        print(i)

def playerDamage():
    rand = random.randint(0, 10)
    return rand

def enemyDamage():
    randE = random.randint(0, 10)
    return randE

# Initialise Health Variables
playerHealth = 100
enemyHealth = 100

# List Heroes and Villains
heroChar = ["Luke", "Leia", "Obi-Wan"]
villChar = ["Darth Vader", "Count Dooku"]


# Character Selection
HoV = input('Please select Heroes or Villains(h OR v)')
if HoV == 'h':
    printHeroes()
    hSelect = input('Please select from the heroes above')
    if hSelect == 'Luke':
        print("Your adversary is " + randVillainChoice())
        duel = input("Would you like to start the duel? (y or n)")
        if duel == 'y':
            print("You have " + str(playerHealth) + " health")
            playerHealth -= playerDamage()
            print("You now have " + str(playerHealth))
            enemyHealth -= enemyDamage()
            print("Enemy now has " + str(enemyHealth) + " health")
    elif hSelect == 'Leia':
        print("Your adversary is " + randVillainChoice())
        duel = input("Would you like to start the duel? (y or n)")
        if duel == 'y':
            print("You have " + str(playerHealth) + " health")
            playerHealth -= playerDamage()
            print("You now have " + str(playerHealth))
            enemyHealth -= enemyDamage()
            print("Enemy now has " + str(enemyHealth) + " health")
    elif hSelect == 'Obi-Wan':
        print("Your adversary is " + randVillainChoice())
        duel = input("Would you like to start the duel? (y or n)")
        if duel == 'y':
            print("You have " + str(playerHealth) + " health")
            playerHealth -= playerDamage()
            print("You now have " + str(playerHealth))
            enemyHealth -= enemyDamage()
            print("Enemy now has " + str(enemyHealth) + " health")

elif HoV == 'v':
    printVillains()
    vSelect = input('Please select from the heroes above')
    if vSelect == 'Darth Vader':
        print("Your adversary is " + randHeroChoice())
        duel = input("Would you like to start the duel? (y or n)")
        if duel == 'y':
            print("You have " + str(playerHealth) + " health")
            playerHealth -= playerDamage()
            print("You now have " + str(playerHealth))
            enemyHealth -= enemyDamage()
            print("Enemy now has " + str(enemyHealth) + " health")
    elif vSelect == 'Count Dooku':
        print("Your adversary is " + randHeroChoice())
        duel = input("Would you like to start the duel? (y or n)")
        if duel == 'y':
            print("You have " + str(playerHealth) + " health")
            playerHealth -= playerDamage()
            print("You now have " + str(playerHealth))
            enemyHealth -= enemyDamage()
            print("Enemy now has " + str(enemyHealth) + " health")

else:
    print("Incorrect Input, Please try again!")


