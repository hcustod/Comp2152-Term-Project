import random
from character import Character


class Monster(Character):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.survivals = []
        self.evolved = False
        self.combat_strength = random.randint(1, 6)
        self.health_points = random.randint(10, 20)

    def display_info(self):
        print("Monster Stats")
        print(f"Combat Strength: {self.combat_strength}")
        print(f"Health Points: {self.health_points}")
        print("=" * 40)

    def evolve(self):
        print("The Monster evolves stronger!")
        self.level += 1
        self.combat_strength += 2
        self.evolved = True

    def __del__(self):
        super().__del__()
        print("The Monster object is being destroyed by the garbage collector.")