import pygame
import os
import random
from Ship import Ship
from Asteroid import Asteroid
from Comet import Comet
from Laser import Laser
from Candy import Candy
from Start_Button import Start_Button
from pygame.sprite import Group, groupcollide

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
screen = pygame.display.set_caption("SPACE SHOOTER")

background_image = pygame.image.load('background1.png')
ship_image = pygame.image.load('shipimage.png')
comet_image = pygame.image.load('cometimage.png')
candy_image = pygame.image.load('candyimage.png')
asteroid_image1 = pygame.image.load('asteroidimage1.png')
asteroid_image2 = pygame.image.load('asteroidimage2.png')
asteroid_image3 = pygame.image.load('asteroidimage3.png')
laser_image = pygame.image.load('laserimage.png')

ship = Ship()
asteroids = Group()
asteroids.add(Asteroid())
comets = Group()
comets.add(Comet())
lasers = Group() 
lasers.add(Laser(ship.x,ship.y))
start_button = Start_Button(pygame_screen)

while running:
    tick += 1  
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
                new_arrow = Arrow(ship)
                arrows.add(new_arrow)
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
            
    
    pygame_screen.blit(background_image,[0,0])
    ship.draw_me(620,480)
    if game_start == True:        
        for asteroid in asteroids:
            asteroid.update_me()
            pygame_screen.blit(asteroid.image,[asteroid.rect.x,asteroid.rect.y])
        for comet in comets:
            comet.update_me()
            pygame_screen.blit(asteroid.image,[comet.rect.x,comet.rect.y])
        for laser in lasers:
            laser.update_me()
            pygame_screen.blit(laser_image,[laser.rect.x,laser.rect.y])
            pygame_screen.blit(ship_image,[ship.rect.x,ship.y])
            laser_hit = groupcollide(lasers,asteroids,True,True)

    if game_start == False:
        start_button.setup_message()
        start_button.draw_me()
        
    pygame.display.flip()
