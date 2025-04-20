import random

username = input("Please enter your username")

steps = 0
game_status = True

while(game_status):
    if (steps==0):
        print("\n\n\nWelcome to the Number Guessing Game. A game of wits and technique\n Guess the number between 1-100 the computer has chosen in the last number of steps\n ARE YOU READY!!!\n\n\n")

        computer_choice = random.randint(1,100)
        try:
            user_choice = int(input("Please select your input\n"))
        except:
            print(f"Don't act smart, {username} , I can't detect words\n\n")

    if(user_choice != computer_choice):
        steps +=1
        if(user_choice>computer_choice):
            try:
                user_choice = int(input(f"The number is lower than {user_choice}. Try Again\n"))
            except:
                print(f"Don't act smart, {username} , I can't detect words\n\n")
        else:
            try:
                user_choice = int(input(f"The number is higher than {user_choice}. Try Again\n"))
            except:
                print(f"Don't act smart, {username} , I can't detect words\n\n")
    else:
        print(f"Congratualations! {username} You got it right in {steps} attempts")

        restart_game = input("Would you like to play again (y/n)")
        if(restart_game=="y"):
            game_status=True
            steps=0
        else:
            game_status=False
else:
    print("Thank you for playing Number Guessing Game")



