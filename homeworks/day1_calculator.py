"""
Divide, multiply, add, subtract 2 inputs from user

Author: Sheena Dale Mariano
Date created: 20190820
"""

# imports
from sys import argv


operators = ["add", "multiply", "subtract", "divide"]

# Check if user has entered the correct arguments
if ( len(argv) != 4 
        or argv[3].lower() not in operators
        or (not argv[1].lstrip("-").isdigit() 
            and not argv[2].lstrip("-").isdigit()) ):
    
    print("Usage: python day1_calculator.py <int> <int> <operator>")
    print("Ex: python day1_calculator.py 1 1 add")
    print(f"Operations: {', '.join(operators)}")
    exit(1)

# Addition
if argv[3].lower() == operators[0]:
    result = int(argv[1]) + int(argv[2])
    operand = "+"
    

# Multiplication
elif argv[3].lower() == operators[1]:
    result = int(argv[1]) * int(argv[2])
    operand = "*"

# Subtraction
elif argv[3].lower() == operators[2]:
    result = int(argv[1]) - int(argv[2])
    operand = "-"
    
# Division
elif argv[3].lower() == operators[3]:
    result = int(argv[1]) / int(argv[2])
    operand = "/"

print(f"{argv[1]} {operand} {argv[2]} = {result}")
