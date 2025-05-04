"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#

def twoPluses(grid):
    # Write your code here
    n = len(grid)
    m = len(grid[0])
    # getting the list of coordinates of all good cells
    goodcells = [(r, c) for r in range(n) for c in range(m) if grid[r][c] == 'G']
    # initialize the list of crosses of single cells
    pluses = [{cell} for cell in goodcells]
    # finding the larger crosses
    for r, c in goodcells:
        if 0 < r < n and 0 < c < m:
            for i in range(1, min(r, c, n - r - 1, m - c - 1) + 1):
                four_cells = [(r + i, c), (r - i, c), (r, c - i), (r, c + i)]
                if all(cell in goodcells for cell in four_cells):
                    h_line = set((r, x) for x in range(c - i, c + i + 1))
                    v_line = set((y, c) for y in range(r - i, r + i + 1))
                    pluses.append(h_line | v_line)
                else:
                    break
    pluses = sorted(pluses, key = len, reverse = True)
    max_2 = 0
    while len(pluses) > 1:
        plus_a = pluses.pop(0)
        for plus_b in pluses:
            if plus_a.isdisjoint(plus_b):
                max_2 = max(max_2, len(plus_a) * len(plus_b))
                break
    return max_2
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()

"""

"""
def twoPluses(grid):
    n = len(grid)
    m = len(grid[0])
    # getting the list of coordinates of all good cells
    goodcells = [(r, c) for r in range(n) for c in range(m) if grid[r][c] == 'G']
    # initialize the list of crosses of single cells
    pluses = [{cell} for cell in goodcells]
    # finding the larger crosses
    for r, c in goodcells:
        if 0 < r < n and 0 < c < m:
            for i in range(1, min(r, c, n - r - 1, m - c - 1) + 1):
                four_cells = [(r + i, c), (r - i, c), (r, c - i), (r, c + i)]
                if all(cell in goodcells for cell in four_cells):
                    h_line = set((r, x) for x in range(c - i, c + i + 1))
                    v_line = set((y, c) for y in range(r - i, r + i + 1))
                    pluses.append(h_line | v_line)
                else:
                    break
    pluses = sorted(pluses, key = len, reverse = True)
    max_2 = 0
    while len(pluses) > 1:
        plus_a = pluses.pop(0)
        for plus_b in pluses:
            if plus_a.isdisjoint(plus_b):
                max_2 = max(max_2, len(plus_a) * len(plus_b))
                break
    return max_2
"""