# this is a thing about dictionaries; they seem very useful for lists and changing values.
# Dictionaries are just like lists, but instead of numbered indices they have english indices.
# it's like a key
greg = [
    "Greg",
    "Male",
    "Tall",
    "Developer",
]

# This is not intuitive, and the placeholders give no indication as to what they represent

# Key:value pair

greg = {
    "name": "Greg",
    "gender": "Male",
    "height": "Tall",
    "job": "Developer",
}
# make a new dictionary
zombie = {}#dictionary

zombies = []#list
zombie['weapon'] = "fist"
zombie['health'] = 100
zombie['speed'] = 10

print zombie
# zombie stores the items it comprises in random order.
print zombie ['weapon']
for key, value in zombie.items():#key is basically an i, and I don't get how it iterated because both change...?
    print "zombie has a key of %s with a value of %s" % (key, value)

zombies.append({
    'name': "Hank",
    'weapon': "baseball bat",
    'speed': 10
})
zombies.append({
    'name': "Willy",
    'weapon': "axe",
    'speed': 3,
    'victims': ['squirrel', 'rabbit', 'Hank']
})
print zombies[1]['victims'][1]