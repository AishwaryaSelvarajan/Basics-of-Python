# Checking Usernames

current_users = ['mollie', 'eric', 'clark', 'lisa', 'petunia', 'hermoine']
new_users = ['Jancy', 'Janet', 'Lisa', 'Clowda', 'CLARK' ]

for new_user in new_users:
    if new_user.lower() in current_users:
        print ("Hi " + new_user + ", please enter a new username")
    else:
        print ("The username is available")


