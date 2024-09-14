"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    # Write your code here
    #******* IZHAR CODE ************
    words = 1
    for i in s:
        if i == i.upper():
            words += 1
    
    return count




    #******* IZHAR CODE ************

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()

"""

s = "pythonCodeProgramm"

def camelCase(s):
    words = 1
    for i in s:
        if i == i.upper():
            words += 1  
    # return words
    print(words)
camelCase(s)
"""
"""


"""
    def camelcase(s):
    c=0
    for i in range(0,len(s)):
        if i==0:
            c+=1
        if ord(s[i])>=65 and ord(s[i])<=90:
            c+=1
    return c
    """    

"""
    def camelcase(s):
    # Write your code here
    stack = []
    for i, char in enumerate(s):
        stack.append((char, i))
    
    word_count = {}
    
    while stack:
        char, idx = stack.pop()
        if char.isupper():
            word_count[idx] = word_count.get(idx, 0) + 1
    
    count = 1  
    for idx in word_count:
        count += word_count[idx]
    
    return count
    """


"""
def camelcase(s): 
        if len(s) == 0: 
            return 0 
        capitals = [c for c in s if 64 < ord(c) < 96] 
        return len(capitals) + 1 
"""    
