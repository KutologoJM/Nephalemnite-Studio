import random


def casino_welcome():
    convert = 0
    player_names = []
    player_information = []

    print("NephalemNite Casino.")
    while True:
        try:
            num_players = int(input("How many will be playing today?\nAmount of players: "))
        except ValueError:
            print("Invalid input. Try again.\n")
            continue
        if num_players < 2:
            print("Minimum of 2 players required.\n")
            continue
        for i in range(num_players):
            if i < 1:
                while True:
                    name = input(f"\nWhat is your name Player {i + 1}? \nName: ")
                    if len(name) < 2:
                        print("\nName must be more than 2 characters")
                        continue
                    else:
                        print(f"Welcome {name}. Enjoy your stay.\n")
                        player_names.append(name)
                        break
            else:
                while True:
                    name = input(f"And what is your name Player {i + 1}? \nName: ")
                    if len(name) < 2:
                        print("\nName must be more than 2 characters")
                        continue
                    else:
                        print(f"Welcome {name}. Enjoy your stay.\n")
                        player_names.append(name)
                        break

        for x in range(num_players):
            balance = 5000
            print(f"{player_names[x]} you have ${balance} in your account.")
            while True:
                try:
                    convert = int(input(f"Amount to convert to chips: "))
                    if convert > balance:
                        print("Insufficient funds")
                        continue
                    elif convert < 1:
                        print("Please enter a positive number")
                        continue
                except ValueError:
                    print("Invalid option chosen, please try again.\n")
                    continue
                print(f"Okay {player_names[x]}, you now have {convert} chips.\n")
                break
            balance -= convert
            num_casino_chips = 0
            num_casino_chips += convert
            player_information.append(
                {"Name": player_names[x], "Balance": balance, "Chips": num_casino_chips, "Pending_Bet": 0}
            )
        return num_players, player_information


def calculations(suit):
    cv = random.randint(0, 12)
    possible_card_value = ['Ace', "2", "3", "4", "5", "6", "7", "8", "9", "10", "King", "Queen", "Jack"]
    if cv == 0:
        while True:
            try:
                ace_value = int(input("Ace: 1/11? \n"))
                if ace_value == 1 or ace_value == 11:
                    print(f"You drew the {possible_card_value[0]} of {suit}")
                    card_value = f"{possible_card_value[0]} of {suit}"
                    return ace_value, card_value
                else:
                    while ace_value != 1 or ace_value != 11:
                        ace_value = int(input("Try again. \n"))
                        if ace_value == 1 or ace_value == 11:
                            break
                    print(f"You drew the {possible_card_value[0]} of {suit}")
                    card_value = f"{possible_card_value[0]} of {suit}"
                    return ace_value, card_value
            except ValueError:
                print("Please enter a valid number. 1 or 11!")
                continue
    else:
        print(f"You drew the {possible_card_value[cv]} of {suit}")
        card_value = f"{possible_card_value[cv]} of {suit}"
        return possible_card_value[cv], card_value


def draw():
    suit_number = random.randint(1, 4)
    if suit_number == 1:
        card_suit = "Clubs"
        absolute_value, card_info = calculations(card_suit)
        if absolute_value == "King" or absolute_value == "Jack" or absolute_value == "Queen":
            absolute_value = 10
        return int(absolute_value), card_info

    elif suit_number == 2:
        card_suit = "Diamonds"
        absolute_value, card_info = calculations(card_suit)
        if absolute_value == "King" or absolute_value == "Jack" or absolute_value == "Queen":
            absolute_value = 10
        return int(absolute_value), card_info

    elif suit_number == 3:
        card_suit = "Hearts"
        absolute_value, card_info = calculations(card_suit)
        if absolute_value == "King" or absolute_value == "Jack" or absolute_value == "Queen":
            absolute_value = 10
        return int(absolute_value), card_info

    elif suit_number == 4:
        card_suit = "Spades"
        absolute_value, card_info = calculations(card_suit)
        if absolute_value == "King" or absolute_value == "Jack" or absolute_value == "Queen":
            absolute_value = 10
        return int(absolute_value), card_info


def dealer_calculations(suit, dealer_will_bust):
    cv = random.randint(0, 12)
    possible_card_value = ['Ace', "2", "3", "4", "5", "6", "7", "8", "9", "10", "King", "Queen", "Jack"]
    if cv == 0:
        if dealer_will_bust:
            ace_value = 1
        else:
            ace_value = 11
        if ace_value == 1 or ace_value == 11:
            print(f"Dealer drew the {possible_card_value[0]} of {suit}")
            card_value = f"{possible_card_value[0]} of {suit}"
            return ace_value, card_value
    else:
        print(f"Dealer drew the {possible_card_value[cv]} of {suit}")
        card_value = f"{possible_card_value[cv]} of {suit}"
        return possible_card_value[cv], card_value


def dealer_draw(will_lead_to_bust):
    suit_number = random.randint(1, 4)
    if suit_number == 1:
        card_suit = "Clubs"
        absolute_value, card_info = dealer_calculations(card_suit, will_lead_to_bust)
        if absolute_value == "King" or absolute_value == "Jack" or absolute_value == "Queen":
            absolute_value = 10
        return int(absolute_value), card_info

    elif suit_number == 2:
        card_suit = "Diamonds"
        absolute_value, card_info = dealer_calculations(card_suit, will_lead_to_bust)
        if absolute_value == "King" or absolute_value == "Jack" or absolute_value == "Queen":
            absolute_value = 10
        return int(absolute_value), card_info

    elif suit_number == 3:
        card_suit = "Hearts"
        absolute_value, card_info = dealer_calculations(card_suit, will_lead_to_bust)
        if absolute_value == "King" or absolute_value == "Jack" or absolute_value == "Queen":
            absolute_value = 10
        return int(absolute_value), card_info

    elif suit_number == 4:
        card_suit = "Spades"
        absolute_value, card_info = dealer_calculations(card_suit, will_lead_to_bust)
        if absolute_value == "King" or absolute_value == "Jack" or absolute_value == "Queen":
            absolute_value = 10
        return int(absolute_value), card_info
