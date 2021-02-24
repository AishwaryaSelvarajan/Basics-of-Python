'''Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message saying
they’ll have to wait for a table. Otherwise, report that their table is ready.'''

number_of_people = input ("How many people are there for Dining? : ")
number_of_people = int(number_of_people)

if (number_of_people > 8):
    print ("Please wait for a while")
else:
    print ("Your table is ready")