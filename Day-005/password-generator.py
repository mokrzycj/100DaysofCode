# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""

# adding letter
for i in range(0, nr_letters):
    password += letters[random.randint(0, len(letters)-1)]
# adding symbols
for i in range(0, nr_symbols):
    password += symbols[random.randint(0, len(symbols)-1)]
# adding numbers
for i in range(0, nr_numbers):
    password += numbers[random.randint(0, len(numbers)-1)]

print(f"Password with letters, symbols and numbers in order: {password}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
randomized_password = ""
randomized_password_table = []

for i in range(0, nr_letters):
    randomized_password_table += letters[random.randint(0, len(letters)-1)]
    # print(randomized_password_table)
for i in range(0, nr_symbols):
    randomized_password_table.insert(random.randint(0, len(
        randomized_password_table)-1), symbols[random.randint(0, len(symbols)-1)])
for i in range(0, nr_numbers):
    randomized_password_table.insert(random.randint(0, len(
        randomized_password_table)-1), numbers[random.randint(0, len(numbers)-1)])

# for letter in randomized_password_table:
#     randomized_password+=letter

randomized_password = ''.join(randomized_password_table)


print(
    f"Password with symbols and numbers on random positions: {str(randomized_password)}")
