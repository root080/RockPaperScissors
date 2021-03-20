# Modifications Copyright (C) 2021 Andrew F

def rockPaperScissors(USER_NAME1, USER_NAME2):
    txt = True
    
    while txt:
        import getpass
        U1 = 0
        U2 = 0
    
        while U1 <= 10 and U2 <= 10:
            USER1 = getpass.getpass("Rock, paper or scissors ? ", None)
            USER2 = getpass.getpass("Rock, paper or scissors ? ", None)
    
            if USER1 in ["rock", "r"]:
                if USER2 in ["paper", "p"]:
                    print(USER_NAME2, " won!", "\nCongratulations!")
                    U2 += 1
                if USER2 in ["scissors", "s"]:
                    print(USER_NAME1, " won!", "\nCongratulations!")
                    U1 += 1
            if USER1 in ["paper", "p"]:
                if USER2 in ["rock", "r"]:
                    print(USER_NAME1, " won!", "\nCongratulations!")
                    U1 += 1
                if USER2 in ["scissors", "s"]:
                    print(USER_NAME2, " won!", "\nCongratulations!")
                    U2 += 1
            if USER1 in ["scissors", "s"]:
                if USER2 in ["rock", "r"]:
                    print(USER_NAME2, " won!", "\nCongratulations!")
                    U2 += 1
                if USER2 in ["paper", "p"]:
                    print(USER_NAME1, " won!", "\nCongratulations!")
                    U1 += 1
            elif USER1 == USER2:
                print("Draw")
            else:
                print("Error... Try again")

            print(USER_NAME1, ": ", U1, " vs ", USER_NAME2, ": ", U2)
            
        print('G A M E  O V E R')
        
        if U1 == 10:
            print(USER_NAME1, ' won the game !')
        elif U2 == 10:
            print(USER_NAME2, ' won the game !')
            
        txt2 = input("Would you like to play again? [y/n]")
        
        if txt2 in ["Y", "y", "Yes", "yes"]:
            print("Run the code...")
            txt = True
        elif txt2 in ["N", "n", "No", "no"]:
            print("OK")
            txt = False
            
                     
t1 = input("What's your name ? ")
t2 = input("What's your name ? ")
rockPaperScissors(t1, t2)
