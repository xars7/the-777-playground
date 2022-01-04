# PasswordSafe v1.0.0 by Kevin Flynn (xars7)
# 
#   Description - This program will create a folder that it stores your passwords in. Each password get's it's own designated .txt file. Along with another file containing
#                 your master password. Now I know what your thinking "Kevin my passwords wouldn't really be safe if they were just in a text file waiting for someone to read
#                 them" and you are absolutely right. That's why we are going to encrypt them before we send them to their designated txt file. The only way you'll be able 
#                 to access your passwords is if you enter in the correct master password and login.
#
#
#   HOW TO USE: 
#               Step 1. Start up the program and enter in the number "1". This will bring you through the creation process of your master credentials wich will be stored in
#                       the "MasterCreds" folder
#               Step 2. Login to your vault by pressing the number "2" button the next time the program asks you to choose. Enter in your master credentials that you created
#                       in step 1.
#               Step 3. You will be prompted on whether or not you want to generate a password or view a password. To generate a password enter in the number "2". Enter in the 
#                       name that you want to find your credentials by for example ("GMail"), the username for your password, whether you want special characters or not, and then
#                       the length that you want your password
#               Step 4. To view a password simply access the vault again by loggin in and select the view password option number "1". Enter in the name that you specified last time
#
#                       ****NOTE**** this program is very case sensitive, if the program cannot find your password please check your spelling. As a last resort you can always
#                                    check the "UsernameDB" and the "PasswordDB" to find the exact name you used for your credentials
#               Step 5. Enjoy the feeling of having your passwords protected!
#
# Import modules
import os
from cryptography.fernet import Fernet
import random
import string

# Print program version number
print("PasswordSafe v1.0.0 by Kevin Flynn(xars7)")

# when the user chooses this option we want them to be able to view their passwords
def viewPasswords():
    # get the encryption key
    with open("PasswordSafe/MasterCreds/EncryptionKey.key", "rb") as encKey:
        key = encKey.read()

    # Create a Fernet object with key
    f = Fernet(key)
    # Find the password the user wants to see
    findPassName = input("Please enter the name of the password you are looking for (Ex. Google) : ")
    # open the password file with the designated name
    with open("PasswordSafe/PasswordDB/" + findPassName, "rb") as password:
        thePass = password.read()
    # open the username file with the designated name
    with open("PasswordSafe/UsernameDB/" + findPassName, "rb") as username:
        theUser = username.read()

    # decrypt the password and username
    decryptedPass = f.decrypt(thePass)
    decryptedUser = f.decrypt(theUser)
    # decodes the password and username to display it to the user
    decodedPass = decryptedPass.decode()
    decodedUser = decryptedUser.decode()
    # print the credentials
    print("Your credentials are : " + decodedUser + " | " + decodedPass)

# This function creates the passwords
def createPassword():
    # when the user chooses this option we want them to be able to create a random password for the database
    # they need to be able to choose the length of the password and wether or not special characters are needed
    # and then save the login credentials in files named by the user

    # find the encryption key
    with open("PasswordSafe/MasterCreds/EncryptionKey.key", "rb") as encKey:
        key = encKey.read()

    # create a Fernet object using the key
    f = Fernet(key)
    
    # grab info on password from the user
    passwordName = input("Please enter the Name you want to call this login : ")
    passwordUser = input("Please enter the username you want to use for this login : ")
    enableSpecChar = input("Do you need Special Characters? (y/n) : ")
    passwordLength = input("Please enter the length of your password : ")

    # if the user needs special characters generate a password with special characters 
    # if not generate a password without special characters
    if enableSpecChar == "Y" or enableSpecChar == "y":
        # defines what letters to use
        letters = string.ascii_letters + string.digits + string.punctuation
        # generate the password
        passw0rd = ''.join(random.choice(letters) for i in range(int(passwordLength)))
        # print the password
        print(passw0rd)
        # encode the username and  password before encryption
        encodedPass = passw0rd.encode("utf-8")
        encodedUser = passwordUser.encode('utf-8')
        # encrypt the username and password
        encryptedPass = f.encrypt(encodedPass)
        encryptedUser = f.encrypt(encodedUser)
        # create a password file and store the encrypted password in it
        with open("PasswordSafe/PasswordDB/" + passwordName, "wb") as password:
            password.write(encryptedPass)
        # create a username file and store the encypted username in it
        with open("PasswordSafe/UsernameDB/" + passwordName, "wb") as username:
            username.write(encryptedUser)
    elif enableSpecChar == "N" or enableSpecChar == "n":
        # defines what letters to use
        letters = string.ascii_letters + string.digits
        # generate the password
        passw0rd = ''.join(random.choice(letters) for i in range(int(passwordLength)))
        # print the password
        print(passw0rd)
        # encrypt the password
        encryptedPass = f.encrypt(passw0rd)
        encryptedUser = f.encrypt(passwordUser)
        # create a password file and store the encrypted password in it
        with open("PasswordSafe/PasswordDB/" + passwordName, "wb") as password:
            password.write(encryptedPass)
        # create a username file and store the encypted username in it
        with open("PasswordSafe/UsernameDB/" + passwordName, "wb") as username:
            username.write(encryptedUser)

# create new passwords or view passwords we've created
def accessVault():
    # ask the user if they want to create a password or view their passwords
    vaultMenuChoice = input("1. View my passwords 2. Create a password : ")

    if vaultMenuChoice == "1":
        # view passwords
        viewPasswords()
    elif vaultMenuChoice == "2":
        # create a password
        createPassword()
    else:
        print("That's not a menu choice")

# Create a login with a username and master password
def createALogin(usernameCreate, masterPasswordCreate):
    # generate an encryption key 
    key = Fernet.generate_key()
    f = Fernet(key)
    # write that encryption key to a key file for safe keeping
    with open("PasswordSafe/MasterCreds/EncryptionKey.key", "wb") as fernetKey:
        fernetKey.write(key)

    # encode the username and master password before encryption
    encodedUserCred = usernameCreate.encode("utf-8")
    encodedPassCred = masterPasswordCreate.encode("utf-8")
    # encrypt the usernameCreate and masterPasswordCreate
    encryptedUser = f.encrypt(encodedUserCred)
    encryptedMassPass = f.encrypt(encodedPassCred)
    # write the encrypted login to a login file
    with open("PasswordSafe/MasterCreds/Login.txt", "wb") as login:
        login.write(encryptedUser) 
    # write the encrypted MasterPassword to a MasterPassword File
    with open("PasswordSafe/MasterCreds/MasterPassword.txt", "wb") as masterPass:
        masterPass.write(encryptedMassPass)

# login to the password safe using the inputed master password and username
def loginToSafe(usernameLogin, masterPasswordLogin):
    # read the encryption key
    with open("PasswordSafe/MasterCreds/EncryptionKey.key", "rb") as fernetKey:
        key = fernetKey.read()
    # read the encrypted login to a login file
    with open("PasswordSafe/MasterCreds/Login.txt", "rb") as login:
        usernameCheck = login.read()
    # read the encrypted MasterPassword to a MasterPassword File
    with open("PasswordSafe/MasterCreds/MasterPassword.txt", "rb") as masterPass:
        masterPassCheck = masterPass.read()
    
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
        accessVault()
    else:
        print("wrong login credentials")

# this is our main function
def main():
    # This is our main while loop
    while True:
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
        # If the user types quit quit the program
        elif mainMenuChoice == "Quit" or mainMenuChoice == "quit" or mainMenuChoice == "Exit" or mainMenuChoice == "exit":
            quit()
        else:
            print("That's not an option")

# Run our main function on startup
if __name__ == "__main__":
    main()