#!/usr/bin/python3.8

def rockPaperScissors(NAME_USER1, NAME_USER2):
    txt = True
    
    while txt == True:
        import getpass
        U1 = 0
        U2 = 0
    
        while U1 <= 10 and U2 <= 10:
            USER1 = getpass.getpass("Rock, paper or scissors ? ", None)
            USER2 = getpass.getpass("Rock, paper or scissors ? ", None)
    
            if USER1 in [rock, r]:
                if USER2 in [paper, p]:
                    print(NAME_USER2, " won !", "\nCongratulation !")
                    U2 += 1
                if USER2 in [scissors, s]:
                    print(NAME_USER1, " won !", "\nCongratulation !")
                    U1 += 1
            if USER1 in [paper, p]:
                if USER2 in [rock, r]:
                    print(NAME_USER1, " won !", "\nCongratulation !")
                    U1 += 1
                if USER2 in [scissors, s]:
                    print(NAME_USER2, " won !", "\nCongratulation !")
                    U2 += 1
            if USER1 in [scissors, s]:
                if USER2 in [rock, r]:
                    print(NAME_USER2, " won !", "\nCongratulation !")
                    U2 += 1
                if USER2 in [paper, p]:
                    print(NAME_USER1, " won !", "\nCongratulation !")
                    U1 += 1
            elif USER1 == USER2:
                print("Draw")
            else:
                print("Error... Try again")

            print(NAME_USER1, ": ", U1, " vs ", NAME_USER2, ": ", U2)
            
        print('G A M E  O V E R')
        
        if U1 == 10:
            print(NUME_USER1, ' won the game !')
        elif U2 == 10:
            print(NUME_USER2, ' won the game !')
            
        txt2 = input('Would you like to play again ?[Y/n])
        
        if txt2 in ["Y", "y", "Yes", "yes"]:
            print("Run the code...")
            txt = True
        elif txt2 in ["N", "n", "No", "no"]:
            print("OK")
            txt = False
            
                     
t1 = input("What's your name ?")
t2 = input("What's your name ?")
piatraHartieFoarfeca(t1, t2)
