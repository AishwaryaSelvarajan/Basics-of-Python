# Favorite Numbers

fav_numbers = {
    'Aadhirayan' : ['9', '5'],
    'Chacha' : ['10', '20'],
    'Linda': ['40','6'],
    'Sagar' : ['3', '8'],
}

for name, numbers in fav_numbers.items():
    print (name + "'s favorite numbers are: ")
    for number in numbers:
        print (number)

