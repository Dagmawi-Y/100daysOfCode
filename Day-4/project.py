import random

rock = "rock"
paper = "paper"
scissors = "scissors"

options = [rock, paper, scissors]

player_choice_number = int(input("What do you choose? type 0 for rock, 1 for Paper and 2 for scissors. "))

if player_choice_number > 2:
    player_choice_number = 2


player_choice = options[player_choice_number]
computer_choice = options[random.randint(0, 2)]


print(f"your choice: {options[player_choice_number]}")
print (f"computer choice: {computer_choice}")

if player_choice == computer_choice:
    print ("Its a tie. please play again. ")
else:
    if ((player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock")):
        print ("You won!")
    else:
        print("You lost!")
