


'''Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.'''

from module1_user import User

class Privileges():
    
    def __init__(self, privileges_list = ["can add post", "can delete post", "can ban user"]):
        self.privilege = privileges_list

    def show_privileges(self):
        print ("The following are the priveleges the Admin has: ")
        for roles in self.privilege:
            print (roles)

class Admin (User):

    def __init__(self,first_name,last_name,location,age):
        super().__init__(first_name,last_name,location,age)
        self.privileges = Privileges()