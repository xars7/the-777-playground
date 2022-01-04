# PasswordSafe v1.0.0 by Kevin Flynn (xars7)
# 
#   Description - This program will create a folder that it stores your passwords in. Each password get's it's own designated .txt file. Along with another file containing
#                 your master password. Now I know what your thinking "Kevin my passwords wouldn't really be safe if they were just in a text file waiting for someone to read
#                 them" and you are absolutely right. That's why we are going to encrypt them before we send them to their designated txt file. The only way you'll be able 
#                 to access your passwords is if you enter in the correct master password and login.
#
#                 TODO:
#                       Step 1. Ask a user to create a login or login in to their safe
#                       Step 2. IF: the user has decided to create an account, create a file with their login and password for later logins
#                               IF: the user has decided to login, read the file that corresponds with their username and see if they have entered the right passsword, if so
#                                   let them into their safe
#                       Step 3. Ask the user if they would like to see their passwords or create a new one                               
#                       Step 4. IF: the user want's to create a password go into the createPassword function
#                               IF: the user asks to see their passwords show them their passwords
#                       Exit the program whenever user types exit/Exit
#
#
#
#
#

import os
from cryptography.fernet import Fernet


print("PasswordSafe v1.0.0 by Kevin Flynn(xars7)")

key = Fernet.generate_key()

f = Fernet(key)

# Create a login with a username and master password
def createALogin(usernameCreate, masterPasswordCreate):

    # encrypt the usernameCreate and masterPasswordCreate
    encryptedUser = f.encrypt(b"{usernameCreate}")
    encryptedMassPass = f.encrypt(b"{masterPasswordCreate}")

    with open("PasswordSafe/MasterLogin.txt", "wb") as login:
        login.write(encryptedUser + "\n".encode('ascii') + encryptedMassPass) 




# login to the password safe using the inputed master password and username
#def loginToSafe():




# Ask a user to create a login or login to their safe
mainMenuChoice = input("1. Create a login 2. Login to a safe : ")

if mainMenuChoice == "1":
    username = input("Please enter in a username you would like to use : ")
    masterPassword = input("Please enter the master password you would like to use : ")
    createALogin(username, masterPassword)
elif mainMenuChoice == "2":
    loginToSafe()
else:
    print("That's not an option")