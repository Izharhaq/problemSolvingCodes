"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()

"""

"""
def minimumDistances(a):
    x = len(a)
    mindist = 1000
    for i in range(0, x-1, 1):
        for j in range(i+1, x, 1):
            if a[i] == a[j] and abs(i-j) < mindist:
                mindist = abs(i-j)
    if mindist == 1000:
        return -1
    else:
        return mindist
"""

"""
def minimumDistances(a):
    result = -1
    for id_i, i in enumerate(a[:-1]):
        for id_j, j in enumerate(a[(id_i+1):]):
           if j == i:
                r = id_j + 1
                if result == -1 or r < result:
                    result = r
    return result
"""


"""
from itertools import combinations

def calculate_distances(arr):
    if len(arr) == 1:
        return -1
    return min([abs(x[0] - x[1]) for x in list(combinations(arr, 2))])
    
def minimumDistances(a):
    mapping = {}
    for i, val in enumerate(a):
        if val not in mapping.keys():
            mapping[val] = [i]
        else:
            mapping[val] += [i]
    distances = [calculate_distances(val) for _, val in mapping.items()]
    valid = [x for x in distances if x != -1]
    return min(valid) if len(valid) > 0 else -1
"""

"""
def minimumDistances(a):
    uniqueItems = set(a)
    minDistance = -1
    for item in uniqueItems:
        calc = []
        for index,item2 in enumerate(a):
            if (item2 == item):
                calc.append(index)
        if len(calc) == 1:
            continue
        else:
            distance = calc[1] - calc[0]
            if minDistance == -1:
                minDistance = distance
            elif distance < minDistance:
                minDistance = distance    
			return minDistance
"""