'''Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.'''

message = "Please enter a topping to be added"
message += "\nIf you are done with the toppings,please enter quit : "

topping = " "

while topping != "quit":
    topping = input (message)
    print (topping)
