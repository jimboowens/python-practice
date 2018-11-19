# Electronic Phone Book
# =====================
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry
# 4. List all entries
# 5. Quit
# What do you want to do (1-5)?
# If they choose to look up an entry, you will ask them for the person's name, and then look up the person's phone number by the given name and print it to the screen.
# If they choose to set an entry, you will prompt them for the person's name and the person's phone number,
# If they choose to delete an entry, you will prompt them for the person's name and delete the given person's entry.
# If they choose to list all entries, you will go through all entries in the dictionary and print each out to the terminal.
# Search for an entry
# You can limit this to Name, or loop through the entire dictionary
# If they choose to end_book, end the program.
end_book = False
user_verify_truth = False
name_name = ""
name_number = ""
# class Phone_book:
#     def __init__(self, name, number):
#         self.name = name_name
#         self.number = name_number
# p1 = Phone_book("Melissa", "584-394-5857")
# p2 = Phone_book("Igor","857-485-2935")
# p3 = Phone_book("Jazz", "334=584-2345")
phone_book = {
    "Melissa":"584-394-5857",
    "Igor":"857-485-2935",
    "Jazz": "334-584-2345"
}
while end_book == False:

    print """Electronic Phone Book
    =====================
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Quit"""
    while user_verify_truth == False: 
        try:
            user_input = int(raw_input("What do you want to do? > ").upper())
            if type(user_input) == int :
                user_verify_truth = True
        except:
            print "You entered an invalid character, please try again.."
    if user_input == 1:
        # command
        name_query = raw_input ("What name would you like to look up? > ").upper()
        print name_query
        print (name_query.name)
        print (name_query.number)
        user_verify_truth = False
    if user_input == 2:
        name_entry = raw_input ("What name would you like to set? > ").upper()
        name_name = raw_input ("What is the name of the contact you would like to set? > ").upper()
        name_number = raw_input ("What is their phone number? > ")
        print "Entry stored for %s" %name_name
        # command
        user_verify_truth = False
    if user_input == 3:
        # command
        user_verify_truth = False
    if user_input == 4:
        # command
        user_verify_truth = False
    if user_input == 5:
        break
