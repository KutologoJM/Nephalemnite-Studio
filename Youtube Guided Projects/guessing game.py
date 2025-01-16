def guessing_game():
    import random
    print("The default range is between 1 and 10")
    decision = input("Press 'enter' for default or any other key for custom range: ").capitalize()
    if decision == "":
        generated_number = random.randint(1, 10)
        print("I am thinking of a number between 1 and 10.")
    else:
        print("What would you like the range to be?")
        x = int(input("From __"))
        y = int(input("To __"))
        print(f"I am thinking of a number between {x} and {y}.")
        generated_number = random.randint(x, y)
    attempts = 0
    while attempts < 5:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            print("Incorrect input. Please enter a valid number.")
            continue
        if guess != generated_number:
            if attempts < 4:
                attempts += 1
                print("Incorrect, please try again.")
            else:
                print("Sorry you failed to guess the right answer.")
                print(f"The answer was {generated_number}.")
                attempts += 1
        else:
            attempts += 1
            print(f"Congratulations! You guessed the right answer in {attempts} attempts.")
            print(f"The answer was {generated_number}.")
            break


print("Welcome to my guessing game!")
print("Press 'Enter' to continue.")
if input() == "":
    guessing_game()
while True:
    start_game = input("Would you like to play again? Y/N\n").capitalize()
    if start_game == "Yes" or start_game == "Y":
        print("\n")
        guessing_game()
    elif start_game == "No" or start_game == "N":
        print("Okay, I will see you next time.")
        break
    else:
        "Please enter yes or no."
        continue
