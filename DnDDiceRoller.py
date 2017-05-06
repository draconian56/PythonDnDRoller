######################
# This is a basic    #
# dice roller for my #
# games of DnD       #
######################

from random import *

print "Welcome to the dice roller"

while True:
    choice = raw_input("Do you want to make a roll? ")
    if choice == "":
        diceRolled = 0
        total = 0
        while True:
            try:
                diceAmount = int(raw_input("Please enter how many times you would like to roll: "))               
            except ValueError:
                print "Not an int, try again: "
                continue
            else:
                break
        while True:
            try:
                diceSides = int(raw_input("Please input how many sides the dice has: "))
            except ValueError:
                print "Not an int, try again: "
                continue
            else:
                break
        for i in range(diceAmount):
            diceRolled = randint(1, diceSides)
            total = total + diceRolled
            print diceRolled  
        print total
    elif choice == "no":
        break
exit()
