'''Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating
that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.'''

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print ("The name of the restaurant is " + self.name + " and it serves " + self.type + " cuisine")
    
    def open_restaurant(self):
        print (self.name + " is open")

#my_restaurant = Restaurant("Camile", "Thai")
#print ("The name of the restaurant is " + my_restaurant.name)
#print ("The cuisine it serves is " + my_restaurant.type)

#my_restaurant.describe_restaurant()
#my_restaurant.open_restaurant()

