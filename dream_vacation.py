'''Write a program that polls users about their dream
vacation. Write a prompt similar to If you could visit one place in the world,
where would you go? Include a block of code that prints the results of the poll.'''

# Creating a dictionary to store the name and the user's dream location

responses= {}

polling_active = True

while polling_active:
    name = input ("Please enter your name: ")
    dream_location = input ("If you would visit one place, where would you go? : ")
    responses[name] = dream_location

    repeat = input ("Would you like another user to provide their response? (yes/no) : ")
    if repeat == "no":
        polling_active = False

for user, location in responses.items():
    print (user + " wishes to visit " + location)

