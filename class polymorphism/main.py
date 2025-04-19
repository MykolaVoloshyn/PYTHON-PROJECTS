class GameCharacter:
    def __init__(self, name, sex, health):
        self.name = name
        self.sex = sex
        self.health = health

    def attack(self):
        return f"{self.name} attacks!"


class Warrior(GameCharacter):
    def __init__(self, name, sex, health, weapon, strength):
        super().__init__(name, sex, health)
        self.weapon = weapon
        self.strength = strength

    def attack(self):
        return f"{self.name} swings their {self.weapon} with strength {self.strength}!"


class Archer(GameCharacter):
    def __init__(self, name, sex, health, bow_type, arrows_left):
        super().__init__(name, sex, health)
        self.bow_type = bow_type
        self.arrows_left = arrows_left

    def attack(self):
        return f"{self.name} fires an arrow from their {self.bow_type}. {self.arrows_left} arrows left!"
