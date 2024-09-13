#***************** Problem ************
"""
Problem Description:
You are given an integer array arr and a number d. 
A "beautiful triplet" is defined as a tuple of indices (i, j, k) where:

i < j < k
arr[j] - arr[i] = d
arr[k] - arr[j] = d
In other words, the values at those indices form an arithmetic progression with 
a common difference d. Your task is to count how many such "beautiful triplets" exist in the array.

Input:
n: The number of elements in the array arr
d: The common difference
arr: The array of integers
Output:
An integer representing the number of beautiful triplets found in the array.
Steps to Solve:
Identify Triplets: A triplet consists of three values from the array such that 
the second value minus the first value equals d, and the third value minus the second value equals d. 
This implies:

arr[j] - arr[i] = d
arr[k] - arr[j] = d
In other words:

arr[k] = arr[j] + d
arr[j] = arr[i] + d
Loop Through the Array: For each element in the array, 
look for pairs that meet the conditions of a beautiful triplet.

Count Valid Triplets: Every time you find a valid triplet, increment a counter.
"""

#***************** Solution ************
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d, arr):
    # Write your code here
    #**********  IZHAR CODE ********
    counter = 0 
    n = len(arr) 
    for i in range(n): 
        for j in range(i, n): 
            if arr[j]-arr[i] == d: 
                for k in range(j, n): 
                    if arr[k]-arr[j] == d: 
                        counter += 1 
    return counter

    #********** IZHAR CODE ***********

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

"""

"""
def beautifulTriplets(d, arr):
    n = len(arr)
    count = 0
    for i in range(n):
        if (arr[i] + 2*d) <= arr[n-1]:
            if (arr[i] + d) in arr and (arr[i] + 2*d) in arr:
                count += 1
        else:
            break
    return count
"""

"""
def beautifulTriplets(d, arr):
    arr_map={}
    for n in arr:
        arr_map[n]=arr_map.get(n, 0)+1
    count=0
    for n in arr_map.keys():
        if n+d in arr_map and (n+2*d) in arr_map:
            count+=arr_map[n]*arr_map[n+d]*arr_map[n+2*d]
    return count
"""

"""
def beautifulTriplets(d, arr): 
    counter = 0 
    n = len(arr) 
    for i in range(n): 
        for j in range(i, n): 
            if arr[j]-arr[i] == d: 
                for k in range(j, n): 
                    if arr[k]-arr[j] == d: 
                        counter += 1 
    return counter
"""