"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m
#

def chocolateFeast(n, c, m):
    # Write your code here
    #*********** IZHAR CODE *********
    chocolates = n // c
    wrappers = chocolates
    while wrappers >= m:
        extra_chocolates = wrappers // m
        chocolates += extra_chocolates
        wrappers = wrappers % m + extra_chocolates
    
    return chocolates

    #********* IZHAR CODE ***********

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()

"""

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
c = int(first_multiple_input[1])
m = int(first_multiple_input[2])
def chocolate_feast(n, c, m):
    # Initial chocolates purchased
    chocolates = n // c
    wrappers = chocolates

    # Exchange wrappers for more chocolates
    while wrappers >= m:
        # Number of chocolates we can get by exchanging wrappers
        extra_chocolates = wrappers // m
        chocolates += extra_chocolates
        # Calculate new wrappers after the exchange
        wrappers = wrappers % m + extra_chocolates
    
    return chocolates

print(chocolate_feast(n, c, m))


"""
def chocolateFeast(n, c, m):
    chocolateBars = n // c
    return chocolateBars + (chocolateBars - 1) // (m - 1)
"""

"""
def chocolateFeast(n, c, m):
    total = wrappers = n//c
    while x := wrappers//m:
        wrappers -= x * (m-1)
        total += x
    return total
"""


"""
def chocolateFeast(n, c, m):
    total = n // c
    wrappers = total
    while wrappers // m > 0:
        total += wrappers // m 
        wrappers = (wrappers // m) + (wrappers % m)
    return total
"""




