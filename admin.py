#Admin

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

class Admin (User):

    def __init__(self,first_name,last_name,location,age):
        super().__init__(first_name,last_name,location,age)
        self.priveleges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print ("The following are the priveleges the Admin has: ")
        for privileges in self.priveleges:
            print (privileges)

my_user = Admin("Jacy", "Maze", "Limerick", "16")
my_user.show_privileges()
