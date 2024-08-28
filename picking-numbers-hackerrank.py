"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a.sort()
    max_length = 0
    for i in range(len(a)):
        current_subarray = [a[i]]
        for j in range(i+1, len(a)):
            if abs(a[j] - a[i]) <= 1:
            
                current_subarray.append(a[i])
            else:
                break

        max_length = max(max_length, len(current_subarray))
    return max_length

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

"""




