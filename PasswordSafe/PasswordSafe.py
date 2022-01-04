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

# we want our users to be able to write down their passwords or view them
#def accessVault():



# Create a login with a username and master password
def createALogin(usernameCreate, masterPasswordCreate):
    # generate an encryption key 
    key = Fernet.generate_key()
    f = Fernet(key)
    # write that encryption key to a key file for safe keeping
    with open("PasswordSafe/EncryptionKey.key", "wb") as fernetKey:
        fernetKey.write(key)

    # encode the username and master password before encryption
    encodedUserCred = usernameCreate.encode("utf-8")
    encodedPassCred = masterPasswordCreate.encode("utf-8")
    # encrypt the usernameCreate and masterPasswordCreate
    encryptedUser = f.encrypt(encodedUserCred)
    encryptedMassPass = f.encrypt(encodedPassCred)
    # write the encrypted login to a login file
    with open("PasswordSafe/Login.txt", "wb") as login:
        login.write(encryptedUser) 
    # write the encrypted MasterPassword to a MasterPassword File
    with open("PasswordSafe/MasterPassword.txt", "wb") as masterPass:
        masterPass.write(encryptedMassPass)




# login to the password safe using the inputed master password and username
def loginToSafe(usernameLogin, masterPasswordLogin):
    print("We got to the login function")
    # read the encryption key
    with open("PasswordSafe/EncryptionKey.key", "rb") as fernetKey:
        key = fernetKey.read()
        print("We read the key")
    # read the encrypted login to a login file
    with open("PasswordSafe/Login.txt", "rb") as login:
        usernameCheck = login.read()
        print("We read the login") 
    # read the encrypted MasterPassword to a MasterPassword File
    with open("PasswordSafe/MasterPassword.txt", "rb") as masterPass:
        masterPassCheck = masterPass.read()
        print("We read the password") 
    
    # create a Fernet object using the key we found earlier
    f = Fernet(key)

    # decrypt the usernameCheck and masterPasscheck
    decryptedUserCred = f.decrypt(usernameCheck)
    decryptedPassCred = f.decrypt(masterPassCheck)

    # decodes the decrypted passwords to verify them with the user input
    decodedUserCred = decryptedUserCred.decode()
    decodedPassCred = decryptedPassCred.decode()

    # if the credentials add up the program should say it works
    if decodedUserCred == usernameLogin and decodedPassCred == masterPasswordLogin:
        print("It works!")
        #accessVault()
    else:
        print("wrong login credentials")


# Ask a user to create a login or login to their safe
mainMenuChoice = input("1. Create a login 2. Login to a safe : ")

# If the user chooses one create a login page
if mainMenuChoice == "1":
    username = input("Please enter in a username you would like to use : ")
    masterPassword = input("Please enter the master password you would like to use : ")
    createALogin(username, masterPassword)
# If the user chooses two login to the password safe
elif mainMenuChoice == "2":
    username2 = input("Please enter your username : ")
    masterPassword2 = input("Please enter the master password : ")
    loginToSafe(username2, masterPassword2)
else:
    print("That's not an option")