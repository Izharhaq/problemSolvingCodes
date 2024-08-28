### Submitted on Hackerrank *********

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    #********* IZHAR CODE **********
    birdsid_count = {}
    for i in arr:
        if i in birdsid_count:
            birdsid_count[i] += 1
        else:
            birdsid_count[i] = 1
    max_ids = max(birdsid_count.values())
    max_items = [key for key, value in birdsid_count.items() if value == max_ids] 
    return min(max_items)
    
    #********* IZHAR CODE **********

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
