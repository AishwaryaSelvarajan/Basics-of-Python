# Styling

def describe_city(city,country="India"):
    print (city + " is in " + country)

describe_city("Pune")
describe_city("Chennai")
describe_city("Limerick", "Ireland")

# User Profile

def user_profile(f_name, l_name, **user_info):
    profile = {}
    profile['first'] = f_name
    profile['last'] = l_name
    for key, value in user_info.items():
        profile[key] = value
    print (profile)

user_profile ('Linda','Sam',location='Alaska',experience='2 years in IT',previous_employer='Fidelity')