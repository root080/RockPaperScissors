# signUp.py Copyright (C) 2021 Alex C

import sys
import getpass

def signUp():
    firstName = input("First Name: ")
    lastName = input("Last Name: ")
    age = input("Age: ")
    email = input("Email Address: ")
    city = input("City: ")
    street = input("Street: ")
    postalCode = input("Postal Code: ")

    global name
    global email
    name = firstName + lastName
    address = city + street + postalCode

    null = "unknown"

    userAccountData = {'Name': name, 'Password': '', 'E-mail': email}
    userPersonalData = [name, age, address, email]

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
                    email = input("Email Address: ")
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
                                password = PASSWORD_INPUT
                                global password
                                print("Signup process finished")
                                print("from: contact@alexc.com \nto: " + email)
                                print("Hi, " + name)
                                print("Congratulation, you've created your RockPaperScissors account. Now you're "
                                      "ready to play. But, before that, I want to tell you more about the project. "
                                      "RockPaperScissors was initially a simple project idea, for learning Python "
                                      "programing. But everything changed after I decided to create a repository on "
                                      "GitHub with this idea. I've created two branches: main, where I upload my "
                                      "initial code and feature, that I recommend you to use, and a branch with a "
                                      "better version of game code and a bit of shell, to automate the process. The "
                                      "update of the feature version, where initially I put the same code as in the "
                                      "main branch, was possible with thefirethirteen's help and I thank them for the "
                                      "contribution \nAlex C, owner of the RockPaperScissors project")
                                break
                            else:
                                print("There is not the same password. Retype it !")
                        break
                    elif nrIncercari == 3:
                        print("One more try")
                    elif nrIncercari == 4:
                        print("The security code is incorect.")
                        print("End program...")
                        sys.exit()
                    else:
                        print("Incorrect security code. Please try again")
                        nrIncercari += 1

    elif USER_INPUT in ["No", "no", "N", "n"]:
        print("OK, introduce-ti din nou datele si asigura-te ca sunt scrise corect")
        signUp()
    else:
        print("Error...")


USER_INPUT = input("Do you already have an account? [y/n] ")

if USER_INPUT in ["Yes", "yes", "ye", "Y", "y"]:
    while True:
        EMAIL_INPUT = input("E-mail Address: ")
        if EMAIL_INPUT == name:
            PASSWORD_INPUT = getpass.getpass("Password: ")
            if PASSWORD_INPUT == password:
                print("Logged In")
                break
            else:
                print("Incorrect password. Try again...")
        else:
            print("This username does not exist")
elif USER_INPUT in ["No", "no", "N", "n"]:
    signUp()
else:
    print("Error...")
