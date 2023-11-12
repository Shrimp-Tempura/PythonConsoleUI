import time
import os


mainMenu = [1, 2, 3, 4, 5, 6, 7, 8, 9, "exit"]

def printChoices(choiceIndex: int, choiceMenu: list):
    """Prints a list of options for the user.
    
    Places brackets around the current choice (with index of choiceIndex)
    """
    # Add a space before first choice if user choice is not chosen.
    if choiceIndex != 0:
        print(" ", end="")
    # Print the choices
    for choice in choiceMenu:
        # If the choice is currently chosen, add "[]" arount it.
        if choiceMenu.index(choice) == choiceIndex:
            print("[" + str(choice) + "]", end=" ")
        elif choiceMenu.index(choice) == choiceIndex - 1:
            print(choice, end=" ")
        # Else, just print the choice.
        else:
            print(choice, end="  ")
    print(" ")

def askUserChoice(choiceMenu: list):
    """Prints choices and allows user to change choice.
    
    Returns the choice chosen.
    """
    currentChoice = 0 # By defult, user's choice has an index of 0.
    while True:
        coverTitle = open("sometitle.txt", "r") # Might remove (or add it as an argument)
        print(coverTitle.read())
        printChoices(currentChoice, choiceMenu)
        key = input()
        os.system('clear')
        if key == "d" and currentChoice != len(choiceMenu) - 1:
            currentChoice += 1
            continue
        elif key == "a" and currentChoice != 0:
            currentChoice -= 1
            continue
        elif key == "e":
            break
        elif key == "w":
            return choiceMenu[currentChoice]

while True:
    finalChoice = askUserChoice(mainMenu)
    print(finalChoice)
    break

