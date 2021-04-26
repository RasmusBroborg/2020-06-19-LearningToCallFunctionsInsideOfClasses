#Rock, Paper, Scissors

import random

compWin = "Computer Wins!"
playerWin = "Player wins!"

def winLooseFunction(x):
    win = [["rock", "scissors"], ["paper","rock"], ["scissors","paper"]]
    loose = [["rock","paper"], ["paper","scissors"], ["scissors","rock"]]
    draw = [["rock", "rock"], ["paper", "paper"], ["scissors", "scissors"]]

    
    if x in win:
        print("Player wins!")
    elif x in loose:
        print("Computer wins!")
    elif x in draw:
        print("It's a draw!")
    else:
        print("Something went wrong. :(")


while True:
    amountOfChoices = random.randint(0, 2)
    computerOptions = ["rock", "paper", "scissors"]
    computerChoice = computerOptions[amountOfChoices]
    while True:
        playerChoice = input()
        if playerChoice not in computerOptions:
            print("You can only choose between rock, paper, or scissors. Try again:")
        else:
            break
    
    print("Player chose " + str(playerChoice) + " while the computer chose " + str(computerChoice) + ".")
    
    finale = [playerChoice, computerChoice]
    winLooseFunction(finale)
    
    break
