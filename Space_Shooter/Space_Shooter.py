import pygame
import random
from Ship import Ship
from Asteroid import Asteroid
from Comet import Comet
from Laser import Laser
from Candy import Candy
from Button import Start_Button
from pygame.sprite import Group, groupcollide

screen_size = (620,480)
tick = 0

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode(screen_size)
screen = pygame.display.set_caption("SPACE SHOOTER")

background_image = pygame.image.load('background.png')
ship_image = pygame.image.load('ship.png')
asteroid_image1 = pygame.image.load('asteroidimage1.png')
asteroid_image2 = pygame.image.load('asteroidimage2.png')
asteroid_image3 = pygame.image.load('asteroidimage3.png')
comet_image = pygame.image.load('cometimage.png')
candy_image = pygame.image.load('candyimage.png')
laser_image = pygame.image.load('laser.png')

running = True  
while running:
    tick +=1   
    if event.type == pygame.QUIT
        running = False
    elif event.type == pygame.KEYDOWN:
        # the user pressed a key!!!
        print (event.key)
        if event.key == 275:
            theHero.should_move("right")
        elif event.key == 276:
            theHero.should_move("left")
        if event.key == 273:
            theHero.should_move("up")
        elif event.key == 274:
            theHero.should_move("down")
        elif event.key == 32:
            new_arrow = Arrow(theHero)
            arrows.add(new_arrow)
    elif event.type == pygame.KEYUP:
        if event.key == 275:
            theHero.should_move("right",False)
        elif event.key == 276:
            theHero.should_move("left",False)
        if event.key == 273:
            theHero.should_move("up",False)
        elif event.key == 274:
            theHero.should_move("down",False)
    elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos();
        if start_button.rect.collidepoint(mouse_x, mouse_y):
            game_start = True;
            bg_music = pygame.mixer.Sound('faf.wav');
            bg_music.play();
    
    screen.fill(black)
    pygame_screen.blit(background_image,[0,0])
        theHero.draw_me(512,480)
        if game_start == True:
            
            for asteroid in asteroids:
                asteroid.update_me(theHero)
                pygame_screen.blit(monster_image,[asteroid.x,asteroid.y])

            for arrow in arrows:
                arrow.update_me(asteroid)
                pygame_screen.blit(arrow.img,[arrow.x,arrow.y])
                
                pygame_screen.blit(hero_image,[theHero.x,theHero.y])

                arrow_hit = groupcollide(arrows,asteroids,True,True)
                # print arrow_hit
                if arrow_hit:
                    asteroids.add(asteroid)

        if game_start == False:
            start_button.setup_message()
            start_button.draw_button()
        
        pygame.display.flip()