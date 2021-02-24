'''Make a list of magician’s names. Pass the list to a function
called show_magicians(), which prints the name of each magician in the list.'''

def show_magicians(magician_names):
    for magician_name in magician_names:
        print (magician_name)

names = ['Dumbledore', 'Hagrid', 'Hermoine']
show_magicians(names)