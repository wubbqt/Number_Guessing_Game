import statistics
import random
   # write your code inside this function.


def start_game():
    print("Welcome to the guessing game.")

    guesses = 1
    answer = random.randrange(1, 100)
    print(answer)

    while guesses != 0:
        try:
            user_guess = int(input("Enter a number: "))
            print("That's not a valid entry")

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

    return print("It looks like it took you {} trys, not bad".format(guesses))


start_game()
