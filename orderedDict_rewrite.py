from collections import OrderedDict

glossary = OrderedDict()

glossary = {
    'if-elif-else' : 'For decision making on Multiple conditions',
    'List_comprehension' : 'Making a list using the for statement in a single line',
    'List' : 'Stores items in an ordered way',
    'Dictionaries' : 'Stores the values in Key value pairs',
    'for' : 'To iterate through the items'
}

for keywords, meaning in glossary.items():
    print('\n' + keywords + ":" + "\n" + meaning)