#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    #*********** IZHAR CODE *****************
    for i in range(n):
        # Print the required number of spaces
        for j in range(n - i - 1):
            print(' ', end='')
        # Print the required number of hashes
        for k in range(i + 1):
            print('#', end='')
        # Move to the next line after each level
        print()


    #*********** IZHAR CODE *****************

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
