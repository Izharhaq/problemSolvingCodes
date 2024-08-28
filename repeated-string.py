"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    #*********** IZHAR CODE **********
    repeatation = n//len(s)
    remainder = n - (repeatation*len(s))
    
    remainder = s[:remainder].count("a")
    res = s.count("a") * repeatation
    
    return res + remainder

    #********** IZHAR CODE **********

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

"""

# s = input()
# n = int(input().strip())

s = "abaabc"
n = 100

def repeatedString(s, n):
    repeatation = n//len(s)
    remainder = n - (repeatation*len(s))
    
    remainder = s[:remainder].count("a")
    res = s.count("a") * repeatation
    
    # return res + remainder
    print(res+remainder)

    
repeatedString(s, n)

"""
1. check if len(s)==n ->> If yes , No need to define and read pattern
2.                          If No, read and define the pattern
"""


"""
def repeatedString(s, n):
    repeatation = n//len(s)
    remainder = n - (repeatation*len(s))
    
    reminder = s[:remainder].count("a")
    res = s.count("a") * repeatation
    
    return res + remainder
"""

"""
def repeatedString(s,n):
    return (s.count("a") * (n // len(s))) + s[:n%len(s)].count("a")
"""


"""
def repeatedString(s, n): 
    # Write your code here 
    count_a_in_s = s.count('a')

    full_repeats = n // len(s)

    total_a_in_full_repeats = full_repeats * count_a_in_s

    remainder = n % len(s)

    total_a_in_remainder = 0
    for i in range(remainder):
        if s[i] == 'a':
            total_a_in_remainder += 1

    total_a = total_a_in_full_repeats + total_a_in_remainder

    return total_a
"""

"""
def repeated_string(s, n):
    return s.count('a') * (n//len(s)) + s[:n%len(s)].count('a')
"""