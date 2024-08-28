"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    #********* IZHAR CODE **********
    n = len(c)
    jumps = 0
    i = 0
    while i < n - 1:
        if i + 2 < n and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1
        
    return jumps

    #********* IZHAR CODE ***********

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

"""

n = int(input().strip())
c = list(map(int, input().rstrip().split()))
def jumpingOnClouds(c):
    n = len(c)
    jumps = 0
    i = 0
    
    while i < n - 1:
        # Try to jump 2 steps if it's within bounds and safe
        if i + 2 < n and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1
        
    # return jumps
    print(jumps)

jumpingOnClouds(c)


"""
def jumpingOnClouds(c):
    n = len(c)
    jumps = 0
    i = 0
    
    while i < n - 1:
        # Try to jump 2 steps if it's within bounds and safe
        if i + 2 < n and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1
        
    return jumps
"""


"""
def jumpingOnClouds(c):
    # Write your code here
    if len(c) == 1:
        return 0
    if len(c) == 2:
        return 1
    if c[2] != 1:
        return jumpingOnClouds(c[2:]) + 1
    else:
        return jumpingOnClouds(c[1:]) + 1

"""

"""
def jumpingOnClouds(c):
    # Write your code here
    if len(c) <= 1:
        return 0
    if c[0]:
        return math.inf
    return 1 + min(jumpingOnClouds(c[1:]), jumpingOnClouds(c[2:]))
"""

"""
def jumpingOnClouds(c):
    last_index=len(c)-1
    jumps=0
    index=0
    while  index < last_index:
      jumps+=1
      if index +2 <= last_index and c[index+2] == 0:
        index+=2
      else:
        index+=1
    return jumps
"""

