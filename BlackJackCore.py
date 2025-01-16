from blackjack_logic import casino_welcome
from blackjack_logic import draw
from blackjack_logic import dealer_draw

num_players, player_information = casino_welcome()

while True:
    end_game = False
    player_turn = True
    card_value = None
    list_of_cards = []
    player_surrendered = False
    player_went_bust = False
    for i in range(num_players):
        list_of_cards.append({})
    bet = None
    total_card_value = 0

    card_index = None  # which or how many cards are currently being played
    current_player_index = None  # who is currently playing

    while player_turn:
        for i in range(num_players):
            total_card_value = 0
            card_index = 0
            current_player_index = i

            name, balance, chips, _ = player_information[i].values()
            # ---------------------bet() --------------------------#
            print(f"\033[30;44m\033[1m\033[3m\033[4m\033[10m{name}'s turn Begins\033[0m")

            while True:
                try:
                    print(f"You have {chips} chips")
                    if chips <= 0:
                        while True:
                            print(f"Your balance is {balance}")
                            chips = int(input("How many chips would you like to purchase.\n Convert: "))
                            if chips > balance:
                                print("Insufficient funds")
                                continue
                            else:
                                break

                    bet = int(input(f"How much would you like to bet {name}?\nBet: "))
                except ValueError:
                    print("Invalid option, please enter a valid amount.")
                    continue
                if bet > chips:
                    print("Insufficient funds")
                    continue
                elif bet < 2:
                    print("There is a minimum bet of 2 required.")
                    continue
                elif bet > 500:
                    print("Maximum bet is equal to 500")
                    continue
                else:
                    chips -= bet
                    break
            print("___________________________________________________________________________")
            print("You are automatically dealt two cards.")
            for x in range(2):
                card_index += 1
                card_value, cardInfo = draw()
                total_card_value += card_value
                list_of_cards[current_player_index].update({f"Card {card_index}": cardInfo})
            while True:
                print("___________________________________________________________________________")
                print(f"Chips: {chips}, Current Bet: {bet}, Total card value: {total_card_value}")
                print("___________________________________________________________________________")

                action = input("\nHit, Stand, DoubleDown, Surrender?\nAction: ").capitalize()

                if action == "Hit":
                    card_index += 1
                    card_value, cardInfo = draw()
                    total_card_value += card_value
                    list_of_cards[current_player_index].update({f"Card {card_index}": cardInfo})
                    if total_card_value > 21:
                        print(f"{name} went bust")
                        bet = 0
                        break
                    else:
                        continue
                elif action == "Stand":
                    print(f"{name} chose to Stand")
                    break

                elif action == "Double":  # and special parameters are met
                    if chips - bet < 0:
                        print("Insufficient funds")
                        continue
                    elif not (chips - bet < 0):
                        chips -= bet
                        bet += bet
                        card_index += 1
                        card_value, cardInfo = draw()
                        total_card_value += card_value
                        list_of_cards[current_player_index].update({f"Card {card_index}": cardInfo})
                        if total_card_value > 21:
                            print(f"{name} went bust")
                            bet = 0
                            break
                        else:
                            continue
                elif action == "Surrender":
                    bet *= 0.5
                    chips += bet
                    print(f"{name} has surrendered.")
                    """update surrender code"""
                    player_surrendered = False
                    break
                else:
                    print("Option not available")
                    continue

            list_of_cards[current_player_index].update({f"Player {current_player_index}": total_card_value})
            player_information[current_player_index].update({'Balance': balance, 'Chips': chips, "Pending_Bet": bet})
            # ---------------------updates balance in player_information-----------#
            print("\n___________________________________________________________________________")
            print(f"{name}'s Chips: {chips}, {name}'s Current Bet: {bet}, Final card value: {total_card_value}")
            print("___________________________________________________________________________\n")
        break

    # ---------------------Dealer.exe---------------------------

    dealer_cards = {}
    dealer_total_card_value = 0
    dealer_stands = False
    dealer_went_bust = False
    dealer_will_bust = False
    card_index = 0
    print(f"\033[7;37;44mDealer's turn begins\033[0m")
    while not dealer_stands or not dealer_went_bust:
        card_index += 1
        card_value, cardInfo = dealer_draw(dealer_will_bust)
        if card_value > 10:
            dealer_will_bust = True
        dealer_total_card_value += card_value
        dealer_cards.update({f"Card {card_index}": cardInfo})
        if dealer_total_card_value > 21:
            print(f"\nDealer went bust")
            print(f"Dealer's Final Card Value: {dealer_total_card_value}")
            dealer_went_bust = True
            break
        elif dealer_total_card_value >= 17:
            dealer_stands = True
            print("\nDealer chose to stand")
            print(f"Dealer's Final Card Value: {dealer_total_card_value}")
            break
        else:
            continue

    # --------------------Money matters
    if dealer_went_bust:
        for i in range(num_players):
            current_player_index = i
            total_card_value = list_of_cards[i].get(f"Player {i}")
            _, _, chips, bet = player_information[i].values()
            chips += (bet * 2)
            bet = 0
            player_information[current_player_index].update({'Chips': chips, "Pending_Bet": bet})
    elif dealer_stands:
        for i in range(num_players):
            current_player_index = i
            total_card_value = list_of_cards[i].get(f"Player {i}")
            _, _, chips, bet = player_information[i].values()
            if dealer_total_card_value > total_card_value:
                bet = 0
                player_information[current_player_index].update({'Chips': chips, "Pending_Bet": bet})
            elif dealer_total_card_value < total_card_value:
                chips += (bet * 2)
                bet = 0
                player_information[current_player_index].update({'Chips': chips, "Pending_Bet": bet})
            elif dealer_total_card_value == total_card_value:
                chips += bet
                bet = 0

    print(f"\033[30;44m\033[1m\033[3m\033[4m\033[10m'Game Stats'\033[0m")

    i = 0
    while i < num_players:
        name, balance, chips, _ = player_information[i].values()
        print(f"Name: {name}\n"
              f"Balance: {balance}\n"
              f"Chips: {chips}\n")
        if balance <= 1 and chips < 1:
            print(f"Player {name} cannot continue. Better luck next time.")
            print("___________________________________________________________________________\n")
            del player_information[i]
            num_players -= 1
        else:
            i += 1
        if i == len(player_information):
            break
    while True:
        continue_to_play = input("Would you like to continue?\n Y/N: ").lower()
        if continue_to_play == "yes" or continue_to_play == "y":
            end_game = False
            break
        elif continue_to_play == "no" or continue_to_play == "n":
            end_game = True
            break
        else:
            print("Invalid option. Please enter yes or no")
            continue
    if end_game:
        break
    elif not end_game:
        continue
print("Until next time. I hope you enjoyed your visit.")
