import random

class Character:
    def __init__(self):
        self._combat_strength = random.randint(5, 10)
        self._health_points = random.randint(20, 30)

    @property
    def combat_strength(self):
        return self._combat_strength

    @combat_strength.setter
    def combat_strength(self, value):
        self._combat_strength = max(0, value)

    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, value):
        self._health_points = max(0, value)

    def __del__(self):
        return 1