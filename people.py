''' Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.'''

people_1= {
    'first_name': 'Aadhi',
    'last_name' : 'Subbu',
    'age' : 2,
    'city' : 'Limerick',
    }

people_2 = {
    'first_name': 'Chaku',
    'last_name' : 'Chika',
    'age' : 3,
    'city' : 'Denver',
}

people_3 = {
    'first_name': 'Chuchu',
    'last_name' : 'Chika',
    'age' : 10,
    'city' : 'Dublin',
}

people = [people_1, people_2, people_3]

for each_people in people:
    print (each_people)