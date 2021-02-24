'''Ask the user for a number, and then report whether the
number is a multiple of 10 or not.'''

number = input("Please enter a numberto check whether it is multiple of 10 or not? : ")
number = int(number)

if (number % 10 == 0):
    print ("The number is a multiple of 10")
else:
    print ("The number is not a multiple of 10")