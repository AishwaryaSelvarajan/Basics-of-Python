def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Simulate creating a 3D print from the design.
        print ("Printing model: " + current_design)
        completed_models.append (current_design)
        

  