# Dog_Hasher.py v1.0.0 by Kevin Flynn/xars7
#
# Description - 
#   This program is the opposite of hashcat. It will take a password from the rockyou.txt dictionary file, hash it using the algorithm you choose and (md5, sha1, sha224, etc), and 
#   give you the hash to crack. Good luck and have fun cracking!
#
# All you need to run this program is Python

# import modules
import hashlib
import random
import os

# get the path to the rockyou.txt file located in the project folder
#file_path = str(pathlib.Path.cwd() + "/rockyou.txt")

full_path =  os.path.realpath(__file__)
file_path = os.path.dirname(full_path)

# our main function
def main():
    # print version number
    print("Dog_Hasher v1.0.0 by Kevin Flynn/xars7")
    # asks for user input
    print("Please select a hash algorithm")
    menuChoice = input("1. MD5 2. SHA1 3. SHA224 4. SHA256 5. SHA384 6. SHA512 : ")
    # send our user to the correspondinig option that they chose in the input
    # each if statement is the same the only difference is the hashing algorithm
    if menuChoice == '1':
        # finds the rockyou.txt, chooses a random line, and assigns it to password
        password = random.choice(open(file_path, errors="ignore").readlines())
        # prints the password in plain text
        print(password)
        # hashes the password
        hash_object = hashlib.md5(password.encode())
        # prints the hashed password
        print(hash_object.hexdigest())
    elif menuChoice == '2':
        password = random.choice(open(file_path, errors="ignore").readlines())
        print(password)
        hash_object = hashlib.sha1(password.encode())
        print(hash_object.hexdigest())
    elif menuChoice == '3':
        password = random.choice(open(file_path, errors="ignore").readlines())
        print(password)
        hash_object = hashlib.sha224(password.encode())
        print(hash_object.hexdigest())
    elif menuChoice == '4':
        password = random.choice(open(file_path, errors="ignore").readlines())
        print(password)
        hash_object = hashlib.sha256(password.encode())
        print(hash_object.hexdigest())
    elif menuChoice == '5':
        password = random.choice(open(file_path, errors="ignore").readlines())
        print(password)
        hash_object = hashlib.sha384(password.encode())
        print(hash_object.hexdigest())
    elif menuChoice == '6':
        password = random.choice(open(file_path, errors="ignore").readlines())
        print(password)
        hash_object = hashlib.sha512(password.encode())
        print(hash_object.hexdigest())
    # if the user doesn't input an option quit the application 
    else:
        quit()
# run our main function on program startup
if __name__ == "__main__":
    main()
    
    
