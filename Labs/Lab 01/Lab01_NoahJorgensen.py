# 1. Name:
#    Noah Jorgensen
# 2. Assignment Name:
#    Lab 01: Python Review
# 3. Assignment Description:
#    This is a guessing game where the user tries to guess a random number
# 4. What was the hardest part? Be as specific as possible.
#    I forgot to cast some variables. Once I did that the program ran great.
# 5. How long did it take for you to complete the assignment?
#    About 45 minutes including making the video.
 
import random

# Game introduction.
print(
    """This is the "guess a number" game.
You try to guess a random number in the smallest number of attempts."""
)
# Prompt the user for how difficult the game will be. Ask for an integer.
while True:
    try:
        value_max = int(
            input("""How difficult would you like this to be? Pick a max integer: """)
        )
    except ValueError:
        print("The given value must be an integer.")
    else:
        if value_max <= 1:
            print("The number must be an integer greater than 1.")
        else:
            break
# Generate a random number between 1 and the chosen value.
value_random = random.randint(1, value_max)

# Give the user instructions as to what he or she will be doing.
print(f"Guess a number between 1 and {value_max}")
# Initialize the sentinal and the array of guesses.
guesses = []
# Play the guessing game.
while True:
    # Prompt the user for a number.
    current_guess = int(input("> "))
    # Store the number in an array so it can be displayed later.
    guesses.append(current_guess)
    # Make a decision: was the guess too high, too low, or just right.
    if current_guess > value_random:
        print("\tToo high!")
    elif current_guess < value_random:
        print("\tToo low!")
    else:
        break

# Give the user a report: How many guesses and what the guesses where.
print(f"You were able to find the number in {len(guesses)} guesses.")
print(f"The numbers you guessed were: {guesses}")
