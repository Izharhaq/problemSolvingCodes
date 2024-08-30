"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'serviceLane' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY cases
#

def serviceLane(n, cases):
    # Write your code here
    #********** IZHAR CODE *********

    case = dict(enumerate(width))
    temp = max(width)
    results = []
    for i in cases:
        temp = max(width)
        for j in range(i[0], i[1]+1):
            if case[j] < temp:
                temp = case[j]
        results.append(temp)
    return results

    #************ IZHAR CODE ********


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

"""



first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
t = int(first_multiple_input[1])
width = list(map(int, input().rstrip().split()))
cases = []
for _ in range(t):
    cases.append(list(map(int, input().rstrip().split())))

def serviceLane(n, cases):
    # Write your code here
    case = dict(enumerate(width))
    temp = max(width)
    results = []
    for i in cases:
        temp = max(width)
        for j in range(i[0], i[1]+1):
            if case[j] < temp:
                temp = case[j]
        results.append(temp)
    return results

# print(serviceLane(n, cases))

"""
def serviceLane(n, cases):
    return [min(width[c[0]:c[1]+1]) for c in cases]
"""


"""
def serviceLane(n, cases):
    return list(map(min, map(lambda x: width[x[0]:x[1]+1], cases)))
"""

"""
def serviceLane(n, cases):
    return [min(width[i[0]:i[1]+1]) for i in cases]
"""

"""
def serviceLane(width, cases):
    # Write your code here
    case = dict(enumerate(width))
    temp = max(width)
    lst = []
    for i in cases:
        temp = max(width)
        for j in range(i[0], i[1]+1):
            if case[j] < temp:
                temp = case[j]
        lst.append(temp)
    return lst
"""



