# Modifications Copyright (C) 2021 Andrew F

def rockPaperScissors(USER_NAME1, USER_NAME2):
    txt = True
    
    while txt:
        import getpass
        roundCounter = 0
        user_one_wins = 0
        user_two_wins = 0
    
        while roundCounter <= 10:
            USER1 = getpass.getpass("Rock, paper or scissors? ", None)
            USER2 = getpass.getpass("Rock, paper or scissors? ", None)
    
            if USER1 in ["rock", "r"]:
                if USER2 in ["paper", "p"]:
                    print(USER_NAME2, " won!", "\nCongratulations!")
                    roundCounter += 1
                    user_two_wins += 1
                if USER2 in ["scissors", "s"]:
                    print(USER_NAME1, " won!", "\nCongratulations!")
                    roundCounter += 1
                    user_one_wins += 1
            elif USER1 in ["paper", "p"]:
                if USER2 in ["rock", "r"]:
                    print(USER_NAME1, " won!", "\nCongratulations!")
                    roundCounter += 1
                    user_one_wins += 1
                if USER2 in ["scissors", "s"]:
                    print(USER_NAME2, " won!", "\nCongratulations!")
                    roundCounter += 1
                    user_two_wins += 1
            elif USER1 in ["scissors", "s"]:
                if USER2 in ["rock", "r"]:
                    print(USER_NAME2, " won!", "\nCongratulations!")
                    roundCounter += 1
                    user_two_wins += 1
                if USER2 in ["paper", "p"]:
                    print(USER_NAME1, " won!", "\nCongratulations!")
                    roundCounter += 1
                    user_one_wins += 1
            elif USER1 == USER2:
                print("Draw")
            else:
                print("Error... Try again")

            print(USER_NAME1, ": ", user_one_wins, " vs ", USER_NAME2, ": ", user_two_wins)
            
        print('G A M E  O V E R')
        
        if user_one_wins > user_two_wins:
            print(USER_NAME1, " won the game !")
        elif user_two_wins > user_one_wins:
            print(USER_NAME2, " won the game !")
        elif user_one_wins == user_two_wins:
            print("It's a tie!")
            
        txt2 = input("Would you like to play again? [y/n]")
        
        if txt2 in ["Y", "y", "Yes", "yes"]:
            print("Run the code...")
            txt = True
        elif txt2 in ["N", "n", "No", "no"]:
            print("OK")
            txt = False
            
                     
t1 = input("What's your name? ")
t2 = input("What's your name? ")
rockPaperScissors(t1, t2)
