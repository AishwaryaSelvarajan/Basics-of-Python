'''Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.'''

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print ("The name of the restaurant is " + self.name + " and it serves " + self.type + " cuisine")
    
    def open_restaurant(self):
        print (self.name + " is open")

my_restaurant_1 = Restaurant("Zaitoon", "Arabic")
my_restaurant_2 = Restaurant("Little Italy", "Italy")
my_restaurant_3 = Restaurant("Hot Chips", "Tamil Nadu")

my_restaurant_1.describe_restaurant()
my_restaurant_2.describe_restaurant()
my_restaurant_3.describe_restaurant()