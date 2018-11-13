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
while(gameOn == True):
    number = raw_input ("What is the Secret Number? > ")
    if (number == secretNumber):
        print 'Yes! You got the Secret Number.'
        gameOn = False

    else:
        print ('Sorry, you guessed wrong. Try again!')
        i+=1
