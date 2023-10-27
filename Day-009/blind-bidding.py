import os, art

# os.system('clear') # for mac, for windows 'cls'
is_everyone_done=True
bidders={}

def highest_bid(bidders):
    highest=0
    for bidder in bidders:
        if bidders[bidder]>=highest:
            highest=bidders[bidder]
            highest_bidder_name=bidder
    return f"The winner is {highest_bidder_name}, with the bid of {highest}"

while is_everyone_done:
    print(art.logo)
    print("Welcome to the secret auction program.")
    name=input("What's your name?\n")
    bid=int(input("What's your bid?\n"))
    bidders[name]=bid
    os.system("clear")
    print(art.logo)
    all_bidders=input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if all_bidders=="no":
        is_everyone_done=False

print(highest_bid(bidders))
# print(bidders)