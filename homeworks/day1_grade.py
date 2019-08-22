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


usage_msg = """
Usage: python day1_grade.py <float grade in numbers>
Ex: python day1_grade.py 90.1
"""

# Check if user has entered the correct argument
if len(argv) != 2:
    print(usage_msg)
    exit(1)

# Get user's input and convert to float
try:
    raw_grade = float(argv[1])
except ValueError:
    print(usage_msg)
    exit(2)

print("Equivalent grade: ")

if (raw_grade > 90.0):
    print("A")
    
elif (80 < raw_grade <= 90.0):
    print("B")

elif (70.0 <= raw_grade <= 80.0):
    print("C")
    
else:
    print("E")
