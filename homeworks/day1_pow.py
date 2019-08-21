"""
Ask for an integer input n and power p 
to compute the pth power of input n

Author: Sheena Dale Mariano
Date created: 20190820
"""

# Imports
from sys import argv


# Check if user has entered the correct argument
#TODO: Check if number argument has at least a character that isn't a number
if (len(argv) != 3 
        or (not argv[1].lstrip("-").isdigit() 
            and not argv[2].lstrip("-").isdigit())):
    
    print("Usage: python day1_pow.py <int n> <int p>")
    print("Ex: python day1_pow.py 2 2")
    exit(1)

n = int(argv[1])
p = int(argv[2])

# Shortcut
# print(f"{n} ** {p} = {n ** p}")

# Longcut
power = 1.0

if p < 0:
     for i in range(p, 0, 1):
        power /= n
else:
    for i in range(p):
        power *= n

print(f"{n} ** {p} = {power}")