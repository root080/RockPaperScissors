# Created by AlexC

import sys
import getpass

def signUp():
    lastName = input("Last Name: ")
    surname = input("Surname: ")
    age = input("Age: ")
    email = input("Email Adress: ")
    city = input("City: ")
    street = input("Street: ")
    postalCode = input("Postal Code: ")

    name = lastName + surname
    adress = city + street + postalCode

    null = "unknown"

    userAccountData = {'Nume': name, 'Password': '', 'E-mail': email}
    userPersonalData = [name, age, adress, email]

    existingUserData = ['Alex C', '30', null, 'contact@alexc.com']

    for i in [userAccountData.values(), userPersonalData]:
        if i == "":
            i = null
            if i == null:
                while lastName == null:
                    print("Last Name required")
                    lastName = input("Last Name: ")
                while surname == null:
                    print("Surname required")
                    surname = input("Surname: ")
                while email == null:
                    print("E-mail required")
                    email = input("Email Adress: ")
                while city == null:
                    print("City required")
                    city = input("City: ")

    USER_INPUT = input("Your name is " + name + " and you have " + age + " years old" + ". You live in " + city + "(" + postalCode + ")" ", " + street + " street ?[Y/n] ")
    if USER_INPUT in ["Yes", "yes", "ye", "Y", "y"]:
        if userPersonalData == existingUserData:
            print("This account already exist")
            sys.exit()
        else:
            print("Hi, " + lastName + " everything is right, so you can continue.")
            USER2_INPUT = input("Would you like to continue ?[Y/n] ")
            if USER2_INPUT in ["Yes", "yes", "ye", "Y", "y"]:
                email_preview = input("We send a security code to " + email + ". Would you like to preview it ?[Y/n] ")
                securityCode = "95867"
                if email_preview in ["Yes", "yes", "ye", "Y", "y"]:
                    print("Thanks again for downloading RockPaperScissors feature. Your security code is " + securityCode + "\nSincerely, \nAndrew F \nAlexC")
                nrIncercari = 0
                while nrIncercari < 5:
                    CODE_INPUT = input("Type the security code: ")
                    if CODE_INPUT == securityCode:
                        print("OK, you can pass to the next step")
                        while True:
                            PASSWORD_INPUT = getpass.getpass("Type your password: ")
                            PASSWORD_VERIFICATION = getpass.getpass("Retype your password: ")
                            if PASSWORD_INPUT == PASSWORD_VERIFICATION:
                                print("Signup process finished")
                                print("from: contact@alexc.com \nto: " + email)
                                print("Hi, " + name)
                                print("Congratulation, you've created your RockPaperScissors account. Now you're ready to play. But, before this, I want to tell you more "
                                      "about this project. RockPaperScissors was a simple project idea, inital created on my computer for learning Python programing. "
                                      "But everything changed after I decided to create a repository on GitHub with this idea. I've created two branches: main, where I "
                                      "upload my initial code and feature, that I recommend you to install(if you don't have MacOS), a branch with a better version of game "
                                      "code and a bite of shell, to automate the process. The update of the feature version, where initially I put the same code as in the "
                                      "main branch, was possible with Andrew F help and I thank him for the contribution \nAlexC, owner of RockPaperScissors project")
                                break
                            else:
                                print("There is not the same password. Retype it !")
                        break
                    elif nrIncercari == 3:
                        print("One more try")
                    elif nrIncercari == 4:
                        print("Your security code is incorect.")
                        print("End proram...")
                        sys.exit()
                    else:
                        print("Incorect security code. Retype it")
                        nrIncercari += 1

    elif USER_INPUT in ["No", "no", "N", "n"]:
        print("OK, introduce-ti din nou datele si asigura-te ca sunt scrise corect")
        signUp()
    else:
        print("Error...")
        

from SignUp import email
from SignUp import password
        
USER_INPUT = input("Have you already an accont ?[Y/n] ")

if USER_INPUT in ["Yes", "yes", "ye", "Y", "y"]:
    repond = True
    while repond:
        EMAIL_INPUT = input("E-mail Adress: ")
            if EMAIL_INPUT == name:
            PASSWORD_INPUT = getpass.getpass("Password: ")
                if PASSWORD_INPUT == password:
                print("Loged In")
                break
            else:
                print("Incorrect password. Try again...")
            else:
                print("This username does not exist")
elif USER_INPUT in ["No", "no", "N", "n"]:
    SignUp()
else:
    print("Erorr...")

