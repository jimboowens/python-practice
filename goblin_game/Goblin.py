import random

class Goblin (object):
    def __init__ (self):
        self.name = "Goblin"
        self.health = 6
        self.power = random.randint(2,6)
    def take_damage(self, amount_of_damage):
        self.health -= amount_of_damage
    def is_alive(self):
        return self.health > 0