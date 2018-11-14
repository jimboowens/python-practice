month = 'november'
print type(month)
date = 13
print type(date)
firstName = 'Jim'
lastName = 'Owens'
print(firstName + " " + lastName)
print date
# this is how I write a comment and add it in via command slash
# name = raw_input ('What is your name? > ')
# print name
# print type(name)
# one = means set the left equal to whatever is on the right.
# two == means compare the left and the right
print 2 ==2
print 2==1
print 2=="2"
gameOn = True
i=0
secretNumber = "5"
print "Game on!"
while(gameOn):
    number = raw_input ("What is the Secret Number? > ")
    # this has to be within the while loop so when the iteration resets the user will see it each time, 
    # but can't be within the if/else statement as it sets the condition to terminate the loop.
    if (number == secretNumber): #the colon means the next indent belongs to this loop
        print 'Yes! You got the Secret Number.'
        gameOn = False
    else:
        print ('Sorry, you guessed wrong. Try again!')
        i+=1
print 'Game Over.'
# find is a good utility, it's for finding something missing. as well as locate
# toilet and figlet prints our large text, but that's not for zsh 
# grep - searches inside files stuff
# sed - 
# top - task manager 
# htop - same with cool colors
# 
