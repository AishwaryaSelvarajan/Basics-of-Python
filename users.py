'''Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.'''

class User():

    def __init__(self,first_name,last_name,location,age):
        self.f_name = first_name
        self.l_name = last_name
        self.loc = location
        self.age = age

    def describe_user(self):
        print ("The following are the user information : ")
        print ("First Name : " + self.f_name)
        print ("Last Name : " + self.l_name)
        print ("Location : " + self.loc)
        print ("Age : " + str(self.age))
        
    def greet_user(self):
        print ("Hello " + self.f_name +" " + self.l_name)

my_user = User("Jacy", "Maze", "Limerick", "16")
my_user.describe_user()
my_user.greet_user()

