import os
import random

def userInput():

    options = ["Rock", "Paper", "Scissors"]

    computer_input = random.randint(0, 2)


    user_input = (int(input("1) Rock --- "
                           "2) Paper --- "
                           "3) Scissors \n"
                           "------------------------------------ \n"
                           "User options ---> "))-1)

    os.system("cls")

    print("User ---> " + options[user_input])
    print("Computer ---> "+options[computer_input]+"\n")

    inputs = [computer_input, user_input]
    return inputs

def checkWinner(computer_input, user_input):

    if user_input == computer_input:
        print("Its a Tie!!!")
    elif user_input == 0 and computer_input == 2:
        print("You Win!!!")
    elif user_input == 1 and computer_input == 0:
        print("You Win!!!")
    elif user_input == 2 and computer_input == 1:
        print("You Win!!!")
    else:
        print("You Lose!!!")

def playAgain():
    again = input("Do you want to play again? (y/n) ")
    if again == "y":
        os.system("cls")
        main()
    else:
        exit(0)

def main():
    inputs = userInput()
    checkWinner(inputs[0], inputs[1])
    playAgain()

if __name__ == '__main__':
    main()