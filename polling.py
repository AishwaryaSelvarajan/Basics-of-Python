# Polling

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'dutta' : 'perl',
    'janet' : 'ruby',
    'linda' : 'java'
}

people_polls = ['jen', 'lara', 'dutta', 'sarah', 'edward', 'lychee']

list_of_people = [people for people in favorite_languages.keys()]
for people in people_polls:
    if people.lower() in list_of_people:
        print ("Thank you " + people + ", for responding")
    else:
        print ("Hi " + people + ", could you please take up the poll")

    
