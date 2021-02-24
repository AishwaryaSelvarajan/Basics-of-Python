'''Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a
day of business.'''

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print ("The name of the restaurant is " + self.name + " and it serves " + self.type + " cuisine")
    
    def open_restaurant(self):
        print (self.name + " is open")

    def set_number_served(self, servings):
        self.number_served = servings
        return str(self.number_served)

    def increment_number_served(self,increment):
        self.number_served += increment
        return self.number_served

restaurant = Restaurant("Camile", "Thai")
restaurant.number_served = 50

print ("The restaurant have served " + str(restaurant.number_served) + " people")

# no_of_servings = restaurant.set_number_served('100')
# print ("Now the additional people restaurant served is "+ no_of_servings)

no_of_servings = restaurant.set_number_served(150)
print ("Now the additional people restaurant served is "+ no_of_servings)

increment_in_servings = restaurant.increment_number_served(100)
print ("The increment in servings is " + str(increment_in_servings))