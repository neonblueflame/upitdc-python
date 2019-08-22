"""
Either convert peso to dollars or vice versa. The 
conversation rate of a dolar to peso should be asked 
from the user.

Author: Sheena Dale Mariano
Date created: 20180822
"""

# Imports
from sys import argv


usage_msg = """
Usage: python day1_conversion.py <float value> <str value currency>
Where value currency can be: peso, dollar
Ex: python day1_conversion.py 10.0 peso
"""

# Check if user has entered the correct argument
if len(argv) != 3:
    print(usage_msg)
    exit(1)

# Check if rate and amount is a proper float value
try:
    print("What is the current conversion rate?")
    rate = float(input())
    value = float(argv[1])
except ValueError:
    print(usage_msg)
    exit(2)

if argv[2].lower() == "peso":
    conversion_currency = "dollar"
    conversion_value = value / rate
    
elif argv[2].lower() == "dollar":
    conversion_currency = "peso"
    conversion_value = value * rate
    
else:
    print(usage_msg)
    exit(3)
    
print(f"{value} {argv[2]} in {conversion_currency}: {conversion_value}")
