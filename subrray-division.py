"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    #***** IZHAR CODE *************
    count = 0
    n = len(s)
    
    for i in range(n - m + 1):
        if sum(s[i:i + m]) == d:
            count += 1
    
    return count



    #***** IZHAR CODE *************

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()

"""
# n = int(input().strip())
# s = list(map(int, input().rstrip().split()))
# first_multiple_input = input().rstrip().split()
# d = int(first_multiple_input[0])
# m = int(first_multiple_input[1])
"""
"""

# s = [1, 2, 1, 3, 2]
# d = 4,
# m = 2

n = int(input().strip())
s = list(map(int, input().rstrip().split()))
first_multiple_input = input().rstrip().split()
d = int(first_multiple_input[0])
m = int(first_multiple_input[1])


def birthday(s, d, m):
    # Write your code here
    
    count = 0
    n = len(s)
    
    for i in range(n - m + 1):
        if sum(s[i:i + m]) == d:
            count += 1
    
    return count
    # print(count)
birthday(s, d, m)


# birthday(s, d, m)