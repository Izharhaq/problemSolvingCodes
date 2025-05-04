"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

def larrysArray(A):
    # Write your code here
    while len(A) > 2:
        smallest = A.index(min(A))
        if smallest % 2 == 0:
            A = [A[smallest]] + A[:smallest] + A[smallest + 1:]
        else:
            if smallest > 1:
                A = [A[0]] + [A[smallest]] + A[1:smallest] + A[smallest + 1:]
            A = A[1:3] + [A[0]] + A[3:]
        A.pop(0)
    return 'YES' if A[0] < A[1] else 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()


"""





"""
def larrysArray(A):
    while len(A) > 2:
        smallest = A.index(min(A))
        if smallest % 2 == 0:
            A = [A[smallest]] + A[:smallest] + A[smallest + 1:]
        else:
            if smallest > 1:
                A = [A[0]] + [A[smallest]] + A[1:smallest] + A[smallest + 1:]
            A = A[1:3] + [A[0]] + A[3:]
        A.pop(0)
    return 'YES' if A[0] < A[1] else 'NO'
"""