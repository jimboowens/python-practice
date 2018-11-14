for i in range (1,11):
    print i

startingPoint = False
while (startingPoint == False):
    try:
        start = int(raw_input("Please give me a starting point: "))
        if (type(start) == int):
            startingPoint = True
    except:
        print "You entered an invalid character, please try again.."
endingPoint = False
while (endingPoint == False ):
    try:
        end = int(raw_input("Please give me a terminal point: "))+1
        if (type(end) == int):
            endingPoint = True
    except:
            print "You entered an invalid character, please try again.."

if (start > end):
    print "Your starting point is higher than your ending point, and the result is invalid."
for i in range (start, end):
    print i
