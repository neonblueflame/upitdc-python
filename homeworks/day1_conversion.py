"""
Either convert peso to dollars or vice versa. The 
conversation rate of a dolar to peso should be asked 
from the user.

Author: Sheena Dale Mariano
Date created: 20180822
"""

# Imports
from sys import argv

# Check if user has entered the correct argument
#TODO: Check if argument is a number or a float
if len(argv) != 3:
    print("Usage: python day1_conversion.py <float value> <str value currency>")
    print("Where value currency can be: peso, dollar")
    print("Ex: python day1_conversion.py 10.0 peso")
    exit(1)

print("What is the current conversion rate?")
rate = float(input())
value = float(argv[1])

#TODO: Study this more :(
if argv[2].lower() == "peso":
    conversion_currency = "dollar"
    conversion_value = value / rate
    
elif argv[2].lower() == "dollar":
    conversion_currency = "peso"
    conversion_value = value * rate
    
else:
    print("Currency can be: peso, dollar")
    exit(2)
    
print(f"{value} in {conversion_currency}: {conversion_value}")
