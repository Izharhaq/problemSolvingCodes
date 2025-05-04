"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

"""

#********** This was submitted ***********
"""
def maxSubarray(arr):
    # Write your code here
    maxx=0
    x=summ=arr[0] if arr[0]>0 else 0
    h=arr[0]
    for i in range(1,len(arr)):
        h=max(h,arr[i])
        summ+=arr[i] if arr[i]>0 else 0
        x=arr[i] if x<0 else x+arr[i]
        maxx=max(maxx,x)
        
    return [maxx,summ] if maxx!=0 else [h,h] 
"""

"""
def a(arr):
    r=min(0,max(arr))
    for e in arr:
        if e>0:
            r+=e
    return r
def s(arr):
    l=[arr[0],arr[0]]
    for i in range(1,len(arr)):
        l[0]=max(arr[i],arr[i]+l[0])
        l[1]=max(l[1],l[0])
    return max(l)
    
def maxSubarray(arr):
    return s(arr),a(arr)
"""





"""
def maxSubarray(arr):
    n=len(arr)
    dp=[[0]*n for _ in range(2)]
    dp[0][0]=arr[0]
    dp[1][0]=arr[0]
    for i in range(1,n):
        dp[0][i]=max(dp[0][i-1]+arr[i],arr[i])
        dp[1][i]=max(max(dp[1][i-1],dp[1][i-1]+arr[i]),arr[i])
    return [max(dp[0]),dp[1][-1]]
"""



"""
def maxSubarray(arr):
    curSum = -sys.maxsize
    maxSum = -sys.maxsize
    m1 = -sys.maxsize
    posNums = 0
    
    for num in arr:
        ## curSum is the maximum of our current sum or the number
        ## e.g. if our current sum is -5, and the next num is 2, it is best to start over
        curSum = max(num, curSum + num)
        ## maxsum is just the max of the current sum and previous max
        maxSum = max(maxSum, curSum)
        
        ## we track all positive numbers and the smallest non-positive integer
        ## if we have no positive integers, our largest subsequence is just the 
        ## smallest non-positive integer
        if num > 0:
            posNums += num
        elif num >= m1:
            m1 = num
       
    
    if posNums == 0:
        return [maxSum, m1]
    else:
        return [maxSum, posNums]
"""