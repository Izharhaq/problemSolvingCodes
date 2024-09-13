"""
Problem Description:
You are given a range of days, and for each day, you need to determine whether it's a "beautiful day." 
A day is considered "beautiful" if the absolute difference between the day and 
its reverse is divisible by a given integer k.

Input:
A starting day i
An ending day j
A divisor k

Output:
The number of "beautiful days" in the given range [i, j].

Steps to Solve:
1. Reverse the number: For each day between i and j (inclusive), 
   reverse the digits of the day. For example, if the day is 123, the reverse is 321.

2. Calculate the difference: Compute the absolute difference between the original day and its reverse.

3. Check divisibility: Check if the absolute difference is divisible by k. If yes, it's a "beautiful day."

4. Count the number of beautiful days: Keep track of how many days satisfy the condition.
"""


##****************** Solution *****************
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    # Write your code here
    #******** IZHAR CODE **********
    beautiful_days = 0
    for number in range(i, j+1):
        reverse = int(str(number)[::-1])
        
        if abs(number - reverse) % k == 0:
            beautiful_days += 1
            
    return beautiful_days

    #********* IZHAR CODE***********

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()

"""
###****************************************************

first_multiple_input = input().rstrip().split()
i = int(first_multiple_input[0])
j = int(first_multiple_input[1])
k = int(first_multiple_input[2])

def beautifulDays(i, j, k):
    beautiful_days = 0
    for number in range(i, j+1):
        reverse = int(str(number)[::-1])
        
        if abs(number - reverse) % k == 0:
            beautiful_days += 1
            
    # return beautiful_days
    print(beautiful_days)

beautifulDays(i, j, k)




##********* logic-2 *****************
"""

def beautifulDays(i, j, k):
    beautiful_days = 0
    for number in range(i, j+1):
        reverse = int(str(number)[::-1])
        
        if abs(number - reverse) % k == 0:
            beautiful_days += 1
            
    return beautiful_days
"""

#************* logic-3 *****************

"""
def beautifulDays(i, j, k): 
    l=[] 
    for i in range(i,j+1): 
        l.append(i) 
    q=[] 
    for j in range(len(l)): 
    n=l[j] 
    b=str(n) 
    c=b[::-1] 
    d=int(c) 
    ans=(n-d)/k 
    q.append(ans) 
    count=0 
    for k in q: 
        if k%1==0: 
            count+=1 
    return count
"""

#*****************logic-4*******************
"""
def beautifulDays(i, j, k):
    li = []
    b = []
    count = 0
    for a in range(i,j+1):
        b.append(a)
        a = str(a)
        a = a[::-1]
        li.append(int(a))
    for i in range(len(li)):
        if (li[i]-b[i])/k == (li[i]-b[i])//k:
            count+=1
    return count
"""

#************** logic-5*****************
"""
def reverse_number(number):
    n = number
    reverse = 0
    while n>0:
        t = n %10
        reverse = reverse*10 + t
        n = n//10
    return reverse


        
def beautifulDays(i, j, k):
    count = 0
    for t in range(i , j+1):
        reverse = reverse_number(t)
        if abs(t-reverse) % k == 0:
            count += 1
        else:
            continue
    return count
"""