import pygame
import os
from pygame.sprite import Sprite

pygame.display.set_mode((620, 480))
laser_image = pygame.image.load('laserimage.png')

class Laser(Sprite):
    def __init__(self,shooter):
        super(Laser,self).__init__()
        self.image = pygame.transform.scale(laser_image, (20,50))
        self.rect = self.image.get_rect()
        self.y = shooter.y +80
        self.x = 0
        self.rect.bottom = self.y
        self.rect.centerx = shooter.x
        self.speedx = 20
    def update_me(self):
        self.rect.x += self.speedx
        if self.rect.bottom < 0:
            self.kill()