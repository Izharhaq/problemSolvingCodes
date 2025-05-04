#********** Problem Statement *************
"""
ASDFGH
"""

#************ Solution *******************
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    # Write your code here
    #********* IZHAR CODE ***********


    #******** IZHAR CODE ************

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

"""


"""
def workbook(n, k, arr):
    m=1
    n=1
    o=0
    acc=0
    while (o != len(arr)):
        le = min(m+k-1, arr[o])
        if (m <= n and n <= le):
            acc+=1
        m = le + 1
        if (m > arr[o]):
            o+=1
            m=1
        n+=1
    return acc
"""


"""
def workbook(n, k, arr):
    m=1 #problem number pointer
    s=1 #pagepointer
    o=0 #array_index pointer
    acc=0 #accumelator
    while (True):
        if m == s:
            acc+=1
        if m == arr[o]:
            s+=1
            o+=1
            m=0
        s+= (1 if m % k ==0 and m!= 0 else 0)
        m+=1
        if o == len(arr):
            break
    return acc
"""


"""
def workbook(n, k, arr):
    at=0
    acc=0
    for el in arr:
        at+= 1
        for i in range(1, el+1):
            if (i-1) % k == 0 and (i-1) != 0:
                at+=1
            if i == at:
                acc+=1
    return acc
"""

"""
def work_book(n, k, arr):
    special_problems = 0
    current_page = 1

    for chapter in range(n):
        total_problems = arr[chapter]
        problem_number = 1

        while problem_number <= total_problems:
            # Calculate the last problem on the current page
            last_problem_on_page = min(problem_number + k - 1, total_problems)

            # Check if the current page contains a special problem
            if problem_number <= current_page <= last_problem_on_page:
                special_problems += 1

            # Move to the next page and update the problem number
            current_page += 1
            problem_number = last_problem_on_page + 1

    return special_problems
"""


