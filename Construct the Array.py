"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countArray' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER x
#
NUM = 10**9+7
def countArray(n, k, x):
    # Return the number of ways to fill in the array.
    dp = [[0 for _ in range(2)] for _ in range(n+1)]
    
    # dp[length][ends in x]
    
    dp[2][0] = k - 2 if x != 1 else k - 1
    dp[2][1] = 1 if x != 1 else 0
    
    for i in range(3, n+1):
        dp[i][0] = ((((k-2) % NUM) * (dp[i-1][0] % NUM)) % NUM + (((k-1) % NUM) * (dp[i-1][1] % NUM)) % NUM) % NUM
        dp[i][1] = dp[i-1][0] % NUM
    
    return dp[n][1] % NUM

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = int(first_multiple_input[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()

"""


"""
NUM = 10**9+7

def countArray(n, k, x):
    dp = [[0 for _ in range(2)] for _ in range(n+1)]
    
    # dp[length][ends in x]
    
    dp[2][0] = k - 2 if x != 1 else k - 1
    dp[2][1] = 1 if x != 1 else 0
    
    for i in range(3, n+1):
        dp[i][0] = ((((k-2) % NUM) * (dp[i-1][0] % NUM)) % NUM + (((k-1) % NUM) * (dp[i-1][1] % NUM)) % NUM) % NUM
        dp[i][1] = dp[i-1][0] % NUM
    
    return dp[n][1] % NUM
"""