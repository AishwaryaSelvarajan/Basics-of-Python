'''Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.'''

class User():

    def __init__(self,first_name,last_name,location,age):
        self.f_name = first_name
        self.l_name = last_name
        self.loc = location
        self.age = age
        self.login_attempts = 0
        

    def describe_user(self):
        print ("The following are the user information : ")
        print ("First Name : " + self.f_name)
        print ("Last Name : " + self.l_name)
        print ("Location : " + self.loc)
        print ("Age : " + str(self.age))
        
    def greet_user(self):
        print ("Hello " + self.f_name +" " + self.l_name)

    def increment_login_attempts(self):
        self.login_attempts += 1
        print ("The number of login attempt is " + str(self.login_attempts))

    def reset_login_attempts(self):
        self.login_attempts = 0
        print ("The number of login attempt is " + str(self.login_attempts))


my_user = User("Jacy", "Maze", "Limerick", "16")
my_user.describe_user()
my_user.greet_user()

my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()

my_user.reset_login_attempts()

