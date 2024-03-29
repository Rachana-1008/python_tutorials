
import random

def guess_word_game():
    choices = ["apple", "banana", "orange", "kiwi", "grape"]

    secret_word = random.choice(choices)
    chances = 5
    
    print("Welcome to the Guess the Word Game!")
    print("I have selected a word [apple, banana, orange, kiwi, grape]. Can you guess it?")
    
    while chances > 0:
        guess = input("Enter your guess: ")
        
        if guess == secret_word:
            print("Congratulations! You guessed the correct word.")
            break
        else:
            print("Incorrect guess. Try again.")
            chances -= 1
            print(f"You have {chances} chances left.")
    
    if chances == 0:
        print(f"Sorry, you've run out of chances. The correct word was {secret_word}.")

guess_word_game()




