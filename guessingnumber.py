'''def guess_number_game():
    target_number = 18
    chances = 5
    
    print("Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 20. Can you guess it?")
    
    while chances > 0:
        guess = int(input("Enter your guess: "))
        
        if guess == target_number:
            print("Congratulations! You guessed the correct number.")
            break
        elif guess < target_number:
            print("Incorrect guess. The number is greater. Try again.")
        else:
            print("Incorrect guess. The number is smaller. Try again.")
            
        chances -= 1
        print(f"You have {chances} chances left.")
    
    if chances == 0:
        print(f"Sorry, you've run out of chances. The correct number was {target_number}.")

guess_number_game()
'''
import random

def guess_number_game():
    secret_number = random.randint(1, 10)
    
    chances = 5
    
    print("Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 10. Can you guess it?")
    
    while chances > 0:
        guess = int(input("Enter your guess: "))
        
        if guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            break
        else:
            print("Incorrect guess. Try again.")
            chances -= 1
            print(f"You have {chances} {'chance' if chances == 1 else 'chances'} left.")
    
    if chances == 0:
        print(f"Sorry, you've run out of chances. The correct number was {secret_number}.")

guess_number_game()
