from random import randint

class Die():

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        for i in range(10):
            x = randint(1, self.sides)
            print (x)

# roll_a_die = Die(6)
# roll_a_die.roll_die()

# roll_a_die = Die(10)
# roll_a_die.roll_die()

roll_a_die = Die(20)
roll_a_die.roll_die()

