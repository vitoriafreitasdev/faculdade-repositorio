# value = "y"
# count = 0

# while value:
#     count += 1
#     print(count)
#     if(count == 5):
#         break
#     else:
#         value = 0 # 0 = false, por isso sai do loop, msm usando o continue
#         continue

import sys 
import random
from enum import Enum
def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3    
    playerchoice = input("\n1 for rock,\n2 for paper, or \n3 for scissors: \n\n")

    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3")
        return play_rps()

    player = int(playerchoice)
    
    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS', '').title() + '.')
    print("\nPython chose " + str(RPS(computer)).replace('RPS', '').title() + '.')

    if player == 1 and computer == 3:
        print("You win!")
    elif player == 2 and computer == 1:
        print("You win")
    elif player == 3 and computer == 2:
        print("Ypu win!")
    elif player == computer:
        print("tie game")
    else:
        print("Python wins")
    print("\nPlay again? ")

    while True:
        playagain = input("\nY for Yes or \nQ to Quit \n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n******")
        print("Thank you for playing!\n")
        sys.exit("Bye")
    


    
play_rps()
