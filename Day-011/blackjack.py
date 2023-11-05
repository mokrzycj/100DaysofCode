import art, random, os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playerWins=0
computerWins=0

def choose_random_card():
    return cards[random.randint(0, len(cards)-1)]

def score(cards):
    return sum(cards)

def cards_and_scores(userCards, computerCards, userScore, computerScore, winner):
    os.system("clear")
    print(art.logo)
    print(f"Your cards are {userCards} and your score is {userScore}")
    print(f"Computer cards are {computerCards} and it's score is {computerScore}.")

    if winner=="player":
        print("You win!!!")
        global playerWins, computerWins
        playerWins+=1
        print(f"Players total score: {playerWins}")
        print(f"Computer total score: {computerWins}")
    elif winner=="computer":
        print("You loose!")
        computerWins+=1
        print(f"Players total score: {playerWins}")
        print(f"Computer total score: {computerWins}")
    elif winner=="draw":
        print("it's a draw.")
    

def blackjack():
    wantToPlay=input("Do you want to play blackjack? Press 'y' or 'n': ")
    os.system("clear")
    if wantToPlay == 'n':
        return
    print(art.logo)

    userCards = [choose_random_card(), choose_random_card()]
    computerCards = [choose_random_card(), choose_random_card()]
    # userCards = [11,11]
    userScore=score(userCards)
    computerScore=score(computerCards)

    if userScore>21 and 11 in userCards:
        userCards[userCards.index(11)]=1
        userScore=score(userCards)

    print(f"Your cards are {userCards}, and your current score is {userScore}")
    print(f"Computer first card is [{computerCards[0]}]")

    if computerScore==21 or (userScore and computerScore)==21:
        cards_and_scores(userCards, computerCards, userScore, computerScore, "computer")
        return blackjack()
    elif userScore==21:
        cards_and_scores(userCards, computerCards, userScore, computerScore, "player")
        return blackjack()
    elif userScore>21:
        userCards[0]=1
        userScore=score(userCards)

    anotherCard=input("Do you want next card? 'y' or 'n': ")
    while anotherCard == 'y' and userScore<21:
        userCards.append(choose_random_card())
        userScore=score(userCards)
        if userScore>21 and 11 in userCards:
            userCards[userCards.index(11)]=1
            userScore=score(userCards)
        print(f"Your cards are {userCards}, and your current score is {userScore}")
        if userScore>21 and 11 in userCards:
            userCards[userCards.index(11)]=1
            userScore=score(userCards)

        if userScore==21:
            cards_and_scores(userCards, computerCards, userScore, computerScore, "player")
            return blackjack()
        elif userScore>21:
            cards_and_scores(userCards, computerCards, userScore, computerScore, "computer")
            return blackjack()

        anotherCard=input("Do you want next card? 'y' or 'n': ")
    
    while computerScore<=17:
        computerCards.append(choose_random_card())
        computerScore=score(computerCards)
        print(f"Computer cards are {computerCards}")
    
    if computerScore == userScore:
        cards_and_scores(userCards, computerCards, userScore, computerScore, "draw")
        return blackjack()
    elif computerScore>userScore and computerScore<=21:
        cards_and_scores(userCards, computerCards, userScore, computerScore, "computer")
        return blackjack()
    elif computerScore<userScore or computerScore>21:
        cards_and_scores(userCards, computerCards, userScore, computerScore, "player")
        return blackjack()

    


blackjack()



############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

