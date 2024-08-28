"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    ####### IZHAR CODE **************
    if x2 > x1 and v2>= v1:
        return "NO"
    elif v1 == v2:
        if x1 == x2:
            return "YES"
        else:
            return "NO" 
    else:
        t = (x2 - x1) / (v1 - v2)                   # (x1 + v1.t = x2 +v2.t)
        if t >= 0 and t.is_integer():
            return "YES"
        else:
            return "NO"


    ###### IZHAR CODE ***************

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


"""
first_multiple_input = input().rstrip().split()

x1 = int(first_multiple_input[0])

v1 = int(first_multiple_input[1])

x2 = int(first_multiple_input[2])

v2 = int(first_multiple_input[3])

def kangaroo(x1, v1, x2, v2):
    if x2 > x1 and v2>= v1:
        print("NO") # return "NO"
    elif v1 == v2:
        if x1 == x2:
            print("YES")
        else:
            print("NO") 
    else:
        t = (x2 - x1) / (v1 - v2)
        if t >= 0 and t.is_integer():
            print("YES") #return "YES"
        else:
            print("NO") #return "NO"

kangaroo(x1, v1, x2, v2)




######## logic-2 for testing locally
"""
 if x2 > x1 and v2>= v1:
        return "NO"
    elif (x1 - x2)%(v2 - v1) == 0:
        return "YES"
    return "NO"
"""