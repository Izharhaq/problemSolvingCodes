# ******** Problem Statement ***********************
"""
Professor will cancel a class if students come late....
a[i]<= 0 --> On time,  a[i] --> late
return "YES" if class is canceled otherwise "NO".
k=3 (Minimum students reuired to run class) , 
a=[-2,-1,0,1,2] -->> 3 students are on time so it will return NO
"""
 
#****** Solution *******************
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'angryProfessor' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#

def angryProfessor(k, a):
    # Write your code here
    #****** IZHAR CODE *******
    students_on_time = []
    for i in range(n):
        if a[i]<= 0:
            students_on_time.append(i)
    if len(students_on_time) >= k:
        return "NO"
    else:
        return "YES"

    #****** IZHAR CODE ********

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()

"""
#*************** Logic-2 ***************
"""
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
a = list(map(int, input().rstrip().split()))

# n=5
# k=3
# a=[-2, -1, 0, 1, 2]

def angryProfessor(k, a):
    students_on_time = 0
    for i in a:
        if a[i]<= 0:
            students_on_time += 1
        else:
            continue
        if students_on_time>= k:
            # return "NO"
            print("NO")
        else:
            # return "YES"
            print("YES")

angryProfessor(k, a)
"""

"""
##***submitted earlier **
students_on_time = []
    for i in range(n):
        if a[i]<= 0:
            students_on_time.append(i)
    if len(students_on_time) >= k:
        return "NO"
    else:
        return "YES"


"""

"""
def angryProfessor(threshold, arrivalTimes):
    
    onTime=0
    for arrivalTime in arrivalTimes:
        if arrivalTime<=0:
            onTime += 1
    if onTime >= threshold:
        return "NO"
    else:
        return "YES"
"""


"""
def angryProfessor(k, a):
    # Write your code here
    return "NO" if len([student for student in a if student <= 0]) >= k else "YES"
"""

"""
def angryProfessor(k, a):
    return "NO" if sum(map(lambda x: x<=0, a))>=k else "YES"
"""

"""
 arrival_times_str = list(map(str, a))
    
    on_time_str = list(filter(lambda x: int(x) <= 0, arrival_times_str))
    
    on_time_int = list(map(int, on_time_str))
    
    on_time_count = 0
    for time in on_time_int:
        on_time_count += 1
    
    if on_time_count < k:
        return "YES"
    else:
        return "NO"
"""


"""
def angryProfessor(k, a):
    count=0 
    for i in range(len(a)): 
        if a[i]<=0: 
            count +=1 
        else: 
            continue 
        if count>=k: 
            return "NO" 
        else: 
            return "YES"
"""

