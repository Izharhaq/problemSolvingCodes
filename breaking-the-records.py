"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    #******* IZHAR CODE ***********
    min_initial=scores[0]
    max_initial=scores[0]
    max_count=0
    min_count=0
    n = len(scores)
    for i in range(n):
        if (scores[i]>max_initial):
            max_initial=scores[i]
            max_count+=1
        elif (scores[i]<min_initial):
            min_initial=scores[i]
            min_count+=1
    return [max_count, min_count]



    #******* IZHAR CODE ***********

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

"""
n = int(input().strip())
scores = list(map(int, input().rstrip().split()))

def breakingRecords(scores):
    min_initial=scores[0]
    max_initial=scores[0]
    max_count=0
    min_count=0
    n = len(scores)
    for i in range(n):
        if (scores[i]>max_initial):
            max_initial=scores[i]
            max_count+=1
        elif (scores[i]<min_initial):
            min_initial=scores[i]
            min_count+=1
    return [max_count, min_count]
    # print(max_count, min_count)
breakingRecords(scores)



"""
"""