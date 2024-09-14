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



n = int(input().strip())
ar = list(map(int, input().rstrip().split()))
def sockMerchant(n, ar): 
    # Write your code here
    # Here we need key value pair so we use dict.
    color_dic={} 
    count=0 
    for i in ar: 
        if i in color_dic.keys(): 
            color_dic[i]+=1 
        else: 
            color_dic[i]=1
    for i in color_dic: 
        count+=color_dic[i]//2
    print(count)
    # return count
    
sockMerchant(n, ar)




#*********** Logic-2 ************
"""
import math
n = int(input().strip())
ar = list(map(int, input().rstrip().split()))

def sockMerchant(n, ar):
    hashmap = dict()
    pairs = 0
    for sock in ar:
        if sock in hashmap:
            hashmap[sock] +=1
        else:
            hashmap[sock] = 1
    for key in hashmap.keys():
        pairs += math.floor(hashmap[key]/2)

    # return int(pairs)
    print(int(pairs))
sockMerchant(n, ar)
"""



##********** Logic -3 **********

"""
n = int(input().strip())
ar = list(map(int, input().rstrip().split()))

def sockMerchant(n, ar):
    total = 0
    ar.sort()
    dic = {}
    for i in ar:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in dic.values():
        total += i // 2
    # return total
    print(total)
sockMerchant(n, ar)
"""

###****** APPROACHES ************