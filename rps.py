import random

user_win=0
comp_win=0

option=["rock", "paper", "scissors"]


while True:
    user_input=input("Enter Rock, Paper, Scissors or Q (to quit)").lower()
    if user_input== 'q':
        break
    if user_input not in option:
        continue
    r=random.randint(0,2)
    computer_pick=(option[r])
    
    print("Computer picked", computer_pick+".")
    if user_input== computer_pick:
        continue
    if user_input=="rock" and computer_pick=="scissors" :
        print("You won")
        user_win += 1
    elif user_input=="paper" and computer_pick=="rock":
        print("You won")
        user_win += 1
    elif user_input=="scissors" and computer_pick=="paper":
        print("You won")
        user_win += 1
    else:
        print("You lost")
        comp_win +=1
print("User won:", user_win ,"times")
print("Computer won",comp_win,"times")
print("Goodebye!")
    

    
    
    
            