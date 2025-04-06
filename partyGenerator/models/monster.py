import random

class Monster:
    def __init__(self):
        self.combat_strength = random.randint(1, 6)
        self.health_points = random.randint(10, 20)

    def display_info(self):
        print("Monster Stats")
        print(f"Combat Strength: {self.combat_strength}")
        print(f"Health Points: {self.health_points}")
        print("=" * 40)