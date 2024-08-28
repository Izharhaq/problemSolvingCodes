"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here
    #****** IZHAR CODE ********
    res = 0
    str_n = str(n)
    for i in str_n:
        if i == '0':
            continue
        elif n% int(i)==0:
            res += 1
    return res

    #****** IZHAR CODE *******

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

"""


# t = int(input().strip())
# for t_itr in range(t):
#     n = int(input().strip())

# n = 1012
n = 1012345678901234567890123456789012345678901234567890
def findDigits(n):
    res = 0
    str_n = str(n)
    for i in str_n:
        if i == '0':
            continue
        elif n% int(i)==0:
            res += 1
    return res
    # print(res)
findDigits(n)


#************** Logic - 2 ************
"""
def findDigits(n):
    c=0
    for i in str(n):
        if int(i)!=0:
            if n%int(i)==0:
                c+=1
            
    return c
"""

"""
def findDigits(n):
    s=0
    for i in str(n):
        if i!='0'and n%int(i)==0 :
            s+=1
    return s
"""

"""
def findDigits(n):
    number = n
    count = 0
    while n > 0:
        num = n% 10
        if num != 0 and number % num == 0:
            count +=1
        n //= 10
    return count
"""

"""
def findDigits(n: int) -> int:
        return sum(1 for digit in filter(lambda d: d != '0' and n % int(d) == 0, str(n)))
"""


"""
def digit_list(n):
    return list(map(int, str(n)))

def is_valid_divisor(n, digit):
    return digit != 0 and n % digit == 0

def count_valid_divisors(n, digits, count=0):
    if not digits:
        return count
    digit = digits[0]
    if is_valid_divisor(n, digit):
        count += 1
    return count_valid_divisors(n, digits[1:], count)

def findDigits(n):
    # Write your code here.
    digits = digit_list(n)
    count = count_valid_divisors(n, digits)
    return count
"""

"""
def findDigits(n: int) -> int:
    divisors_count = 0

    for digit in str(n):
        parsed_digit = int(digit)

        if parsed_digit == 0:
            continue

        if n % parsed_digit == 0:
            divisors_count += 1

    return divisors_count
"""