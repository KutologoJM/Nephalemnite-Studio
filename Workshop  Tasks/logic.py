import random

"""
A guessing game made in python. 
While setting up the game a logic error was made possible that allowed the game to break its own rules -
 "number between 1 and 20".

"""

num = random.randint(1, 21)
attempts = 0

print("I'm thinking of a number between 1 and 20.")
guess = ""
while guess != num:
    print("Take a guess.")
    guess = int(input())
    attempts += 1
    if attempts > 5:
        break
    elif guess < num:
        print("Your guess is too low.")
    elif guess > num:
        print("Your guess is too high.")
    elif guess == num:
        break

if attempts < 6:
    print(f"Good job! You guessed my number in {attempts} guesses!")
else:
    print(f"Nope the number I was thinking of was {num}.")
