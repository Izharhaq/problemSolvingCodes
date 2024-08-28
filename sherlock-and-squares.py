"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    # Write your code here
    #********* IZHAR CODE *************
    res = 0
    for i in range(int(a**0.5), int(b**0.5) + 1):
        if i*i>=a and i*i<=b:
            res += 1
    return res

    #******** IZHAR CODE ***************
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()

"""

first_multiple_input = input().rstrip().split()
a = int(first_multiple_input[0])
b = int(first_multiple_input[1])

def squares(a, b):
    res = 0
    for i in range(int(a**0.5), int(b**0.5) + 1):
        if i*i>=a and i*i<=b:
            res += 1
    return res
    # print(res)


squares(a, b+1)

#**************Logic-2***********************
"""
def squares(a, b):
    # Write your code here
    count = 0
    i = 0
    while (i**2 <= b):
        if i**2 >= a:
            count +=1
        else:
            pass
        i +=1
    return count
"""

#************** Logic-3 ***********************
"""
def squares(a, b):
    # Write your code here
    
    i = 1
    res = 0
    squ = 0
    while squ + i <= b:
        squ += i
        if squ >= a:
            res += 1
        i += 2
    return res
"""

#************** Logic-4 ***********************
"""
def squares(a, b):
    # Write your code here
    start = math.ceil(math.sqrt(a))
    end = math.floor(math.sqrt(b))
    return max(0, end - start + 1)
"""

"""
def squares(a, b):
    squares = 0
    i = int(math.sqrt(min(a, b)))
    while i*i <= max(a, b):
        if i*i >= min(a, b):
            squares += 1
        i += 1
    return squares  
"""

"""
return math.floor(math.sqrt(max(a, b))) - math.ceil(math.sqrt(min(a, b))) + 1
"""


"""
# Find the starting and ending square roots within the range
    start_sqrt = int(a ** 0.5)
    end_sqrt = int(b ** 0.5)
    
    # Count the square integers within the range
    count = end_sqrt - start_sqrt + 1 if start_sqrt ** 2 == a else end_sqrt - start_sqrt
    
    return count
"""

"""
def squares(a, b):
    i=math.ceil(math.sqrt(a))
    c=0
    while i*i<=b:
        c+=1
        i+=1
    return c
"""

"""
def squares(a, b):
    l = int(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1
    return l
"""
