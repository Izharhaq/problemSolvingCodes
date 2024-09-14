"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    # Write your code here
    # ********** IZHAR CODE ***********
    if abs(z-x) < abs(z-y):
        return "Cat A"
    elif abs(z-x) > abs(z-y):
        return "Cat B"
    else:
        return "Mouse C"

    # ********* IZHAR CODE *************

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()

"""


q = int(input())

for q_itr in range(q):
    xyz = input().split()
    x = int(xyz[0])
    y = int(xyz[1])
    z = int(xyz[2])


def catAndMouse(x, y, z):
    if abs(z-x) < abs(z-y):
        print("Cat A")
    elif abs(z-x) > abs(z-y):
        print("Cat B")
    else:
        print("Mouse C")


catAndMouse(x, y, z)


"""
def catAndMouse(x, y, z): 
    if abs(x-z)>abs(y-z): 
        return "Cat B" 
    elif abs(x-z)==abs(y-z): 
        return "Mouse C" 
    else: 
        return "Cat A"
"""