"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    # Write your code here
    nums = sorted(arr)
    if nums == arr:
        return "yes"
    swaps = []
    for i in range(len(arr)):
        if arr[i] != nums[i]:
            swaps.append(i+1)
    if len(swaps) == 2:
        print('yes')
        print('swap', swaps[0], swaps[1])
    else:
        if len(arr) > 2:
            reverse = [arr[i] for i in range(swaps[0]-1, swaps[-1])]
            if sorted(reverse) == reverse[::-1]:
                print('yes')
                print("reverse", swaps[0], swaps[-1])
            else:
                print("no")
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)


"""


"""
def almostSorted(arr):
    nums = sorted(arr)
    if nums == arr:
        return "yes"
    swaps = []
    for i in range(len(arr)):
        if arr[i] != nums[i]:
            swaps.append(i+1)
    if len(swaps) == 2:
        print('yes')
        print('swap', swaps[0], swaps[1])
    else:
        if len(arr) > 2:
            reverse = [arr[i] for i in range(swaps[0]-1, swaps[-1])]
            if sorted(reverse) == reverse[::-1]:
                print('yes')
                print("reverse", swaps[0], swaps[-1])
            else:
                print("no")
"""




