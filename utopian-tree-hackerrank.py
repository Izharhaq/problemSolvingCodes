"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    #******** IZHAR CODE ********
    height = 1
    for p in range(1, n+1):
        if p % 2 == 0:
            height += 1
        else:
            height *= 2

    return height

    #******** IZHAR CODE ********

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()

"""


#************logic-1 ********** Working fine*********
"""
t = int(input().strip())
for t_itr in range(t):
    n = int(input().strip())
def utopianTree(n):
    height = 1
    for p in range(1, n+1):
        if p % 2 == 0:
            height += 1
        else:
            height *= 2

    # return height
    print(height)

utopianTree(n)
"""

#***********logic-2***********Working fine********
"""
t = int(input().strip())
for t_itr in range(t):
    n = int(input().strip())
def utopianTree(n):
    count=0 
    for i in range(n+1): 
        if i==0: 
            count+=1 
        elif i%2==0 or i==1: 
            count+=1 
        elif i%2==1: 
            count*=2
    # return count
    print(count)
utopianTree(n)
"""


#************ Logic-3 ************working fine *********8
"""
t = int(input().strip())
for t_itr in range(t):
    n = int(input().strip())
def utopianTree(n):
    height = 1
    for p in range(1, n+1):
        if p % 2 == 0:
            height += 1
        else:
            height *= 2

    return height
"""

#************ Logic-4 **********Working fine *******
"""
t = int(input().strip())
for t_itr in range(t):
    n = int(input().strip())
def utopianTree(n):
    height = 0
    for i in range(n+1):
        if i == 0:
            height += 1
        elif i%2==0 or i==1:
            height += 1
        elif i%2==1:
            height *= 2 
    # return height    
    print(height)

utopianTree(n)
"""









