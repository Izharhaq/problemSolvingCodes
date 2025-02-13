"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    #****** IZHAR CODE **********
    color_dic={} 
    count=0 
    for i in ar: 
        if i in color_dic.keys(): 
            color_dic[i]+=1 
        else: 
            color_dic[i]=1
    for i in color_dic: 
        count+=color_dic[i]//2
        return count

    #***** IZHAR CODE ***********

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

"""