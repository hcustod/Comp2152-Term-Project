from character import Character

class Monster(Character):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.survivals = []
        self.evolved = False

    def evolve(self):
        print("The Monster evolves stronger!")
        self.level += 1
        self.combat_strength += 2
        self.evolved = True

    def __del__(self):
        super().__del__()
        print("The Monster object is being destroyed by the garbage collector.")
