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
import random

moves=[rock, paper, scissors]
user=input("What move do you choose - (r)ock, (p)aper or (s)cissors?\n")
move_choice=["r", "p", "s"]
print(moves[move_choice.index(user)])
computer=move_choice[random.randint(0,2)]
print(moves[move_choice.index(computer)])

if (user=="r" and computer=="s") or (user=="p" and computer=="r") or (user=="s" and computer=="p"):
    print("Congratulations, you win!")
elif user==computer:
    print("It's a draft!")
else:
    print("Computer win, sorry!")