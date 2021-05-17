import random

print("This is a cool dice rolling sim. Very exciting.")

def diceroll():
    keepPlaying = True
    while keepPlaying is True:
        roll = random.randint(1, 6)
        answer = input("\nRoll the dice? ")
        if answer == "yes" or answer == "Yes" or answer == "y" or answer == "Y":
            print(roll)
        else:
            print("\nOkay then... that's lame.")
            keepPlaying = False

diceroll()




