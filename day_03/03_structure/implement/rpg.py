from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, health=10, defense=10):
        self._health = health
        self._defense = defense

    @abstractmethod
    def attack(self, other):
        raise NotImplementedError()

class knight(Character):
    def attack(self, other):
        damage = self._defense - other._defense
        other._health -= damage

class Mage(Character):
    def __init__(self, health=10, defense=10, magic=10):
        self._health = health
        self._defense = defense
        self._magic = magic

    def attack(self, other):
        damage = self._magic - other._defense
        other._health -= damage

class Warrior(Character):
    def __init__(self, health=10, defense=10, strength=10):
        self._health = health
        self._defense = defense
        self._strength = strength

    def attack(self, other):
        damage = self._strength - other._defense
        other._health -= damage