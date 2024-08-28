#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
# ********** IZHAR CODE ************
        new_array = sorted(arr)
    
        min_val = sum(new_array[:4])
        max_Val = sum(new_array[-4:])
    
        print(min_val,max_Val)



# ********** IZHAR CODE ************





if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
