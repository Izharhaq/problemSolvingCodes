"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

def matrixRotation(matrix, r):
    # Write your code here
    m = len(matrix)
    n = len(matrix[0])
    d = dict() # storing matrix coordinates and their values
    for i in range(min(m, n) // 2):
        # storing the coordinates for each loop or layer of the matrix
        loop = [(i, j) for j in range(i, n - i)] # top side
        loop += [(j, n - i - 1) for j in range(i + 1, m - i)] # right side
        loop += [(m - i - 1, j) for j in range(n - i - 2, i - 1 , -1)] # bottom side
        loop += [(j, i) for j in range(m - i - 2, i , -1)] # left side
        # listing the values of each loop of the matrix, then shift to mimic the effect of rotation
        loop_values = [matrix[r][c] for r, c in loop]
        rotated_values = loop_values[r % len(loop_values):] + loop_values[: r % len(loop_values)]
        # storing the new values of every position of the loop to respective coordinates
        for k in range(len(loop)):
            d[loop[k]] = rotated_values[k]
    # print out the resultant matrix
    for r in range(m):
        line = [d[(r, c)] for c in range(n)]
        print(*line)
    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)

"""

