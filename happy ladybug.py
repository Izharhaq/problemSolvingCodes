"""
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    # Write your code here
    #********* Izhar Code *******
    
    freq = [0] * 26  # For A to Z
    has_empty = False

    for ch in b:
        if ch == '_':
            has_empty = True
        else:
            freq[ord(ch) - ord('A')] += 1

    # If no '_' is present, check if all are already happy
    if not has_empty:
        for i in range(len(b)):
            if (i > 0 and b[i] == b[i - 1]) or (i < len(b) - 1 and b[i] == b[i + 1]):
                continue
            return "NO"
        return "YES"

    # If '_' is present, ensure no letter occurs only once
    for count in freq:
        if count == 1:
            return "NO"

    return "YES"
          

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()

"""

"""
####****** In this solution a test case was getting failed **********

from collections import Counter

def happyLadybugs(b):
    # If no '_' then check if already happy
    if '_' not in b:
        for i in range(1, len(b)-1):
            if b[i] != b[i-1] and b[i] != b[i+1]:
                return "NO"
        if b[0] != b[1] or b[-1] != b[-2]:  # Check first and last separately
            return "NO"
        return "YES"

    # Count frequency of each character
    count = Counter(b)

    # Check if there's any ladybug with only 1 occurrence
    for key in count:
        if key != '_' and count[key] == 1:
            return "NO"

    return "YES"

"""


"""
def happyLadybugs(b):
    freq = [0] * 26  # For A to Z
    has_empty = False

    for ch in b:
        if ch == '_':
            has_empty = True
        else:
            freq[ord(ch) - ord('A')] += 1

    # If no '_' is present, check if all are already happy
    if not has_empty:
        for i in range(len(b)):
            if (i > 0 and b[i] == b[i - 1]) or (i < len(b) - 1 and b[i] == b[i + 1]):
                continue
            return "NO"
        return "YES"

    # If '_' is present, ensure no letter occurs only once
    for count in freq:
        if count == 1:
            return "NO"

    return "YES"


"""