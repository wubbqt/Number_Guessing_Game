"""
Project 1 - Number Guessing Game
--------------------------------

For this first project you can use Workspaces. 

NOTE: If you prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""
"""Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Save their attempt number to a list.
    6. At the end of the game, show the player, 1) their number of attempts, 2) the mean, median, and mode of the saved attempts list.
    7. Ask the player if they want to play again.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

from multiprocessing.sharedctypes import Value
import random
import statistics


def start_game():
    print("Welcome to the guessing game.")

    guesses = 1
    answer = random.randrange(1,100)
    
    while guesses != 0:
        try:
            user_guess = int(input("Enter a number: "))

            if user_guess == answer:
                print("Got it")
                break

            elif user_guess > answer:
                print("That's a bit too high")
                guesses += 1
                continue

            elif user_guess < answer:
                print("That's a bit too low")
                guesses += 1
                continue
        
        except ValueError: 
            print("Invalid Entry, try again")
        
    return print("It looks like it took you {} trys, not bad".format(guesses))
    



# Kick off the program by calling the start_game function.
start_game()