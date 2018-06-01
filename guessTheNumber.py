# May 31, 2018 - Victoria's first programming project in Python.

# This is a 'Guess the Number' game. The user will be prompted to input
# a number between 1 and 10. If they're correct, they win! If they're
# incorrect, the game will tell them if they need to guess higher or
# lower. The user will get three tries.

import random

# Intro
print("""Welcome to 'Guess the Number'! Guess the number between 1 and 10, and you win!""")
print()

# Set up the iterator
guessCount = 3

# Set up the RNG
r = random.randint(1,11)

# Print the generated number for testing purposes
#print (r)

# While the number of guesses is greater than zero
while guessCount > 0:
    if guessCount == 1:
        print("You have " + str(guessCount) + " guess remaining.")
    else:
        print("You have " + str(guessCount) + " guesses remaining.")
    guess = int(input("What number do you guess? "))
    # Check if the guess was correct
    if guess == r:
        print("Congratulations! You win!")
        break
    else:
        # Guess is too high
        if guess > r and guess < 11:
            print ("Your guess was too high.")
            guessCount -= 1
            print()
            # Out of tries
            if guessCount == 0:
                print("The number was " + str(r) + ".")
                print("Game Over")
                break
            continue
        # Guess is too low
        elif guess < r and guess > 0:
            print("Your guess was too low.")
            guessCount -= 1
            print()
            # Out of tries
            if guessCount == 0:
                print("The number was " + str(r) + ".")
                print("Game Over")
                break
            continue
        else:
            print("Sorry, your guess wasn't a number between 1 and 10.")
            guessCount -= 1
            print()
            continue
