print('Welcome to the Tip Calculator')

totalAmount = input("What was the total amount? ")
peopleNumber = input("How many people to split the bill? ")
tipAmount = input('What percentage tip would you like to give? 10%, 12% or 15% ')

totalWithTip=int(totalAmount)*(1+int(tipAmount)/100)
perPerson = round(int(totalWithTip)/int(peopleNumber),2)

print("Each person should pay: " + str(perPerson))

# PEMDASLR - order of math operations in Python
# ()
# **
# * /
# + -

# 8//3 = integer (1)