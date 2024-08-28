#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superFunctionalStrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def superFunctionalStrings(s):
    # Write your code here
    pass
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = superFunctionalStrings(s)

        fptr.write(str(result) + '\n')

    fptr.close()
