#****** INCOMPLETE SOLUTION **********

"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    #****** IZHAR CODE **************
    def getTotalX(a, b):
    count = 0

    def is_factor(arr,x):
        for i in arr:
            if x % i != 0:
                return 0
        return 1

    def is_multiple(arr,x):
        for i in arr:
            if i % x != 0:
                return 0
        return 1

    for i in range(max(a),min(b)+1):
        if is_factor(a, i) and is_multiple(b, i):
            count+=1              
    return count



    #****** IZHAR CODE **************

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()


"""

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
arr = list(map(int, input().rstrip().split()))
brr = list(map(int, input().rstrip().split()))

def getTotalX(a, b):
    count = 0

    def is_factor(arr,x):
        for i in arr:
            if x % i != 0:
                return 0
        return 1

    def is_multiple(arr,x):
        for i in arr:
            if i % x != 0:
                return 0
        return 1

    for i in range(max(a),min(b)+1):
        if is_factor(a, i) and is_multiple(b, i):
            count+=1              
    return count


"""
def getTotalX(a, b):
    contador=0
    for i in range(1,101):
        first=all(i%num==0 for num in a)
        second=all(num%i==0 for num in b)
        if first and second:
            contador +=1
    return contador
"""
    
