# Icecream Stand

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print ("The name of the restaurant is " + self.name + " and it serves " + self.type + " cuisine")
    
    def open_restaurant(self):
        print (self.name + " is open")

class IceCreamStand (Restaurant):

    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = 'Vanilla'

    def icecream_flavors(self):
        print ("This restaurant sells " + self.flavors + " icecream")


my_restaurant = IceCreamStand("Camile", "Thai")

my_restaurant.describe_restaurant()
my_restaurant.icecream_flavors()

