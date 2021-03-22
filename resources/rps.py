# This is the main code of the game
# Copyright (C) 2021 Alex C

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

    USER_INPUT = int(input("Would you like to play a certain number of rounds (1), or until a player gets a "
                           "certain number of points (2)? "))
    if USER_INPUT == 1:
        rounds_to_play = int(input("How many rounds would you like to play? "))
        max_points = rounds_to_play / 2
    elif USER_INPUT == 2:
        max_points = int(input("How many points does a player need to score in order to win? "))
        rounds_to_play = 2 * max_points
    else:
        print("Unrecoverable error! Exiting")
        sys.exit()

    word_rock = ['rock', 'roc', 'rok', 'rck', 'ro', 'rc', 'rk', 'r']
    word_paper = ['paper', 'pape', 'aper', 'pper', 'p']
    word_scissors = ['scissors', 'scissor', 'sissors', 'scssors', 'scis', 'sci', 's']
        
    while roundCounter <= (rounds_to_play - 1) and (player_one_points < max_points and player_two_points < max_points):
        USER_INPUT = getpass.getpass(prompt=player_one_name + ", Rock, paper or scissors? ")
        USER_INPUT = USER_INPUT.strip()
        player_one_choice = USER_INPUT.lower()
        USER_INPUT = getpass.getpass(prompt=player_two_name + ", Rock, paper or scissors? ")
        USER_INPUT = USER_INPUT.strip()
        player_two_choice = USER_INPUT.lower()

        if player_one_choice == player_two_choice:
            print("Draw!")
            roundCounter += 1
        elif player_one_choice in word_rock:
            if player_two_choice in word_paper:
                print(player_two_name + " won the round!" + "\nCongratulations!")
                roundCounter += 1
                player_two_points += 1
            if player_two_choice in word_scissors:
                print(player_one_name + " won the round!" + "\nCongratulations!")
                roundCounter += 1
                player_one_points += 1
        elif player_one_choice in word_paper:
            if player_two_choice in word_scissors:
                print(player_two_name + " won the round!" + "\nCongratulations!")
                roundCounter += 1
                player_two_points += 1
            if player_two_choice in word_rock:
                print(player_one_name + " won the round!" + "\nCongratulations!")
                roundCounter += 1
                player_one_points += 1
        elif player_one_choice in word_scissors:
            if player_two_choice in word_rock:
                print(player_two_name + " won the round!" + "\nCongratulations!")
                roundCounter += 1
                player_two_points += 1
            if player_two_choice in word_paper:
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

    if USER_INPUT in "yes":
        print("Let's play again then!")
    else:
        print("OK, Goodbye!")
        break
