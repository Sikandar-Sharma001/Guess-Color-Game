import random
from time import sleep
print("**WELCOME TO CCG GAME**")
print("Winning rule of computer is as follows:"+"\nEnter a choice of the following colours and match the Computer's choice to win___")
player_score=0
computer_score=0

while(True):
    print("Violet-> 1")
    print("Indigo-> 2")
    print("Blue->   3")
    print("Orange-> 4")
    print("Red->    5")
    #take input from the user
    player_choice = int(input("Your Turn!"+"\nChoose any of the color: "))
    #incase of invalid input
    while player_choice>5 or player_choice<1:
        player_choice = int(input("Enter valid input:__"))
    if player_choice==1:
        print("You have chosen Violet")
    elif player_choice==2:
        print("You have chosen Indigo")
    elif player_choice==3:
        print("You have chosen Blue")
    elif player_choice==4:
        print("You have chosen Orange")
    else :
        print("You have chosen Red")
    sleep(1)
    print("\nNow it's computer's turn to choose a colour_____")
    sleep(2)
    #computer will choose random number from 1-5
    computer_choice = random.randint(1,5)
    if computer_choice == 1:
        print("Computer has chosen Violet")
    elif computer_choice == 2:
        print("Computer has chosen Indigo")
    elif computer_choice == 3:
        print("Computer has chosen Blue")
    elif computer_choice == 4:
        print("Computer has chosen Orange")
    else:
        print("Computer has chosen Red")
    sleep(2)
        #condition for winning
    if player_choice==computer_choice:
        player_score+=1
    else:
        computer_score+=1
    print("\nPlayer's Score: %d"%player_score)
    print("Computer's Score: %d"%computer_score)
    sleep(1)
    print("\nDo you want to play again?(yes/no)")
    player_response=input()
    if player_response == 'no' or player_response=='No':
        break
#Conclusions
if player_score==computer_score:
    print("<==MATCH TIED==>"+"\nThanks for Playing_-^-_")
if player_score < computer_score:
    print("<==COMPUTER WON==>" +"\nBetter Luck Next time!"+"\nThanks for Playing_-^-_")
if player_score > computer_score:
    print("YOU ARE VICTORIOUS"+"\n<==PLAYER WON==>" + "\nThanks for Playing_-^-_")



