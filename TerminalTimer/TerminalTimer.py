# TerminalTimer v1.0.0 by KevinFlynn/xars7
# 1-7-22
#   Description -
#       This is a program that I originally found on https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/
#       that I modified for my own liking. I like to segment my work time into 30 minute blocks so I often find myself using 
#       https://www.online-stopwatch.com/ which granted is an awesome and much better put together program than mine, but I wanted
#       to make my own so here it is. 
#   
#       I would like to eventually make this program take an input with minutes and seconds as apposed to having to input the time by seconds
# 
#       The only way to currently exit out of the stop watch and countdown is by hitting CTRL+C so keep that in mind. I would like to fix this 
#       in the future.
import time

amIRunning = True

def countDown(countTime):

    while countTime:
        mins, secs = divmod(countTime, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        countTime -= 1

    print('Time is up!')


def stopWatch():
    countTime = 0
    while amIRunning:
        mins, secs = divmod(countTime, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        countTime += 1


def main():
    menuChoice = input("1.CountDown 2.StopWatch Q/q for quit : ")
    while True:
        if menuChoice == "1":
            countTime = input("Enter the time in seconds: ")
            countDown(countTime)
        elif menuChoice == "2":
            stopWatch()
        elif menuChoice == "Q" or "q":
            quit()
        else:
            print("That's not a menuchoice")

if __name__ == "__main__":
    main()