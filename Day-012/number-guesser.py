#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art, random, os

def random_number():
    return 2

def next_game():
    if input("Do you want to play one more time? 'y' or 'n': "):
        guessing_game()

def what_difficulty(mode):
    if mode=='easy':
        return 10
    elif mode=='hard':
        return 5
    
def guessing_game():
    os.system("clear")
    print(art.logo)
    randomNumber=random.randint(0, 100)
    print(random_number)

    print("Welcome to the number guessing game!")
    print("I'm thinking about a number between 1 and 100!")
    difficultyMode=input("Choose difficulty level. Type 'hard' or 'easy' ")

    numberOfAttempts = what_difficulty(difficultyMode)
    print(f"You have {numberOfAttempts} attempts left.")
    
    userGuessed=False

    while not userGuessed and numberOfAttempts>0:
        userGuess=int(input("Make a guess: "))
        numberOfAttempts-=1
        if userGuess==randomNumber:
            print("You win!")
            userGuessed=True
            next_game()
        elif userGuess>randomNumber:
            print("Your number is too high.")
        elif userGuess<randomNumber:
            print("Your number is too low.")
        
        if numberOfAttempts==0 and not userGuessed:
            print("You lost.")

        if numberOfAttempts==0:
            next_game()
        print(f"----- You have {numberOfAttempts} attempts left. -----")



guessing_game()