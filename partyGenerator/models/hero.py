from partyGenerator.signs import assign_random_sign
from partyGenerator.species import get_random_species
import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.combat_strength = random.randint(1, 6)
        self.health_points = random.randint(10, 20)
        self.sign, self.sign_description = assign_random_sign()
        self.species = get_random_species()

    def display_info(self):
        print("**************************************************************************************")
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Awakening Sign: {self.sign} — {self.sign_description}")
        print(f"Combat Strength: {self.combat_strength}")
        print(f"Health Points: {self.health_points}")
        print("**************************************************************************************")