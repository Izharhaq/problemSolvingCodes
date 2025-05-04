"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def absolutePermutation(n, k):
    # Write your code here
    res = []
    used = set()
    for index in range(1, n + 1):
        lower_option = index - k
        upper_option = index + k
        if lower_option > 0 and lower_option not in used:
            res.append(lower_option)
            used.add(lower_option)
        elif upper_option <= n and upper_option not in used:
            res.append(upper_option)
            used.add(upper_option)
        else:
            return [-1]
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

"""

"""
def absolutePermutation(n, k):
    res = []
    used = set()
    for index in range(1, n + 1):
        lower_option = index - k
        upper_option = index + k
        if lower_option > 0 and lower_option not in used:
            res.append(lower_option)
            used.add(lower_option)
        elif upper_option <= n and upper_option not in used:
            res.append(upper_option)
            used.add(upper_option)
        else:
            return [-1]
    return res

"""