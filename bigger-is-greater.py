"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Write your code here
    #**** Izhar Code *************
    
    w = list(w)
    i = len(w) - 1

    # Step 1: Find non-increasing suffix
    while i > 0 and w[i - 1] >= w[i]:
        i -= 1
    if i == 0:
        return "no answer"

    # Step 2: Find rightmost successor to pivot
    j = len(w) - 1
    while w[j] <= w[i - 1]:
        j -= 1

    # Step 3: Swap pivot with successor
    w[i - 1], w[j] = w[j], w[i - 1]

    # Step 4: Reverse the suffix
    w[i:] = reversed(w[i:])

    return ''.join(w)

    #**** Izhar Code *************
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()

"""