class Character:
    def __init__(self, name, ability, health=100):
        self.name = name
        self.ability = ability
        self.health = health
        self.cooldown = 0  # Cooldown for ability

    def use_ability(self, target):
        """Use the character's unique ability on the target."""
        if self.cooldown == 0:
            damage = self._ability_damage()
            print(f"{self.name} used {self.ability}! It dealt {damage} damage!")
            target.take_damage(damage)
            self.cooldown = 3  # Set cooldown (e.g., 3 turns)
        else:
            print(f"{self.ability} is on cooldown for {self.cooldown} more turn(s).")

    def _ability_damage(self):
        """This method will be overridden by subclasses."""
        raise NotImplementedError("Subclasses should implement this method.")

    def take_damage(self, damage):
        """Decrease health by damage."""
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} now has {self.health} health.")

    def update_cooldown(self):
        """Update the cooldown on each turn."""
        if self.cooldown > 0:
            self.cooldown -= 1

    def is_alive(self):
        """Check if the character is still alive."""
        return self.health > 0
