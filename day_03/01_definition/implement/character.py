class Character:
    def __init__(self, health=10, strength=10, defense=10 ):
        self.health = health
        self.strength = strength
        self.defense = defense

    def attact(self, other):
        damage = self.strength - other.defense
        other.health -= damage

player = Character(strength=10)
enemy = Character()

player.attact(enemy)
print(enemy.health)
