# PROGRAM TO BUILD A BASIC CALCULATOR

# taking integers and operator input.

number1 = int(input("Enter num 1: "))
number2 = int(input("Enter num 2: "))

operator = input("Enter an operator from '+', '-', '*', '/', '%', '^', '**' : ")

# checking if the operator inputted is from "+-*/%^**" or not. If not, it asks for the operator input again.

while operator not in "+-*/%^**": 
        operator = input("Please enter any one operator from '+', '-', '*', '/', '%', '^', '**' : ")

# function to perform calculation on the integers based on the operator inputted.

def calculator(number1, number2, operator): 
    if operator == '+':
        return number1+number2
    elif operator == '-':
        return number1-number2
    elif operator == '*':
        return number1*number2
    elif operator == '/':
        try:
            return (number1/number2)
        except ZeroDivisionError:
            return ("Division by 0 gives an error")
        else:
            return (number1/number2)
    elif operator == '%':
        try:
            return (number1%number2)
        except ZeroDivisionError:
            return ("Division by 0 gives an error")
        else:
            return (number1%number2)
    elif operator == '^' or operator == '**':
        return number1**number2
    
# Calling the function with the required arguments.

print("Answer is:", calculator(number1, number2, operator))
