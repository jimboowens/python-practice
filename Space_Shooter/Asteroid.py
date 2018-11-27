from pygame.sprite import Sprite
from random import randint
class Asteroid(Sprite):
    def __init__(self):
        super(Asteroid,self).__init__()
        self.x = 0
        self.y = randint(1,480)
        self.speed = randint(1,6)
        self.rect = pygame.Rect(0,0,64,64)
        self.rect.centerx = self.x
        self.rect.top = self.y
    def update_me(self, var = randint(1,2)):
        if var ==1:
            self.y+=self.speed
        else:
            self.y-=self.speed