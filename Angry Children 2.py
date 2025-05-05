"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'angryChildren' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY packets
#

def angryChildren(k, packets):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    packets = []

    for _ in range(n):
        packets_item = int(input().strip())
        packets.append(packets_item)

    result = angryChildren(k, packets)

    fptr.write(str(result) + '\n')

    fptr.close()

"""


"""
def angryChildren(k, a):
    a.sort()
    n = len(a)
    s = -a[0]
    d = 0
    for i in range(k):
        s += a[i]
        d += (2*i-k+1)*a[i]
    ans = d
    for shift in range(1,n-k):
        d += (- 2*s + (k-1)*(a[shift-1]+a[shift+k-1]))
        s += (a[shift+k-1]-a[shift])
        ans = min(ans,d)
    return ans
"""