import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

moves = [rock, paper, scissors] # assigning ASCII graphics to list

user = input("What move do you choose - (r)ock, (p)aper or (s)cissors?\n")

move_choice = ["r", "p", "s"]

print(moves[move_choice.index(user)]) # prints user choice as ASCII art

computer = move_choice[random.randint(0, 2)] # randomly choosing computer move

print(moves[move_choice.index(computer)]) # prints computer choice as ASCII art

if (user == "r" and computer == "s") or (user == "p" and computer == "r") or (user == "s" and computer == "p"):
    print("Congratulations, you win!")
elif user == computer:
    print("It's a draft!")
else:
    print("Computer win, sorry!")
