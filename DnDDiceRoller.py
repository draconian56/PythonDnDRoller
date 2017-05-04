######################
# This is a basic    #
# dice roller for my #
# games of DnD       #
######################

from random import * 

print "Welcome to the dice roller"

while True:
    # This line makes sure the user wants to either make the first
    # roll, or wants to continue rolling
    choice = raw_input("Do you want to make a roll? ")
    if choice == "a":
        # Set these two to zero for later
        diceRolled = 0
        total = 0
        # These are the inputs to which the for loop below will use
        diceAmount = input("Please enter how many times you would like to roll: ")
        diceSides = input("Please input how many sides the dice has: ")
        # For loop using the input data from diceAmount
        for i in range(diceAmount):
            # Random number generator using the data input from diceSides
            # This code prints each indivicual value that has been rolled
            # and also adds up the total amount
            diceRolled = randint(1, diceSides)
            total = total + diceRolled
            print diceRolled
        # Prints total
        print total
    # End if
    elif choice == "q":
        exit()
    # End elif
# End while
