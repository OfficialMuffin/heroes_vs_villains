# Heroes_vs_Villains

DISCLAIMER: This program has no affiliation with Star Wars. it is purely a fan made project

Welcome to Heroes vs. Villains! This Python-based game lets you choose your favorite hero or villain from the Star Wars universe and engage in epic battles. Each character comes with a set of unique abilities, and you must carefully manage your cooldowns, health, and tactics to outsmart your opponent.

## Features

- **Character Selection:** Choose between heroes and villains from the Star Wars universe.
- **Unique Abilities:** Each character has multiple unique abilities, each with its own damage output and cooldown period.
- **Turn-Based Combat:** The battle is turn-based, with each character attacking or using abilities on their turn.
- **Cooldown Management:** Abilities have cooldowns, so plan your actions wisely!
- **Random Opponents:** Face off against randomly selected enemies to keep each battle exciting and unpredictable.

## Installation

### Prerequisites

To run the project, you'll need to have Python 3.x installed. You can download Python from the official website: https://www.python.org/downloads/

### Clone the Repository

To clone this repository to your local machine, use the following command:

```bash
git clone https://github.com/OfficialMuffin/heroes_vs_villains.git
cd heroes_vs_villains
```

### Running the Game

Once you have the project on your local machine, navigate to the project directory and run the game using Python:

```bash
python game.py
```

Follow the on-screen prompts to select your character and begin the battle!

## How to Play

1. **Select Heroes or Villains:** At the start of the game, you will be prompted to choose whether you want to play as a hero or a villain.
2. **Choose Your Character:** Once you select your faction (Heroes or Villains), you'll choose your character from a list.
3. **Battle Mechanics:**
    - On your turn, you can either select an ability or make a regular attack.
    - Each ability has a cooldown, so choose carefully.
    - The goal is to defeat your opponent before they defeat you.
4. **Cooldowns:** After using an ability, it will go on cooldown, and you’ll need to wait before you can use it again.

## Characters & Abilities

### Heroes

1. **Luke Skywalker**
   - Force Push: Deals 10-20 damage.
   - Lightsaber Strike: Deals 15-25 damage.
   
2. **Leia Organa**
   - Blaster Shot: Deals 5-15 damage.
   - Grenade Toss: Deals 20-30 damage.

3. **Obi-Wan Kenobi**
   - Force Mind Trick: Deals 10-20 damage.
   - Lightsaber Defense: Deals 7-14 damage.

4. **Han Solo**
   - Quick Draw: Deals 7-17 damage.
   - Blaster Barrage: Deals 18-25 damage.

### Villains

1. **Darth Vader**
   - Force Choke: Deals 12-22 damage.
   - Lightsaber Slash: Deals 15-25 damage.
   
2. **Count Dooku**
   - Lightning Strike: Deals 12-18 damage.
   - Force Lightning: Deals 18-30 damage.
   
3. **Darth Sidious**
   - Dark Side Blast: Deals 20-35 damage.
   - Sith Fury: Deals 15-30 damage.
   
4. **Darth Maul**
   - Double Saber Attack: Deals 10-20 damage.
   - Sith Rage: Deals 25-40 damage.

5. **Jango Fett**
   - Explosive Rocket: Deals 20-30 damage.
   - Jetpack Dive: Deals 18-28 damage.

## Project Structure

```
heroes_vs_villains
│
├── game.py          # Main game logic
├── heroes.py        # Hero characters and abilities
├── villains.py      # Villain characters and abilities
├── character.py     # Base class for characters
└── README.md        # Project documentation
```

## Contributing

We welcome contributions to improve the game! If you have any suggestions, improvements, or bug fixes, feel free to create an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to your branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
