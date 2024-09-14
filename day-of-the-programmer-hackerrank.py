"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    # ****** IZHAR CODE *************
    if 1700 <= year <= 1917:
        if year%4==0:
            return f"12.09.{year}"
        else :
            return f"13.09.{year}"

    elif year == 1918: 
        return "26.09.1918"

    elif year > 1918:
        if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"




    # ****** IZHAR CODE *************

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

"""


# This program is under development ******
# Theme - Day of the programmer

year = int(input().strip())
def dayOfProgrammer(year):
    if 1700 <= year <= 1917: # Julian Calender
        if year%4==0:
            # print(f"12.09.{year}")
            return f"12.09.{year}"
        else :
            # print(f"13.09.{year}")
            return f"13.09.{year}"

    elif year == 1918:      # Gregarion Calender
        # print("26.09.1918")
        return "26.09.1918"

    elif year > 1918:       # Gregarion Calender
        if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
            print(f"12.09.{year}")
            return f"12.09.{year}"
        else:
            print(f"13.09.{year}")
            return f"13.09.{year}"
        
dayOfProgrammer(year)

# Need to check leap year
"""
def is_leap(year): 
    leap = False 
    if (year%4 == 0 and year%100 != 0) or (year%400 == 0): 
        return True 
    else: 
        return leap 
year = int(input()) 
print(is_leap(year))
"""

 