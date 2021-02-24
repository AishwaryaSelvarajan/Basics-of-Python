''' Every Function: Think of something you could store in a list. For example,
you could make a list of mountains, rivers, countries, cities, languages, or anything
else you’d like. Write a program that creates a list containing these items
and then uses each function introduced in this chapter at least once.'''

cities = ['Maharashtra','Tamil Nadu', 'Kerala','Andhra Pradesh','Pondicherry']

# Inserting elements into a list
cities.insert(1,'Assam')

# Adding elements to a list
cities.append('West Bengal')

print (cities)

# Removing elements from a list using del statement
del cities[1]
print (cities)

# Removing an item using the pop method from any position in a list
cities.pop(0)
print(cities)

# Removing an item using pop() method
cities.pop()
print(cities)

# Removing an item by value
cities.remove('Tamil Nadu')
print(cities)

# Sorting a list temporarily with sorted() method
print(sorted(cities))

# Sorting a list temporarily with sorted() method, with reverse=True
print(sorted(cities, reverse=True))
print (cities)

# Sorting a list permanently using sort() method
cities.sort()
print (cities)

# Printing a list in reverse order
cities.reverse()

# Print the length of list
print (len(cities))

