# RockPaperScissors main code 1.0.1

import getpass

def rockPaperScissors(USER_NAME1, USER_NAME2):
    txt = True
    
    while txt:
        
        POINTS_USER1 = 0
        POINTS_USER2 = 0
        
        r = ['rock', 'roc', 'rok', 'rck', 'ro', 'rc', 'rk', 'r']
        p = ['paper', 'pape', 'aper', 'pper', 'p']
        s = ['scissors', 'scissor', 'sissors', 'scssors', 'scis', 'sci', 's']
        
        while POINTS_USER1 <= 10 and POINTS_USER2 <= 10:
            USER1 = getpass.getpass("Rock, paper or scissors ? ", None)
            USER2 = getpass.getpass("Rock, paper or scissors ? ", None)
    
            if USER1.lower() in r:
                if USER2.lower() in p:
                    print(USER_NAME2, " won !", "\nCongratulation !")
                    POINTS_USER2 += 1
                if USER2.lower() in s:
                    print(USER_NAME1, " won !", "\nCongratulation !")
                    POINTS_USER1 += 1
            if USER1 in p:
                if USER2 in [rock, r]:
                    print(USER_NAME1, " won !", "\nCongratulation !")
                    POINTS_USER1 += 1
                if USER2 in [scissors, s]:
                    print(USER_NAME2, " won !", "\nCongratulation !")
                    POINTS_USER2 += 1
            if USER1 in [scissors, s]:
                if USER2 in [rock, r]:
                    print(USER_NAME2, " won !", "\nCongratulation !")
                    POINTS_USER2 += 1
                if USER2 in [paper, p]:
                    print(USER_NAME1, " won !", "\nCongratulation !")
                    POINTS_USER1 += 1
            elif USER1 == USER2:
                print("Draw")
            else:
                print("Error... Try again")

            print(USER_NAME1, ": ", POINTS_USER1, " vs ", USER_NAME2, ": ", POINTS_USER2)
            
        print('G A M E  O V E R')
        
        if POINTS_USER1 == 10:
            print(USER_NAME1, ' won the game !')
        elif POINTS_USER2 == 10:
            print(USER_NAME2, ' won the game !')
            
        txt2 = input('Would you like to play again ?[Y/n]')
        
        if txt2 in ["Y", "y", "Yes", "yes"]:
            print("Run the code...")
            txt = True
        elif txt2 in ["N", "n", "No", "no"]:
            print("OK")
            txt = False
            
                     
t1 = input("What's your name ?")
t2 = input("What's your name ?")
piatraHartieFoarfeca(t1, t2)
