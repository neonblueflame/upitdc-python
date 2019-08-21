"""
Convert all the items of a random list of length 20 to odd numbers

Author: Sheena Dale Mariano
Date created: 20190821
"""

#Imports
from random import randrange, shuffle

seed = randrange(1, 20, 2)
list = list(range(seed, seed + 20, 2))
shuffle(list)

for i in list:
    print(i)