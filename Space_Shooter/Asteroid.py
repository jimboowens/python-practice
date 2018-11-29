import pygame
from pygame.sprite import Sprite
import random
import os

WHITE = (255,255,255)
w = 620
h = 480

pygame.display.set_mode((w, h))
asteroid_image1 = pygame.image.load('asteroidimage1.png').convert_alpha()
asteroid_image2 = pygame.image.load('asteroidimage2.png').convert_alpha()
asteroid_image3 = pygame.image.load('asteroidimage3.png').convert_alpha()


class Asteroid(Sprite):
    def __init__(self):
        super(Asteroid, self).__init__()
        rand_asteroid = random.randint(1,3)

        if rand_asteroid == 1:
            asteroid_image = asteroid_image1
        elif rand_asteroid ==2:
            asteroid_image = asteroid_image2
        else:
            asteroid_image = asteroid_image3

        #Create copy for image rotation
        self.image_orig = asteroid_image
        self.image = self.image_orig.copy()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

        self.radius = int(self.rect.width / 2)

        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)

        self.rect.x = random.randrange(700, 800)
        self.rect.y = random.randrange(0,480)
        self.speedy = random.randrange(-3, 3)
        self.speedx = random.randrange(-6, -1)

        # For Rotation
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()



    def update_me(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > h + 700 or self.rect.left < -25 or self.rect.right > w + 2000:
            self.rect.x = random.randrange(700,800)
            self.rect.y = random.randrange(0, 480)
            self.speedy = random.randrange(1, 8)
            self.rotate_me()


    def rotate_me(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            
            self.rect = self.image.get_rect()
            self.rect.center = old_center     