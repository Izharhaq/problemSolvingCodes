"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    #****** IZHAR CODE **********
    result = math.factorial(n)
    # Print the result
    print(result)

    #****** IZHAR CODE **********


if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)

"""


# n = int(input().strip())
# def extraLongFactorials(n):
#     res = 1
#     for i in range(n):
#         res

# extraLongFactorials(n)

#***********
n = 4
def extraLongFactorials(n): 
    n_fact=1 
    while n>0: 
        n_fact=n_fact*(n) 
        n=n-1 
    return n_fact
    print(n_fact)
extraLongFactorials(n)
"""

"""

"""
import math
def extraLongFactorials(n):
    # Calculate factorial using math.factorial
    result = math.factorial(n)
    # Print the result
    print(result)
extraLongFactorials(n)

"""

"""
def factRecursive(n):
    if n==1:
        return 1
    return n * factRecursive(n-1)
    
def extraLongFactorials(n):
    print(factRecursive(n))
"""


"""
def multiply_big_numbers(num1, num2):
    result = [0] * (len(num1) + len(num2))
    
    num1 = num1[::-1]
    num2 = num2[::-1]
    
    for i in range(len(num1)):
        for j in range(len(num2)):
            product = int(num1[i]) * int(num2[j])
            result[i + j] += product
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10
    
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    
    return result[::-1]

def factorial(n):
    # Write your code here.
    result = [1]
    
    for i in range(2, n + 1):
        current_number = list(map(int, str(i)))
        result = multiply_big_numbers(result, current_number)
    
    return ''.join(map(str, result))

"""

"""
def extraLongFactorials(n):
    # Write your code here
    if n == 1 or n == None:
        return 1
    return n*extraLongFactorials(n-1)

if __name__ == '__main__':
    n = int(input().strip())

    print(extraLongFactorials(n))
"""

