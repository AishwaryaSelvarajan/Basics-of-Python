'''Start with your work from Exercise 8-10. Call the
function make_great() with a copy of the list of magicians’ names. Because the
original list will be unchanged, return the new list and store it in a separate list.
Call show_magicians() with each list to show that you have one list of the original
names and one list with the Great added to each magician’s name.'''

def make_great(magician_names):
    great_magicians = []
    while magician_names:
        new_name = "The great " + magician_names.pop() 
        great_magicians.append(new_name)  
    return great_magicians             

def show_magicians(magician_names):
    for magician_name in magician_names:
        print (magician_name)

names = ['Dumbledore', 'Hagrid', 'Hermoine']
great_magicians_list = make_great(names)
show_magicians (great_magicians_list, names)