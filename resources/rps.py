# Modifications Copyright (C) 2021 Andrew F

import sys
import getpass

USER_INPUT = input("Player One, What's your name? ")
player_one_name = USER_INPUT.strip()
USER_INPUT = input("Player Two, What's your name? ")
player_two_name = USER_INPUT.strip()

while True:
    roundCounter = 0
    player_one_points = 0
    player_two_points = 0

    USER_INPUT = int(input("Would you like to play a certain number of rounds (1), or until a player gets a certain "
                           "number of points (2)? "))
    if USER_INPUT == 1:
        rounds_to_play = int(input("How many rounds would you like to play? "))
        max_points = rounds_to_play / 2
    elif USER_INPUT == 2:
        max_points = int(input("How many points does a player need to score in order to win? "))
        rounds_to_play = 2 * max_points
    else:
        print("Unrecoverable error! Exiting")
        sys.exit()

    while roundCounter <= (rounds_to_play - 1) and (player_one_points < max_points and player_two_points < max_points):
        player_one_choice = getpass.getpass(prompt=player_one_name + ", Rock, paper or scissors? ")
        player_two_choice = getpass.getpass(prompt=player_two_name + ", Rock, paper or scissors? ")

        if player_one_choice == player_two_choice:
            print("Draw!")
            roundCounter += 1
        elif player_one_choice in ["rock", "r"]:
            if player_two_choice in ["paper", "p"]:
                print(player_two_name + " won the round!" + "\nCongratulations!")
                roundCounter += 1
                player_two_points += 1
            if player_two_choice in ["scissors", "s"]:
                print(player_one_name + " won the round!" + "\nCongratulations!")
                roundCounter += 1
                player_one_points += 1
        elif player_one_choice in ["paper", "p"]:
            if player_two_choice in ["scissors", "s"]:
                print(player_two_name + " won the round!" + "\nCongratulations!")
                roundCounter += 1
                player_two_points += 1
            if player_two_choice in ["rock", "r"]:
                print(player_one_name + " won the round!" + "\nCongratulations!")
                roundCounter += 1
                player_one_points += 1
        elif player_one_choice in ["scissors", "s"]:
            if player_two_choice in ["rock", "r"]:
                print(player_two_name + " won the round!" + "\nCongratulations!")
                roundCounter += 1
                player_two_points += 1
            if player_two_choice in ["paper", "p"]:
                print(player_one_name + " won the round!" + "\nCongratulations!")
                roundCounter += 1
                player_one_points += 1
        else:
            print("Unrecoverable error! Exiting")
            sys.exit()

        print("Score:")
        print(player_one_name + ": " + str(player_one_points) + " vs " + player_two_name + ": "
              + str(player_two_points))

    print('G A M E  O V E R')

    if player_one_points > player_two_points:
        print(player_one_name + " won the game!")
    elif player_two_points > player_one_points:
        print(player_two_name + " won the game!")
    elif player_one_points == player_two_points:
        print("It's a tie!")

    USER_INPUT = input("Would you like to play again? [y/n] ")

    if USER_INPUT in ["Y", "y", "Yes", "yes"]:
        print("Let's play again then!")
    else:
        print("OK, Goodbye!")
        break
