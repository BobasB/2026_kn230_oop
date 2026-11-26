import random

class GameCharacter:
    def __init__(self, name, health: int = 100, attack_power: int = 10):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other_character: 'GameCharacter'):
        if not isinstance(other_character, GameCharacter):
            raise ValueError("other_character має бути класу GameCharacter")
        print(f"{self.name} атакує {other_character.name}!")
        print(f"Атакуємо {self.attack_power} проти {other_character.health} здоров'я.")
        damage = random.randint(self.attack_power - 2, self.attack_power + 2)
        other_character.health -= damage

    def heal(self):
        amount = random.randint(5, 15)
        self.health += amount
        print(f"{self.name} відновлює {amount} здоров'я. Нове здоров'я: {self.health}")

    def ulta(self, other_character: 'GameCharacter'):
        if not isinstance(other_character, GameCharacter):
            raise ValueError("other_character має бути класу GameCharacter")
        print(f"{self.name} використовує ульту проти {other_character.name}!")
        damage = random.randint(self.attack_power * 2, self.attack_power * 3)
        other_character.health -= damage
        print(f"Атакуємо {damage} проти {other_character.health} здоров'я.")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name}: Здоров'я = {self.health}, Атака = {self.attack_power}"