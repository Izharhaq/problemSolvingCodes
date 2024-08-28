"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'howManyGames' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s
#

def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    #*********** IZHAR CODE ***************
    count = 0
    while s >= p:
        s -= p
        count += 1
        p = max(p - d, m)
    return count

    #*********** IZHAR CODE ***************

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()

"""
first_multiple_input = input().rstrip().split()
p = int(first_multiple_input[0])
d = int(first_multiple_input[1])
m = int(first_multiple_input[2])
s = int(first_multiple_input[3])

def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    count = 0
    while s >= p:
        s -= p
        count += 1
        p = max(p - d, m)
    # return count
    print(count)

howManyGames(p, d, m, s)


"""
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    count = 0
    price = p
    while s >= price:
        s = s - price
        price -= d
        if price < m:
            price = m
        count += 1
    return count
"""

"""
def howManyGames(p, d, m, s):
    total = 0
    count = 0
    while total + p <= s:
        total += p
        count +=1
        if p - d >= m:
            p -= d
        else:
            p = m
    return count
"""