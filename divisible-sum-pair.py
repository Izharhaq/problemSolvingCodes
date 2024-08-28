"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    #******** IZHAR CODE ************
    count = 0
    m = len(ar)
    for i in range(m-1):
        for j in range(i+1, m):
            if (ar[i]+ar[j]) % k == 0:
                count += 1
    return count


    #******* IZHAR CODE *************

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

"""
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
ar = list(map(int, input().rstrip().split()))


def divisibleSumPairs(n, k, ar):
    count = 0
    m = len(ar)
    for i in range(m-1):
        for j in range(i+1, m):
            if (ar[i]+ar[j]) % k == 0:
                count += 1
    print(count)



divisibleSumPairs(n, k, ar)


"""
def divisibleSumPairs(n, k, arr):
    count = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if (arr[i]+arr[j]) % k == 0:
                count += 1
                
    return count
"""