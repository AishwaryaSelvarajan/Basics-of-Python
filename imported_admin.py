'''Start with your work from Exercise 9-8 (page 178).
Store the classes User, Privileges, and Admin in one module. Create a separate
file, make an Admin instance, and call show_privileges() to show that
everything is working correctly.'''

from privileges import Admin, Privileges, User

my_user = Admin("Jacy", "Maze", "Limerick", "16")
my_user.privileges.show_privileges()





