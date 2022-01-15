# encoder64.py v1.0.0 by Xars7
# 1-14-22
#     Description - This program will use base64 to encode and decode whatever you want
#
#     Requirements - Python 
#
#     How to use - Run the program using "python3 encoder64.py"

import base64
# encoding function
def encodeMessage(message):
    encodedBytes = base64.b64encode(message.encode('utf-8'))
    encodedMsg = str(encodedBytes, 'utf-8')
    print(encodedMsg)
# decoding function
def decodeMessage(message):
    decodedBytes = base64.b64decode(message)
    print(str(decodedBytes))
# main menu
def main():
    # ascii art
    print("""
                             __          _____ __ __
  ___  ____  _________  ____/ /__  _____/ ___// // /
 / _ \/ __ \/ ___/ __ \/ __  / _ \/ ___/ __ \/ // /_
/  __/ / / / /__/ /_/ / /_/ /  __/ /  / /_/ /__  __/
\___/_/ /_/\___/\____/\__,_/\___/_/   \____/  /_/
          """)
    print()
    print('----------------------------------')
    print("[*] encoder64 v1.0.0 by Xars7 [*]")
    print('----------------------------------')
    print()
    while True:
        menuChoice = input("Which would you like to do? 1.Encode 2.Decode : ")
        if menuChoice == "1":
            message = input("Enter a message : ")
            encodeMessage(message)
        elif menuChoice == "2":
            message = input("Enter a message : ")
            decodeMessage(message)
        else:
            quit()        
# start main function on script start up
if __name__ == "__main__":
    main()