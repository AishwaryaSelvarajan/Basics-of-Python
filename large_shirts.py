# Large Shirts

def make_shirt(size, text ="I love Python"):
    print ("The shirt size is " + size)
    print ("The text is " + text)

# Function call with medium size and a default text
make_shirt("Medium")

# Function call with Large size and a default text and using keyword arguments
make_shirt(size = "Large")

# Function call with a shirt of any size and another text
make_shirt("small", "I love Javascript")
make_shirt(size = "very small", text = "I love JS")