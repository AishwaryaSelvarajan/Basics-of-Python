'''Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by adding
the phrase the Great to each magician’s name. Call show_magicians() to
see that the list has actually been modified.'''

def make_great(magician_names):
    great_magicians = []
    while magician_names:
        new_name = "The great " + magician_names.pop() 
        great_magicians.append(new_name)  
    return great_magicians             

def show_magicians(original_lists, magician_names):
    for magician_name in magician_names:
        print (magician_name)
    for original_list in original_lists:
        print (original_list)

names = ['Dumbledore', 'Hagrid', 'Hermoine']
great_magicians_list = make_great(names[:])
show_magicians (names, great_magicians_list)
