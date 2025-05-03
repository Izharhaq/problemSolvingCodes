"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    #********* Izhar code ****

    result = []
    for n in range(p, q + 1):
        d = len(str(n))
        square = str(n ** 2)
        right = int(square[-d:]) if square[-d:] else 0
        left = int(square[:-d]) if square[:-d] else 0
        if left + right == n:
            result.append(str(n))

    if result:
        print(' '.join(result))
    else:
        print("INVALID RANGE")

    #****** Izhar Code ************88    

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)

"""