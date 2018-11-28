
import math
<<<<<<< HEAD
from pygame.sprite import Group, groupcollide
class Ship (object):
=======

class Ship (self):
>>>>>>> 8ea8be6c0342d672ed0164f1f6d606f7716fcc3d
    def __init__(self):
        self.x = 0
        self.y = 200
        self.speed = 10
        self.should_move_down = False
        self.should_move_up = False
        self.should_move_left = False
        self.should_move_right = False
<<<<<<< HEAD
        self.health = 11
=======
>>>>>>> 8ea8be6c0342d672ed0164f1f6d606f7716fcc3d
    def should_move(self,direction, start = True):
        if direction == "right":
            self.should_move_right = start
        elif direction == "left":
            self.should_move_left = start
        if(direction == "up"):
            self.should_move_up = start
        elif(direction == "down"):
            self.should_move_down = start
    def draw_me(self, w, h):
        if(self.should_move_right):
            if self.x < 155:
                self.x += self.speed
        elif(self.should_move_left):
            if self.x > 0:
                self.x -= self.speed
        if(self.should_move_down):
            if self.y < 420:
                self.y += self.speed
        elif self.should_move_up:
            if self.y > 32:
<<<<<<< HEAD
                self.y -= self.speed
    def take_damage(self, object):
        self.health-=object.damage
=======
                self.y -= self.speed
>>>>>>> 8ea8be6c0342d672ed0164f1f6d606f7716fcc3d
