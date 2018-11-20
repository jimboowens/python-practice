import random

class Hero (object):
    def __init__ (self, name):
        self.name = name
        self.health = 10
        self.power = random.randint(0,10)
    def cheer_hero(self):
        print "Welcome, valiant %s! " % (self.name)
    def take_damage(self, amount_of_damage):
        self.health -= amount_of_damage
    def is_alive (self):
        return self.health > 0