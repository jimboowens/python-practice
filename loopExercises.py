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
    print "Your starting point is higher than your ending point, and the result is invalid. Moving on.."
for i in range (start, end):
    print i
for i in range (1,10,2):
    print i
for i in range (1,6):
    print "*"*5
startingPointSquare = False
while (startingPointSquare == False):
    try:
        square = int(raw_input("Please give me a width for the square: "))
        if (type(start) == int):
            startingPointSquare = True
    except:
        print "You entered an invalid character, please try again.."
for i in range (1,square+1):

    print "*"*square


lengthTruth = False
while (lengthTruth == False):
    try:
        length = int(raw_input("Please give me a length: "))
        if (type(start) == int):
            lengthTruth = True
    except:
        print "You entered an invalid character, please try again.."
widthTruth = False
while (widthTruth == False ):
    try:
        width = int(raw_input("Please give me a width: "))+1
        if (type(end) == int):
            widthTruth = True
    except:
            print "You entered an invalid character, please try again.."
for i in range (1,length+1):
    if (i==1):
        print "*"*width
    elif (i>1 and i<length):
       print  "*"+ " " * (width - 2) + "*"
    else:
       print  "*"*width
