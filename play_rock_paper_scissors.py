import random

def play_rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    
    print("Welcome to Rock, Paper, Scissors Game!")
    
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ")
        
        if user_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(choices)
        
        print(f"You choose {user_choice}. Computer choose {computer_choice}.")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("Computer wins!")
        
        play_again = input("Do you want to play again? (y/n): ")
        if play_again != "y":
            print("Thanks for playing! Goodbye.")
            break

play_rock_paper_scissors()


