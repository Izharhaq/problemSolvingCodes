"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    #*********** IZHAR CODE ***************
    special_characters = "!@#$%^&*()-+"
    countNum = 0
    countLower = 0
    countUpper = 0
    countSpecial = 0

    for i in password:
        if i.isdigit():
            countNum = 1
        elif i.islower():
            countLower = 1
        elif i.isupper():
            countUpper = 1
        elif i in special_characters:
            countSpecial = 1
    
    charPresent = countNum + countLower + countUpper + countSpecial
    charNeeded = 4- charPresent
    
    currentLength = len(password) + charNeeded
    
    if currentLength < 6:
        charNeeded += (6-currentLength)
     
    return charNeeded

    #*********** IZHAR CODE ***************

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()

"""


n = int(input().strip())
password = input()


# def minimumNumber(n, password):
#     count = 0
#     numbers = "0123456789"
#     lower_case = "abcdefghijklmnopqrstuvwxyz"
#     upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     special_characters = "!@#$%^&*()-+"

#     has_uppercase = False
#     has_lowercase = False
#     has_digit = False
#     has_special = False

#     if len(password)< 6:
#         # return False
#         print(6-n)
#     else :
#         for i in password:
#             if i in upper_case:
#             # has_uppercase = True
#                 count += 1
#             elif i in lower_case:
#             # has_lowercase = True
#                 count += 1
#             elif i in numbers:
#             # has_digit = True
#                 count += 1
#             elif i in special_characters:
#             # has_special = True
#                 count += 1

#     print(4-count)


#     # if has_uppercase and has_lowercase and has_digit and has_special:
#     #     return True
    
#     # return False


# minimumNumber(n, password)

"""
"""
def minimumNumber(n, password): 
    special_characters = "!@#$%^&*()_-+"
    countNum = 0
    countLower = 0
    countUpper = 0
    countSpecial = 0
    
    for i in password:
        if i.isdigit():
            countNum = 1
        elif i.islower():
            countLower = 1
        elif i.isupper():
            countUpper = 1
        elif i in special_characters:
            countSpecial = 1
    
    charPresent = countNum + countLower + countUpper + countSpecial
    charNeeded = 4- charPresent
    
    currentLength = len(password) + charNeeded
    
    if currentLength < 6:
        charNeeded += (6-currentLength)
     
    # return charNeeded
    print(charNeeded)

minimumNumber(n, password)

"""
"""

"""
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    s = list(password)
    lower_c=0
    upper_c=0
    char_c=0
    digit_c=0
    for i in range(len(s)):
      
        if s[i].isupper():
            upper_c=1
        elif s[i].islower():
            lower_c=1
        elif s[i].isdigit():
            digit_c=1
        elif s[i] in ['!','@','#','$','%','^','&','*','(',')','-','+']:
            char_c=1
            
    final_counter = lower_c+upper_c+digit_c+char_c
    types_needed = 4 - final_counter
    
    # Calculate how many characters are needed to reach the minimum length of 6
    length_needed = max(0, 6 - n)
"""


"""
def minimumNumber(n, password):
    # Define character sets
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    # Flags for each type of character
    has_digit = has_lower = has_upper = has_special = False

    # Check the presence of each type of character in the password
    for char in password:
        if char in numbers:
            has_digit = True
        elif char in lower_case:
            has_lower = True
        elif char in upper_case:
            has_upper = True
        elif char in special_characters:
            has_special = True

    # Count the number of missing character types
    missing_types = 0
    if not has_digit:
        missing_types += 1
    if not has_lower:
        missing_types += 1
    if not has_upper:
        missing_types += 1
    if not has_special:
        missing_types += 1

    # Calculate the minimum number of characters to add
    # It should be the maximum of missing types and (6 - n)
    return max(missing_types, 6 - n)
"""
