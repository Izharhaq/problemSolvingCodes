
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    # ************ IZHAR CODE ***********
    count_apples = 0
    count_oranges = 0

    for num in apples:
        apple_dist = num + a
        if s <= apple_dist <= t:
            count_apples += 1

    for num in oranges:
        orange_dist = num + b
        if s <= orange_dist <= t:
            count_oranges += 1

    print(f"{count_apples}\n{count_oranges}")



    # ************ IZHAR CODE ***********

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

"""


########Code -1 tested locally *********

"""
first_multiple_input = input().split()
s = int(first_multiple_input[0])
t = int(first_multiple_input[1])

second_multiple_input = input().split()
a = int(second_multiple_input[0])
b = int(second_multiple_input[1])

third_multiple_input = input().split()
m = int(third_multiple_input[0])
n = int(third_multiple_input[1])

apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))

def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apples = 0
    count_oranges = 0

    for num in apples:
        apple_dist = num + a
        if s <= apple_dist <= t:
            count_apples += 1

    for num in oranges:
        orange_dist = num + b
        if s <= orange_dist <= t:
            count_oranges += 1

    print(f"{count_apples}\n{count_oranges}")

countApplesAndOranges(s, t, a, b, apples, oranges)

"""

####### Code-2 tested locally *********

"""
def countApplesAndOranges(s, t, a, b, apples, oranges):
    c_a = 0
    c_o = 0
    for num in apples:
        if s <= num+a <=t:
            c_a += 1
    for num in oranges:
        if s <= num+b <=t:
            c_o += 1
    print(c_a)
    print(c_o)
countApplesAndOranges(s, t, a, b, apples, oranges)
"""