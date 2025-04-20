# print("Hello World") --> First line of the code
import random

user_name = input("Please enter your username\n")

play_status = True

while(play_status):
    user_choice = input("Rock, Paper, Scissors ?\n")
    user_choice = user_choice.upper()

    computer_choice_list = ["ROCK","PAPER","SCISSORS"]
    computer_choice = random.choice(computer_choice_list)

    print(f"{user_name} choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")

    # Winning scenarios
    if(user_choice == "ROCK" and computer_choice == "SCISSORS"):
        print(f"{user_name} won !")
    elif (user_choice == "PAPER" and computer_choice == "ROCK"):
        print(f"{user_name} won !")
    elif(user_choice == "SCISSORS" and computer_choice == "PAPER"):
        print(f"{user_name} won !")
    # Losing Scenarios
    elif(user_choice == "ROCK" and computer_choice == "PAPER"):
        print(f"Computer won !")
    elif (user_choice == "PAPER" and computer_choice == "SCISSORS"):
        print(f"Computer won !")
    elif(user_choice == "SCISSORS" and computer_choice == "ROCK"):
        print(f"Computer won !")
    # Tie Scenarios
    elif(user_choice==computer_choice):
        print("It's a draw ")
    else:
        print("Please enter a valid input")

    restart_game = input("Would you like to play again (y/n)")

    if(restart_game =="y"):
        play_status = True
    else:
        play_status = False

else:
    print("Thank you for playing Rock Paper Scissors")    
    

    