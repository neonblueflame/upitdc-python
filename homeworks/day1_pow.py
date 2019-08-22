"""
Ask for an integer input n and power p 
to compute the pth power of input n

Author: Sheena Dale Mariano
Date created: 20190820
"""

# Imports
from sys import argv


usage_msg = """
Usage: python day1_pow.py <int n> <int p>
Ex: python day1_pow.py 2 2
"""

# Check if user has entered the correct argument
if len(argv) != 3:
    print(usage_msg)
    exit(1)

try:
    n = int(argv[1])
    p = int(argv[2])
except ValueError:
    print(usage_msg)
    exit(2)

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