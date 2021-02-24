# Pets

cat = {
    'animal': 'pet animal',
    'owner': 'Linda',
}

hamster = {
    'animal' : 'pet animal',
    'owner' : 'Chacha',
}

pig = {
    'animal' : 'farm animal',
    'owner' : 'Chiku',
}

pets = [cat, hamster, pig]

for pet in pets:
    print ('This is a ' + pet['animal'] + ' and its owner is ' + pet['owner'])