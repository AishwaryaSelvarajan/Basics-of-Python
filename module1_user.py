'''Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.'''

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
