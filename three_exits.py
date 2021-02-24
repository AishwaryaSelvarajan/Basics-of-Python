'''Write different versions of either Exercise 7-4 or Exercise 7-5
that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value.'''

while True:
    age = input ("Please enter the age: ")
    age = int(age)

    if age >= 0 and age <= 3:
        print ("The ticket is free")
        break
    elif age > 3 and age <= 12:
        print ("The price of the ticketis 10 dollars")
        break
    elif age > 12:
        print ("The price of the ticket is 15 dollars")
        break
    else:
        print ("Sorry, please enter an valid age")
