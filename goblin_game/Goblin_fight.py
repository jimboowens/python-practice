# this is a procedural approach to a text-based RPG
# The hero is fighting the goblin, and the hero has the option to:
    # 1. fight
    # 2. dance
    # 3. flee

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
        print """%s standeth and fighteth the goblin." 
        You have %d health and %d power." 
        The goblin has %d health and %d power."
        What do you want to do?"
        1. Fight goblin"
        2. Dance"
        3. Flee"
        > """%(hero_name,hero_health,hero_power,goblin_health,goblin_power)
        user_input = raw_input("")
        if user_input == "1":                
            goblin_health -= hero_power
            print "you have done %d damage!" % hero_power
        elif user_input == "2":
            hero_health += 10
            print """The goblin stares in awe of your skill and prowess,
            and your health is now %d""" % hero_health
        else:
            print "I hopeth thou canst live with thineself."
fight()