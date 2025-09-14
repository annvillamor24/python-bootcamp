from .character import Character

class Mage(Character):
    def __init__(self, health=10, defense=10, magic=10):
        self._health = health
        self._defense = defense
        self._magic = magic

    def attack(self, other):
        damage = self._magic - other._defense
        other._health -= damage