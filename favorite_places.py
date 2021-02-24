# Favorite Places

favorite_places = {
    'Subbu' : ['Switzerland' , 'France', 'Netherland'],
    'Chacha' : ['Venice', 'Wayanad', 'Shimoga'],
    'Chiku' : ['London', 'Paris', 'Belfast']
    }

for name, places in favorite_places.items():
    print (name + "'s favorite places are: ")
    for place in places:
        print (place)