# A class is a RECIPE
# an object is the food you make using the RECIPE
# the recipe can be used an indefinite number of times

# our blueprint for making cars is called Car

class Car(object):
    # whenever we start making a new car, __init__ will run. 
    # we ALWAYS pass self first
    def __init__(self, make):
        # self is special. 
        # self refers to THIS object
        self.make = make #this is an instance, or internal variable
        self.model = "Accord"
        self.year = 2007
my_car = Car("Honda")
print my_car.make
your_car = Car("Toyota")
print your_car.make
your_car.make = "Lexus"
print your_car.make
# an object goes one step further than a dictionary, in that it is more abstract
zacs_car = Car("Ford")
print zacs_car.make