from character import Character
import random

class Hero(Character):
    def __init__(self):
        super().__init__()
        self.wins = []
        self.special_ability = False
        self.level = 1

    def hero_attacks(self, monster):
        if self.special_ability:
            damage = self.combat_strength + 3 if random.random() < 0.7 else 0
            print("Hero uses special ability!" if damage > 0 else "Hero's special attack missed!")
        else:
            damage = self.combat_strength

        monster.health_points -= damage
        print(f"The Hero attacks! The Monster takes {damage} damage.")

    def evolve(self):
        print("Hero is evolving!")
        self.special_ability = True
        self.level += 1

    def __del__(self):
        print("The Hero object is being destroyed by the garbage collector.")
        super().__del__()
