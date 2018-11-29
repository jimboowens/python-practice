import pygame
import os
import random
from Ship import Ship
from Asteroid import Asteroid
from Comet import Comet
from Laser import Laser
from Candy import Candy
from Start_Button import Start_Button
from pygame.sprite import Sprite, Group, groupcollide

screen_size = (620,480)
tick = 0
running = True 
game_start = False

# os.system('start d:\spacesounds.wav')

pygame.init()
pygame.mixer.init()
# background_music = pygame.mixer.Sound('spacesounds.wav')
# background_music.play()

pygame_screen = pygame.display.set_mode(screen_size)
picture = pygame.transform.scale(pygame_screen, (620, 480))
# You can then get the bounding rectangle of picture with

rect = pygame_screen.get_rect()
# and move the picture with

rect = rect.move((0, 0))

screen = pygame.display.set_caption("SPACE SHOOTER")

background_image = pygame.image.load('background1.png')
ship_image = pygame.image.load('shipimage.png').convert()
ship_image.set_colorkey((0,0,0))
ship_image = pygame.transform.scale(ship_image,(40,64))
ship_image = ship_image.convert()
comet_image = pygame.image.load('cometimage.png').convert()
comet_image.set_colorkey((0,0,0))
comet_image = pygame.transform.scale(comet_image,(40,64))
comet_image = comet_image.convert()
candy_image = pygame.image.load('candyimage.png').convert()
candy_image.set_colorkey((0,0,0))
candy_image = pygame.transform.scale(candy_image,(40,64))
candy_image = candy_image.convert()
asteroid_image1 = pygame.image.load('asteroidimage1.png').convert()
asteroid_image1.set_colorkey((255,0,255))
asteroid_image1  = pygame.transform.scale(asteroid_image1,(40,64))
asteroid_image1  = asteroid_image1.convert()
asteroid_image2 = pygame.image.load('asteroidimage2.png').convert()
asteroid_image2.set_colorkey((255,0,255))
asteroid_image2 = pygame.transform.scale(asteroid_image2,(40,64))
asteroid_image2 = asteroid_image2.convert()
asteroid_image3 = pygame.image.load('asteroidimage3.png').convert()
asteroid_image2.set_colorkey((255,0,255))
asteroid_image2 = pygame.transform.scale(asteroid_image2,(40,64))
asteroid_image2 = asteroid_image2.convert()
laser_image = pygame.image.load('laserimage.png').convert()
# ship_image.set_colorkey((255,255,255))
# screen.blit(ship_image,(0,0))
ship = Ship()
asteroids = Group()
asteroids.add(Asteroid())
comets = Group()
comets.add(Comet())
lasers = Group() 
lasers.add(Laser(ship))
start_button = Start_Button(pygame_screen)

while running:
    tick += 1
    if tick % 90 == 0:
        asteroids.add(Asteroid()) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # print (event.key)
            if event.key == 275:
                ship.should_move("right")
            elif event.key == 276:
                ship.should_move("left")
            if event.key == 273:
                ship.should_move("up")
            elif event.key == 274:
                ship.should_move("down")
            elif event.key == 32:
                new_laser = Laser(ship)
                lasers.add(new_laser)
        elif event.type == pygame.KEYUP:
            if event.key == 275:
                ship.should_move("right",False)
            elif event.key == 276:
                ship.should_move("left",False)
            if event.key == 273:
                ship.should_move("up",False)
            elif event.key == 274:
                ship.should_move("down",False)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if start_button.rect.collidepoint(mouse_x, mouse_y):
                game_start = True
            
    pygame_screen.fill((0,0,0))
    pygame_screen.blit(background_image,[-tick,0])
    ship.draw_me(620,480)
    if game_start == True:        
        for asteroid in asteroids:
            asteroid.update_me()
            pygame_screen.blit(asteroid.image,[asteroid.rect.x,asteroid.rect.y])
        for comet in comets:
            comet.update_me()
            pygame_screen.blit(comet_image,[comet.rect.x,comet.rect.y])
        for laser in lasers:
            laser.update_me()
            pygame_screen.blit(laser_image,[laser.rect.x,laser.rect.y])
            pygame_screen.blit(ship_image,[ship.rect.x,ship.y])
            laser_hit = groupcollide(lasers,asteroids,True,True)
        # for event in pygame.Rect.colliderect(ship,asteroids):
        #     ship.take_damage()
    if game_start == False:
        start_button.setup_message()
        start_button.draw_me()
        
    pygame.display.flip()
