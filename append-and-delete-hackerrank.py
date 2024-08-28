"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    #***** IZHAR CODE ***********
    if len(s) + len(t) <= k:
        return 'Yes'
    else:
        t = list(t)
        s = list(s)
        for i in range(k):
            if len(t) > len(s):
                t.pop()
            else:
                s.pop()
        if s == t:
            return 'Yes'
        return 'No'


    #***** IZHAR CODE ***********

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()


"""

# # s = input()
# # t = input()
# # k = int(input().strip())
# s = ['a','b','c']
# t = ['d','e','f']
# k = 6


# def appendAndDelete(s, t, k):
#     for i in range(len(s)):

# appendAndDelete(s, t, k)


"""
def appendAndDelete(s, t, k):
    if k-len(s)>=len(t):
        return "Yes"
    try:
        while s[0] == t[0]:
            s = s[1:]
            t = t[1:]
    except IndexError:
        pass
    length_s = len(s)
    length_t = len(t)
    if length_s+length_t <= k:
        if (k-length_s-length_t)%2 == 0:
            return "Yes"
    return "No"
"""


"""
def appendAndDelete(s, t, k):
    i = 0 # index of first char in strings that dont match
    while (i < (min(len(s), len(t)))):
        if not s[i] == t[i]:
            break
        i += 1
    back = len(s) - i
    front = len(t) - i
    totalDist = back + front
    if (k - totalDist) % 2 == 0 and (k - totalDist >= 0): 
        return "Yes"
    elif k >= len(s) + len(t):
        return "Yes"
    else:
        return "No"
"""


"""
def appendAndDelete(s, t, k):
    c,d=0,0
    if set(s)==set(t):
        return 'Yes'
    else:
        for i in range(1,len(s)+1):
            if s[:i]==t[:i]:
                c+=1
        if len(s)<len(t):
            return 'No'
        else:
            if len(s)+len(t)-(2*c)<=k:
                return 'Yes'
            else:
                return 'No'
"""

"""
def appendAndDelete(s, t, k):
    common_length = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            common_length += 1
        else:
            break

    total_operations = len(s) + len(t) - 2 * common_length
    
    if k >= len(s) + len(t) or (k >= total_operations and (k - total_operations) % 2 == 0):
        return 'Yes'
    else:
        return 'No'
"""


"""
def appendAndDelete(s, t, k):
    a = list(s)
    b = list(t)
    
    for i in range(k):
        if a == b[:len(a)] and k - i == len(b[len(a):]):
            a.append(b[len(a)])
        else:
            if a:
                a.pop()

    return "Yes" if a == b else "No"
"""

"""
def appendAndDelete(s, t, k):
    c,b=0,0
    for i in range(len(min(s,t))):
        if s[i]==t[i]:
            c+=1
        else:
            break
    for i in range(len(t[c:])):
        if t[i]!=t[c+i]:
            b=1
            break
    if b==1 and len(s)<len(t):
        return "No"
    elif len(s+t)-(2*c)<=k:
        return "Yes"
    else:
        return "No"
"""

"""
def appendAndDelete(s, t, k):
    common_prefix_length = 0
    
    # Find the length of the common prefix
    for i, (char_s, char_t) in enumerate(zip(s, t)):
        if char_s == char_t:
            common_prefix_length += 1
        else:
            break
    
    # Calculate the steps required for deletion and appending
    steps_required = len(s) + len(t) - 2 * common_prefix_length
    
    # Check if steps_required is less than or equal to k and satisfies the constraints
    if k >= steps_required and (k - steps_required) % 2 == 0 or k >= len(s) + len(t):
        return 'Yes'
    else:
        return 'No'
"""

"""
def appendAndDelete(s, t, k):
    if len(s) + len(t) <= k:
        return 'Yes'
    else:
        t = list(t)
        s = list(s)
        for i in range(k):
            if len(t) > len(s):
                t.pop()
            else:
                s.pop()
        if s == t:
            return 'Yes'
        return 'No'
"""

"""
def appendAndDelete(s, t, k):
    if k > len(s) + len(t):
        return "Yes"
    if s[0] == t[0]:
        for char1, char2 in zip(s, t):
            if char1 != char2:
                break
            k += 2
        return "Yes" if (len(s) + len(t) <= k) and (len(s) + len(t) - k) % 2 == 0 else "No"
        
    return "Yes" if len(s) + len(t) <= k else "No"
"""

"""
def appendAndDelete(s, t, k):
    # Write your code here
    match_pointer = (False, 0)
    for i,(_,_) in enumerate(zip(s, t)):
        if s[:i+1]==t[:i+1]:
            match_pointer = (True, i)
    if match_pointer[0] :
        min_op = (len(s) - match_pointer[1]-1)+(len(t) - match_pointer[1]-1)
        temp = [min_op]
        for i in range(1,match_pointer[1]+2):
            temp.append(min_op+2*i)
        if k in temp or k > max(temp):
            return "Yes"
    elif k > len(t):
        return "Yes"
        
        
    return "No"
"""

"""
def appendAndDelete(s, t, k):
    # Write your code here
    n = len(t)
    m = len(s)
    i = 0
    j = 0
    c = 0
    while i < m and j < n :
        if s[i] != t[j] :
            break
        else:
            i += 1
            j += 1
            c += 1
    ops = (n-c) + (m-c)
    if n+m <= k :  
        return "Yes"
    if ops <= k :
        if (k-ops)%2 == 0:   
            return "Yes"
        elif (k-ops)%2 != 0 and k >= (n-c)+(m-c)+2*c:  # 2*c means delete string and waste the operations and cinstruct upto c
            
            return "Yes"
        elif (k-ops)%2 != 0 and k < (n-c)+(m-c)+2*c:
            return "No"
    return "No"
"""


"""
def appendAndDelete(s, t, k):
    # Write your code here
    n = len(t)
    m = len(s)
    i = 0
    j = 0
    c = 0
    while i < m and j < n :
        if s[i] != t[j] :
            break
        else:
            i += 1
            j += 1
            c += 1
    ops = (n-c) + (m-c)
    if n+m <= k :   # we remover entire string and use extra operation on empty string and create string
        return "Yes"
    if ops <= k :
        if (k-ops)%2 == 0:    # add,delete on one character
            return "Yes"
        elif (k-ops)%2 != 0 and k >= (n-c)+(m-c)+2*c:  # 2*c means delete string and waste the operations and cinstruct upto c
            
            return "Yes"
        elif (k-ops)%2 != 0 and k < (n-c)+(m-c)+2*c:
            return "No"
    return "No"
"""

"""
def appendAndDelete(s, t, k):
    n = len(s)
    m = len(t)
    i = 0
    j = 0 
    count = 0
    while i < n and j < m:
        if s[i] != t[j]:
            break
        else:
            count += 1
            i += 1
            j += 1
    n1 = n-count 
    m1 = m-count 
    remaining_operations = n1 + m1

    # Check if it's possible to perform exactly k operations
    #
    if k >= n + m or (k >= remaining_operations and (k - remaining_operations) % 2 == 0):
        return "Yes"
    else:
        return "No"
"""

"""
def appendAndDelete(s, t, k):    
    diff = 0
    shorter = min(len(s), len(t))
    for i in range(shorter):
        if s[i] != t[i] or i == shorter - 1:
            diff = i
            break    
    count = len(s) - diff + len(t) - diff
    if count <= k and (count - k) % 2 == 0:
        return "Yes"
    elif len(s) + len(t) <= k:
        return "Yes"
    else:
        return "No"
"""


#**********************************************************
s = input()
t = input()
k = int(input().strip())



def appendAndDelete(s, t, k):
    if len(s) + len(t) <= k:
        # return 'Yes'
        print("Yes")
    
    else:
        t = list(t)
        s = list(s)
        for i in range(k):
            if len(t) > len(s):
                t.pop()
            else:
                s.pop()
        if s == t:
            # return 'Yes'
            print("Yes")
        # return 'No'
        print("No")
    
appendAndDelete(s, t, k)