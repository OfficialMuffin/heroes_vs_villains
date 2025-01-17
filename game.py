import random
from heroes import Hero
from villains import Villain


def choose_character(character_list):
    while True:
        try:
            # Display the available characters with their corresponding numbers
            for i, character in enumerate(character_list, start=1):
                print(f"{i}. {character.name} - {character.ability}")

            choice = int(input("Choose a character by number: "))
            if 1 <= choice <= len(character_list):
                return character_list[choice - 1]  # Return the selected character
            else:
                print("Invalid choice. Please pick a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def run():
    # Character Selection
    HoV = input('\nPlease select Heroes or Villains (h/v): ')

    if HoV == 'h':
        heroes = [
            Hero("Luke", "Force Push"),
            Hero("Leia", "Blaster Shot"),
            Hero("Obi-Wan Kenobi", "Force Mind Trick"),
            Hero("Han Solo", "Quick Draw")
        ]
        selected_hero = choose_character(heroes)
        print(f"\nYou are playing as {selected_hero.name}!")
        opponent = random.choice([Villain("Darth Vader", "Force Choke"),
                                  Villain("Count Dooku", "Lightning Strike"),
                                  Villain("Darth Sidious", "Dark Side Blast"),
                                  Villain("Darth Maul", "Double Saber Attack"),
                                  Villain("Jango Fett", "Explosive Rocket")])
        print(f"Your adversary is {opponent.name} from the Villains!")

    elif HoV == 'v':
        villains = [
            Villain("Darth Vader", "Force Choke"),
            Villain("Count Dooku", "Lightning Strike"),
            Villain("Darth Sidious", "Dark Side Blast"),
            Villain("Darth Maul", "Double Saber Attack"),
            Villain("Jango Fett", "Explosive Rocket")
        ]
        selected_villain = choose_character(villains)
        print(f"\nYou are playing as {selected_villain.name}!")
        opponent = random.choice([Hero("Luke", "Force Push"),
                                  Hero("Leia", "Blaster Shot"),
                                  Hero("Obi-Wan Kenobi", "Force Mind Trick"),
                                  Hero("Han Solo", "Quick Draw")])
        print(f"Your adversary is {opponent.name} from the Heroes!")

    else:
        print("Incorrect Input, Please try again!")
        return

    # Battle Start
    print("\nThe duel begins!")
    player_health = 100
    opponent_health = 100

    while selected_hero.is_alive() and opponent.is_alive():
        # Player's Turn
        print(f"\n{selected_hero.name}'s turn!")

        # Show available abilities with their cooldown
        print("Available abilities:")
        available_abilities = []
        for i, ability in enumerate([selected_hero.ability], start=1):
            if selected_hero.cooldown == 0:
                print(f"{i}. {ability}")
                available_abilities.append(ability)
            else:
                print(f"{i}. {ability} (Cooldown: {selected_hero.cooldown} turn(s))")

        # Ability choice by number
        ability_choice = input("Choose an ability by number or type 'attack' for a regular attack: ")

        if ability_choice.isdigit():
            ability_choice = int(ability_choice)
            # Check if the chosen ability is valid and not on cooldown
            if 1 <= ability_choice <= len([selected_hero.ability]) and selected_hero.cooldown == 0:
                chosen_ability = [selected_hero.ability][ability_choice - 1]
                selected_hero.use_ability(opponent)
            elif selected_hero.cooldown > 0:
                print(f"{selected_hero.ability} is on cooldown for {selected_hero.cooldown} more turn(s).")
            else:
                print("Invalid ability number. Please try again.")
        elif ability_choice.lower() == 'attack':
            damage = random.randint(5, 15)  # Regular attack
            print(f"{selected_hero.name} attacked the enemy for {damage} damage!")
            opponent.take_damage(damage)

        # Check if opponent is still alive
        if not opponent.is_alive():
            print(f"{opponent.name} has been defeated! {selected_hero.name} wins!")
            break

        # Opponent's Turn
        print(f"\n{opponent.name}'s turn!")
        damage = random.randint(5, 15)  # Regular attack
        print(f"{opponent.name} attacked for {damage} damage!")
        selected_hero.take_damage(damage)

        if not selected_hero.is_alive():
            print(f"{selected_hero.name} has been defeated! {opponent.name} wins!")
            break

        # Update cooldowns
        selected_hero.update_cooldown()
        opponent.update_cooldown()

    print("Game over!")
