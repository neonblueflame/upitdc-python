"""
Identify if the input year is a leap year. A leap year 
happens every 4 years, except for 100th year. But the 
400th year is a leap year. 
Hint: 2004 is a leap year.

Author: Sheena Dale Mariano
Date created: 20190823
"""

# Imports
from sys import argv


usage_msg = """
Usage: python day1_leapyear.py <int year>
Ex: python day1_leapyear.py 1994
"""

# Check if user has entered the correct argument
if len(argv) != 2:
    print(usage_msg)
    exit(1)

# Get user's input and convert to float
try:
    year = int(argv[1])
except ValueError:
    print(usage_msg)
    exit(2)

if (year % 100 == 0) and (year % 400 == 0):
    print(f"{argv[1]} is a leap year")
    
elif (year % 100 != 0) and (year % 4 == 0):
    print(f"{argv[1]} is a leap year")
          
else:
    print(f"{argv[1]} is not a leap year")
