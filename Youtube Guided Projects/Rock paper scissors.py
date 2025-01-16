name = input("What is your name? ")


def rock_paper_scissors():
    import random
    player_score = 0
    computer_score = 0
    print("Rock, Paper, Scissors, shoot")
    while True:
        computer_action = random.choice(["rock", "paper", "scissors"])
        player_action = input("What do you play? R/P/S \n").lower()
        if player_action == "rock" or player_action == "r":
            if computer_action == "rock":
                print("It's a draw")
            elif computer_action == "paper":
                print("Computer wins")
                computer_score += 1
            elif computer_action == "scissors":
                print(f"{name} wins")
                player_score += 1

        elif player_action == "paper" or player_action == "p":
            if computer_action == "rock":
                print(f"{name} wins")
                player_score += 1
            elif computer_action == "paper":
                print("It's a draw")
            elif computer_action == "scissors":
                print("Computer wins")
                computer_score += 1

        elif player_action == "scissors" or player_action == "s":
            if computer_action == "rock":
                print("Computer wins")
                computer_score += 1
            elif computer_action == "paper":
                print(f"{name} wins")
                player_score += 1
            elif computer_action == "scissors":
                print("It's a draw")
        else:
            print("Please choose rock, paper, or scissors")
            continue
        break
    print(player_score)
    print(computer_score)


def rock_paper_scissors_replay():
    replay = input("Wanna play again?\n").capitalize()
    if replay == "Yes":
        while True:
            rock_paper_scissors()
            if input("Press 'enter' to continue or 'exit' to quit\n") == "exit":
                print("Thanks for playing!")
                break
            else:
                continue
    elif replay == "No" or replay == "N":
        print("Thanks for playing!")


rock_paper_scissors()
rock_paper_scissors_replay()


