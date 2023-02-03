import player, heroes, villains

# Character Selection
HoV = input('\nPlease select Heroes or Villains (h/v): ')
if HoV == 'h':
    heroes.printHeroes()
    hSelect = input('Please select from the heroes above')
    if hSelect == 'Luke':
        print("Your adversary is " + villains.randVillainChoice())
        duel = input("Would you like to start the duel? (y or n)")
        if duel == 'y':
            print("You have " + str(player.HEALTH) + " health")
            player.HEALTH -= player.playerDamage()
            print("You now have " + str(player.HEALTH))
            villains.HEALTH -= villains.enemyDamage()
            print("Enemy now has " + str(villains.HEALTH) + " health")
    elif hSelect == 'Leia':
        print("Your adversary is " + villains.randVillainChoice())
        duel = input("Would you like to start the duel? (y or n)")
        if duel == 'y':
            print("You have " + str(player.HEALTH) + " health")
            player.HEALTH -= player.playerDamage()
            print("You now have " + str(player.HEALTH))
            villains.HEALTH -= villains.enemyDamage()
            print("Enemy now has " + str(villains.HEALTH) + " health")
    elif hSelect == 'Obi-Wan':
        print("Your adversary is " + villains.randVillainChoice())
        duel = input("Would you like to start the duel? (y or n)")
        if duel == 'y':
            print("You have " + str(player.HEALTH) + " health")
            player.HEALTH -= player.playerDamage()
            print("You now have " + str(player.HEALTH))
            villains.HEALTH -= villains.enemyDamage()
            print("Enemy now has " + str(villains.HEALTH) + " health")

elif HoV == 'v':
    villains.printVillains()
    vSelect = input('Please select from the heroes above: ')
    if vSelect == 'Darth Vader':
        print("Your adversary is " + heroes.randHeroChoice())
        duel = input("Would you like to start the duel? (y or n)")
        if duel == 'y':
            print("You have " + str(player.HEALTH) + " health")
            player.HEALTH -= player.playerDamage()
            print("You now have " + str(player.HEALTH))
            villains.HEALTH -= villains.enemyDamage()
            print("Enemy now has " + str(villains.HEALTH) + " health")
    elif vSelect == 'Count Dooku':
        print("Your adversary is " + heroes.randHeroChoice())
        duel = input("Would you like to start the duel? (y or n)")
        if duel == 'y':
            print("You have " + str(player.HEALTH) + " health")
            player.HEALTH -= player.playerDamage()
            print("You now have " + str(player.HEALTH))
            villains.HEALTH -= villains.enemyDamage()
            print("Enemy now has " + str(villains.HEALTH) + " health")

else:
    print("Incorrect Input, Please try again!")