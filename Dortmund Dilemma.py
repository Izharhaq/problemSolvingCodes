#********* NEED TO WORK ON THIS PROBLEM ***********88

"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dortmundDilemma' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def dortmundDilemma(n, k):
    # Write your code here
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = dortmundDilemma(n, k)

        fptr.write(str(result) + '\n')

    fptr.close()

"""

"""
MOD = 10**9 + 9
MAX_N = 100001
MAX_K = 27

# Precompute binomial coefficients C[n][k] = n choose k
C = [[0] * MAX_K for _ in range(MAX_K)]
for i in range(MAX_K):
    C[i][0] = C[i][i] = 1
    for j in range(1, i):
        C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD

# Precompute f[n][k]: number of strings of length n over k letters with no proper prefix equal to a proper suffix
f = [[0] * MAX_K for _ in range(MAX_N)]
for k in range(1, MAX_K):
    f[1][k] = k
    for n in range(2, MAX_N):
        if n % 2 == 1:
            f[n][k] = (f[n - 1][k] * k) % MOD
        else:
            f[n][k] = (f[n - 1][k] * k - f[n // 2][k] + MOD) % MOD

# Precompute total_strings[n][k] = k^n
total_strings = [[0] * MAX_K for _ in range(MAX_N)]
for k in range(1, MAX_K):
    total_strings[1][k] = k
    for n in range(2, MAX_N):
        total_strings[n][k] = (total_strings[n - 1][k] * k) % MOD

# Precompute result[n][k] = total_strings[n][k] - f[n][k]
result = [[0] * MAX_K for _ in range(MAX_N)]
for n in range(1, MAX_N):
    for k in range(1, MAX_K):
        res = (total_strings[n][k] - f[n][k] + MOD) % MOD
        # Inclusion-Exclusion to ensure exactly k distinct letters
        for j in range(1, k):
            res = (res - result[n][j] * C[k][j]) % MOD
        result[n][k] = res

# Function to compute the final answer
def dortmund_dilemma(N, K):
    return (result[N][K] * C[26][K]) % MOD

# Example usage:
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    print(dortmund_dilemma(N, K))

"""


