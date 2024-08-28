"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    # Write your code here
    #***** IZHAR CODE ********
    frequency = {}
    for i in arr:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    max_freq = max(frequency.values())
    deletions = len(arr) - max_freq
    
    return deletions

    #****** IZHAR CODE *******

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

"""
n = int(input().strip())
arr = list(map(int, input().rstrip().split()))

def equalizeArray(arr):
    frequency = {}
    for i in arr:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    max_freq = max(frequency.values())
    deletions = len(arr) - max_freq
    
    # return deletions
    print(deletions)

equalizeArray(arr)


"""
def equalizeArray(arr):
    temp = list(set(arr))
    maxoccur = 0
    for item in temp:
        x = arr.count(item)
        if x > maxoccur:
            maxoccur = x
    return len(arr) - maxoccur
"""


"""
def equalizeArray(ar``r):
    f=[0]*(max(arr)+1)
    for i in range(len(arr)):
        f[arr[i]]+=1
    return len(arr)-max(f)
"""

"""
def equalizeArray(arr):
        min = len(arr)
        for num in arr:
                if min > len(arr) - arr.count(num):
                        min = len(arr) - arr.count(num)

        return min
"""

"""
def equalizeArray(arr):
    frq = [0] * 100
    for x in arr:
        frq[x - 1] += 1
    return len(arr) - max(frq)
"""


"""
def equalizeArray(arr):
    # Write your code here
    unique_elements = []
    frequencies = []
    
    for num in arr:
        if num in unique_elements:
            index = unique_elements.index(num)
            frequencies[index] += 1
        else:
            unique_elements.append(num)
            frequencies.append(1)
    
    max_frequency = -1
    for freq in frequencies:
        if freq > max_frequency:
            max_frequency = freq
    
    total_elements = len(arr)
    min_deletions = total_elements - max_frequency
    
    return min_deletions
"""





