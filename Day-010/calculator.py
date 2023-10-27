import art, os

is_end_of_calculations=True
choice="n"
result=0

def adding(x, y):
    global result
    result=x+y
    return print(f"{x} + {y} = {result}")

def subtracting(x, y):
    global result
    result = x-y
    return print(f"{x} - {y} = {result}")

def multiplying(x, y):
    global result
    result = x*y
    return print(f"{x} * {y} = {result}")

def division(x, y):
    global result
    if y == 0:
        return print("You can't divide by 0!")
    else:
        result=x/y
    return print(f"{x} / {y} = {result}")


while is_end_of_calculations:
    print(art.logo)
    if choice=='n':
        first_number=float(input("What's the fiest number? "))
    
    print("""
        +
        -
        *
        /
        """)
    operation=input("Choose an operation: ")
    second_number=float(input("What's the second number? "))
    if operation=='+':
        adding(first_number, second_number)
    elif operation == '-':
        subtracting(first_number, second_number)
    elif operation == '*':
        multiplying(first_number, second_number)
    elif operation =='/':
        division(first_number, second_number)
    choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if choice == 'y':
        first_number=result
        print(first_number)
    os.system("clear")
    