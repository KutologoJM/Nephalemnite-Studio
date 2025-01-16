# List of 10 questions for the quiz game

list_of_questions = ["What planet is closest to the Sun? a) Mercury b) Venus c) Earth d) Mars",
                     "What is the largest planet in our solar system? a) Earth b) Mars c) Jupiter d) Saturn",
                     "Which planet is also known as the 'Red Planet' a) Jupiter b) Saturn c) Mars d) Uranus",
                     "What is the hottest planet in our solar system? a) Venus b) Mercury c) Mars d) Jupiter",
                     "Which planet has rings around it? a) Mars b) Jupiter c) Saturn d) Uranus",
                     "What is the smallest planet in our solar system? a) Venus b) Earth c) Mercury d) Mars",
                     "Which planet is often referred to as earth's sister a) Mercury b) Venus c) Mars d) Jupiter",
                     "Which planet is known for its Great Red Spot? a) Jupiter b) Saturn c) Neptune d) Uranus",
                     "What is the second planet from the sun? a) Mars b) Venus c) Earth d) Mercury",
                     "What planet is no longer considered a planet? a) Jupiter b) Uranus c) Saturn d) Neptune"]
# Corresponding answers to each of the above questions
list_of_correct_answers = \
                  ["a) Mercury",
                   "c) Jupiter",
                   "c) Mars",
                   "a) Venus",
                   "c) Saturn",
                   "c) Mercury",
                   "b) Venus",
                   "a) Jupiter",
                   "b) Venus",
                   "d) Pluto"
                   ]


print("Python Quiz Game")
# welcomes player using their name in the format John
name = input("What is your name? \n").capitalize()
print(f"Welcome to the game {name}. Enjoy!")

ready_state = False  # determines whether player is ready to play
score = 0  # the player's in game score
x = 0  # placeholder variable used for while loop in line 49

# continually waits for player to state that they are ready then begins the game if true
while ready_state is not True:
    ready_state = input("Are you ready to play? Y/N \n").lower()
    if ready_state == "yes" or ready_state == "y":
        game_is_running = True
        break
    elif ready_state == "no" or ready_state == "n":
        game_is_running = False
    else:
        print("Please enter either 'yes' or 'no'")
        continue

# while loop used to cycle through questions and answers
# contains error handling for potential issues such as invalid answers
while x < 10:
    answer = input(f"Question-{x+1} {list_of_questions[x]}\nAnswer: ").lower()
    if answer in ["a", "b", "c", "d"]:
        if answer == list_of_correct_answers[x][0]:   # from list_of_correct_answers to a,b,c or d e.g "a) Mercury to a"
            print("Correct!")
            score += 1

        else:
            print("Wrong!")
        x += 1
    else:
        print("Please enter either 'a, b, c or d'")
        continue
print(f"Thank you for playing. Your final score is {score}/10.")
