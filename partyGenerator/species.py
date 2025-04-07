import random

SPECIES = [
    "Human",
    "Elf",
    "Dwarf",
    "Orc",
    "Fae"
]

def list_species():
    return SPECIES

def get_random_species():
    return random.choice(SPECIES)
