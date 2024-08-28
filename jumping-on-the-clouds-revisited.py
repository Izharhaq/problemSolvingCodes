"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()

"""

nk = input().split()
n = int(nk[0])
k = int(nk[1])
c = list(map(int, input().rstrip().split()))
# n = 8
# k = 2
# c = [0,0,1,0,0,1,1,0] 


def jumpingOnClouds(c, k):
    e = 100
    n = len(c)
    i = 0
    while True:
        i = (i+k)%n
        e -=1
        if c[i] ==1:
            e -= 2
        if i ==0:
            break
    return e
    # print(e)

jumpingOnClouds(c, k)

# **********Approach to write this code ********************8 ->>
# e = 100 ->> Start with 100 units of energy
# n = len(c) ->> Length of the list
# i  == 0 ->> Start at the first position (index 0)
# i = (i + k) % n ->> ->> ->>
# i + k adds k to the current position i, moving k steps ahead. 
# % n (modulus operation) ensures that the position wraps around to the beginning 
# of the list if it exceeds the list length. For example, if the list has 8 elements and you move
# to position 9, % n will wrap it to position 1.
# energy -= 1  # Lose 1 unit of energy for the jump
# This condition checks if the current position i is 0, meaning you have returned to the starting position.
# If i == 0 is True, the loop breaks, stopping further jumps.

"""
Note: The while loop is used instead of a for loop because the number of iterations 
needed to return to the starting position is not known in advance. 
The while loop allows the program to continue jumping until the condition 
of returning to the start is met, making it well-suited for the problem's circular nature. 
In contrast, a for loop would require a predefined iteration count 
and additional logic to break when the condition is met, complicating the code unnecessarily.
"""


#*********** Logic -2 ***************
"""
def jumpingOnClouds(c, k):
    energy_level = 100
    i = 0
    while True:
        energy_level -= 1
        if c[(i+k)% n] == 1:
            energy_level -= 2
        if (i+k) % n == 0:
            break
        i += k
    return energy_level
"""

#*********** Logic -3 ***************
"""
def jumpingOnClouds(c: [int], k: int) -> int:
    e = 100
    n = len(c)
    i = k % n
    while i != 0:
        e -= 1 + 2 * c[i]
        i = (i + k) % n
    e -= 1 + 2 * c[i]
    return e
"""

#*********** Logic -4 ***************
"""
def jumpingOnClouds(c, k):
    return 100-sum(3 if c[i%n] else 1 for i in range(0, math.lcm(n, k), k))
"""

#*********** Logic -5 ***************
"""
def jumpingOnClouds(c, k, pos=0, energy=100):
    while True:
        pos = (pos + k) % len(c)
        energy -= 1 if c[pos] == 0 else 3
        if pos == 0:
            break
    return energy
"""

#*********** Logic -6 ***************
"""
def jumpingOnClouds(c, k, pos=0, energy=100):
    playing = True
    clouds = len(c)
    while playing:
        pos = (pos + k) % clouds
        energy -= 1 if c[pos] == 0 else 3
        playing = False if pos == 0 else True
    return energy
"""

