
import math
import pygame
from pygame.sprite import Group, groupcollide, Sprite
from pygame import Rect
class Ship (object):
    def __init__(self):
        self.x = 0
        self.y = 200
        self.speed = 10
        self.should_move_down = False
        self.should_move_up = False
        self.should_move_left = False
        self.should_move_right = False
        self.rect = pygame.Rect(0,0,32,32)
        self.rect.centerx = self.x
        self.rect.top = self.y
        self.surface = pygame.image.load("shipimage.png").convert()
        self.surface.set_colorkey((0,0,0))
        self.health = 11
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
            if self.y > 0:
                self.y -= self.speed
    def take_damage(self, object):
        self.health-=object.damage
    # def collide_test(self, object):
    #     if self.colliderect(object):
    #         self.health -=object.damage
