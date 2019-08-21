"""
Print the equivalent grade in letters:
A = Above 90
B = 80 to 90
C = 70 to 80
E = Below 70

Author: Sheena Dale Mariano
Date created: 20190820
"""

# Imports
from sys import argv


# Check if user has entered the correct argument
#TODO: Check if number argument has at least a character that isn't a number
if len(argv) != 2 and argv[1].lstrip("-").isnumeric():
    print("Usage: python hw_grade.py <grade in numbers>")
    print("Ex: python hw_grade.py 90")
    exit(1)

# Get user's input and convert to integer
raw_grade = float(argv[1])

print("Equivalent grade: ")

if (raw_grade > 90.0):
    print("A")
    
elif (80 < raw_grade <= 90.0):
    print("B")

elif (70.0 <= raw_grade <= 80.0):
    print("C")
    
else:
    print("E")
