# this is a procedural approach to a text-based RPG
# The hero is fighting the goblin, and the hero has the option to:
    # 1. fight
    # 2. dance
    # 3. flee
import os

# os.system() will take any command, and python will run it if it can
hero_name = raw_input("What is thy name, brave adventurer? > ")
print "Welcome, %s! Thou art a brave soul!" % hero_name
# were a variable set within a function, the variable is not global. 
# it's like a private function almost
def fight ():
    hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2
    while (hero_health > 0 and goblin_health > 0):
        message_intro =  """%s, You have %d health and %d power.
        The goblin has %d health and %d power.
        What do you want to do?
        1. Fight goblin
        2. Dance
        3. Flee"""
        print message_intro %(hero_name,hero_health,hero_power,goblin_health,goblin_power)
        user_input = raw_input("        > ")
        if user_input == "1": 
            goblin_health -= hero_power
            message = """%s standeth and fighteth the goblin.            
            you have done %d damage!
            The goblin's remaining health is %d"""
            print message %(hero_name,hero_power,goblin_health)
        elif user_input == "2":
            hero_health += 10
            print """The goblin stares in awe of your skill and prowess, and your health is now %d""" % hero_health
        else:
            print "I hopeth thou canst live with thineself."
            break
        # now is the time for the goblin to get it!
        if goblin_health > 0:
            hero_health-=goblin_power
            print "The goblin hits you for %d damage." %goblin_power
        if hero_health<= 0:
                print "Thou hast been slain, fair saint."
                # no need to break, but could to simplify
        if hero_health<5:
            print "Thou hast gone into a rage as death approacheth, tout suite thine power increases!"
            hero_health+=5
        else:
            os.system("say Hooray. Thou hast killed the goblin.")
        raw_input("Hit return to continue _ ")
        os.system("clear")
fight()