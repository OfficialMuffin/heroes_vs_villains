import player
from heroes import heroes, printHeroes
from villains import villains, printVillains, enemyDamage
from random import choice

def chooseCharacter(character_list):
    while True:
        try:
            choice = int(input("Choose a character by number: "))
            if 1 <= choice <= len(character_list):
                return character_list[choice - 1]
            else:
                print("Invalid Choice. Please pick a valid number.")
        except ValueError:
            print("Invalid Input. Please enter a number.")


def run():
    # Character Selection
    HoV = input('\nPlease select Heroes or Villains (h/v): ')
    if HoV == 'h':
        printHeroes()
        selected_hero = chooseCharacter(heroes)
        print(f"\nYou are playing as {selected_hero}!")
        opponent = choice(villains)
        print(f"Your adversary is {opponent} from the Villains!")

    elif HoV == 'v':
        printVillains()
        selected_villain = chooseCharacter(villains)
        print(f"\nYou are playing as {selected_villain}!")
        opponent = choice(heroes)
        print(f"Your adversary is {opponent} from the Heroes!")

    else:
        print("Incorrect Input, Please try again!")
        return

    # Battle Start
    print("\nThe duel begins!")
    player_health = player.HEALTH
    opponent_health = player.HEALTH

    while player_health > 0 and opponent_health > 0:
        # Player's Turn
        print(f"\n{selected_hero if HoV == 'h' else selected_villain}'s turn!")
        damage = player.playerDamage()
        print(f"You dealt {damage} damage!")
        opponent_health -= damage
        print(f"{opponent} now has {max(opponent_health, 0)} health remaining.")

        if opponent_health <= 0:
            print(f"\n{opponent} has been defeated! You win!")
            break

        # Opponent's Turn
        print(f"\n{opponent}'s turn!")
        damage = player.playerDamage()
        print(f"They dealt {damage} damage!")
        player_health -= damage
        print(f"{selected_hero if HoV == 'h' else selected_villain} now has {max(player_health, 0)} health remaining.")

        if player_health <= 0:
            print(f"\n{selected_hero if HoV == 'h' else selected_villain} has been defeated! You lose!")
            break

    print("Game over!")