#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    #*********** IZHAR CODE *****************

    result = s[:-2]
    if s[-2:] == 'AM':
        if s[:2] == '12':
            result = '00' + s[2:-2]
        return result
        
    if s[-2:] == 'PM':
        if s[:2] != '12':
            result = str(12 + int(s[:2])) + s[2:-2]
        return result

    return result


    #*********** IZHAR CODE *****************


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
