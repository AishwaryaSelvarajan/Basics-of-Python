# Sandwiches

def make_sandwiches(*toppings):
    print ("The toppings requested for a sandwich are: ")
    for topping in toppings:
        print (topping)



make_sandwiches ('pepperoni')
make_sandwiches ('ham','cheese')
make_sandwiches('butter', 'jam', 'glazed apples')