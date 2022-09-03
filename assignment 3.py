import random


def guessGame():
    playA = 'y'
    score = 0

    while playA == 'y':

        computerNum = random.randint(1, 50)
        userNum = int(input("\nEnter a number between 1 to 50 - "))

        diff = computerNum - userNum

        if computerNum == userNum:
            print("Its the same number, wow you get 50 Points ")
            score = score + 50
            print("Your updated score is ", score)
        elif diff >= -5 and diff <= 5:
            print("this number is very close to real number ")
            print("UserNum = ", userNum)
            print("ComputerNum = ", computerNum)
            score = score + 25
            print("Your updated score is ", score)
        elif diff >= - 10 and diff <= 10:
            print("this number is close to real number ")
            print("UserNum = ", userNum)
            print("ComputerNum = ", computerNum)
            score = score + 10
            print("Your updated score is ", score)
        else:
            print("Sorry your guess didnt make it ")
            print("UserNum = ", userNum)
            print("ComputerNum = ", computerNum)
            print("Your updated score is ", score)

        playA = playAgain()
    else:
        print("Final Score = ", score)