'''Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the value
that’s returned.'''

def city_country(city, country):
    formatted_string = "\"" + city + ", " + country + "\""
    return formatted_string

final_output = city_country("Dublin", "Ireland")
print (final_output)

final_output = city_country("Delhi", "India")
print (final_output)

final_output = city_country("Des Moines", "USA")
print (final_output)
