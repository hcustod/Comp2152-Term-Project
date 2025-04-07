from partyGenerator.signs import assign_random_sign
from partyGenerator.species import get_random_species
from character import Character
import random

class Hero(Character):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.combat_strength = random.randint(1, 6)
        self.health_points = random.randint(10, 20)
        self.sign, self.sign_description = assign_random_sign()
        self.species = get_random_species()
        # Evo
        self.wins = []
        self.special_ability = False
        self.level = 1

    def display_info(self):
        print("**************************************************************************************")
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Awakening Sign: {self.sign} — {self.sign_description}")
        print(f"Combat Strength: {self.combat_strength}")
        print(f"Health Points: {self.health_points}")
        print("**************************************************************************************")

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