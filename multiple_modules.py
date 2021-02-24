'''Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.'''

from module1_user import User
from module2_privileges_admin import Privileges, Admin

my_user = Admin("Jacy", "Maze", "Limerick", "16")
my_user.privileges.show_privileges()