"""
Print the nth Fibonacci number

Author: Sheena Dale Mariano
Date created: 20190821
"""

# Imports
from sys import argv

if (len(argv) != 2 or not argv[1].isdigit()):
    print("Usage: python hw_fibonacci.py <int n>")
    print("Where int is a positive integer")
    print("Ex: python hw_fibonacci.py 10")
    exit(1)

n = int(argv[1])
num_cur = 0
num_prev = 0

# Shortcut
"""
phi = (1 + (5 ** 0.5)) / 2
phi_assoc = (1 - (5 ** 0.5)) / 2
num_cur = int( ((phi ** n) - (phi_assoc ** n)) / (5 ** 0.5) )
"""

# Longcut
for i in range(n + 1):
    num_temp = num_cur
    num_cur += num_prev
    
    if num_prev == 0:
        num_prev += 1
    else:
        num_prev = num_temp

print(f"{n}: {num_cur}")
