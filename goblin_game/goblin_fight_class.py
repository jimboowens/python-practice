import os
import random
from Hero import Hero
from Goblin import Goblin
from Vampire import Vampire
hero_name = raw_input( "What is your name, brave soul? > ")
theHero = Hero(hero_name)
theHero.cheer_hero()

while (theHero.is_alive()):
    randMonster = random.randint(1,3)
    if randMonster == 1:
        monster = Goblin()
    else:
        monster = Vampire()
    print "You encountered a wild %s!" % monster.name
    while(theHero.is_alive() and monster.is_alive()):
        message = """        You have %d health and %d power.
        The monster has %d health and %d power.
        What do you want to do?
        1. fight %s
        2. do a little dance
        3. flee""" 
        print message % (theHero.health,theHero.power, monster.health, monster.power, monster.name)
        # Get the user's choice
        user_input = raw_input("> ")

        if user_input == "1":
            # The hero has decided to attack!
            # subtract goblins health by hero power
            monster.take_damage(theHero.power)
            print "You have done %d damage to the monster!" % theHero.power
        elif user_input == "2":
            theHero.health += 10
            print """The monster stares at you in disbelief of your skill and prowess. 
            His jaw drops as your wounds heal."""
            print "Your health is now %d" % theHero.health
        elif user_input == "3":
            print "I hopeth thou canst live with thineself, %s" % theHero.name
            # the break statement will end the loop IMMEDIATELY!!
            break
        else:
            # user entered something that we didnt offer
            print "Thou fool. Thou hast stumbledeth (invalid input)"
        # Now, it's the monster's turn
        # unless he just died from the hero attack
        if monster.health > 0:
            theHero.health -= monster.power
            print "The monster hits you for %d damage" % monster.power
            if theHero.health <= 0:
                print "Thou hast been slain."
                break
        # else:
            # os.system("say Hooray. Thou hast killed the monster!")
        if theHero.health < 5:
            print "%s has gone into a rage as death appraoches. Power increased!" % hero_name
            theHero.power += 5
        if not theHero.is_alive: 
            print 'You died... Game over!'
            break
    if theHero.is_alive() and monster.is_alive() == False:
        play_again = raw_input("You win! Play again (y or n)? > ")
        if play_again == "y":
            monster.is_alive == True
        else:
            break
        os.system("clear")
        

