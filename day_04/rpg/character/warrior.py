from .character import Character

class Warrior(Character):
    def __init__(self, health=10, defense=10, strength=10):
        self._health = health
        self._defense = defense
        self._strength = strength