#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from math import pi
import random
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  

"""
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard':")

guessed_correct = True

genereted_number = random.randint(1,100)
def check():
    global guessed_correct
    global number_of_guess 
    user_input = int(input("Make a guess: "))
    if(user_input == genereted_number):
        print(f"You got it! The answer was {genereted_number}.")
        guessed_correct = False
    else:
        number_of_guess = number_of_guess - 1
        print(f"You have {number_of_guess} attempts remaining to guess the number.")
        if(user_input > genereted_number):
            print("Too High")
        else:
            print("Too Low")
        
        print("Guess Again.")
        print(f"You have {number_of_guess} attempts remaining to guess the number.")
        if(number_of_guess == 0):
            guessed_correct = False
            print("You've run out of guesses, you lose.")

number_of_guess = 0
while(guessed_correct == True):
    if(difficulty_level == 'easy'):
        number_of_guess = 10
        
        check()
            
    else:
        number_of_guess = 5
        check()
