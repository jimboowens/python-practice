import random

class Vampire (object):
    def __init__ (self):
        self.name = "Vampire"
        self.health = 12
        self.power = random.randint(5,8)
    def take_damage(self, amount_of_damage):
        self.health -= amount_of_damage
    def is_alive(self):
        return self.health > 0
    def make_girls_swoon(self):
        print "the ladies faint at the sight of his fiery fantastic fangs."