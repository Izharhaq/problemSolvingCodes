"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#

def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    #******* IZHAR CODE ***********
    if y1>y2:
        return 10000
    elif y1==y2 and m1>m2:
        return (m1-m2)*500
    elif y1==y2 and m1==m2 and d1>d2:
        return (d1-d2)*15
    else:
        return 0

    #******** IZHAR CODE **********




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()

"""



"""
def libraryFine(d1, m1, y1, d2, m2, y2): 
    if y1==y2 and m1==m2 and d1==d2: 
        return 0 
    elif y1==y2 and m1==m2 and d1>d2: 
        return (d1-d2) * 15 
    elif y1==y2 and m1>m2: 
        return (m1-m2) * 500 
    elif y1>y2: 
        return (y1-y2) * 10000 
    else: 
        return 0
"""

"""
def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1<y2:
        return 0
    if d1<=d2 and m1==m2 and y1==y2:
        return 0
    if d1>d2 and m1==m2 and y1==y2:
        return 15*(d1-d2)
    if m1<=m2 and y1<=y2:
        return 0
    if m1>m2 and y1==y2:
        return 500*(m1-m2)
    if y1>y2:
        return 10000
"""

"""
import datetime
def libraryFine(d1, m1, y1, d2, m2, y2):
    returned = datetime.datetime(y1, m1, d1)
    duedate = datetime.datetime(y2, m2, d2)
    late_days = (returned - duedate).days
    if late_days <= 0:
        return 0
    if returned.year == duedate.year:
        if returned.month == duedate.month:
            return 15 * late_days
        return 500 * (returned.month - duedate.month + 12*(returned.year-duedate.year))
    return 10000
"""

"""
def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        return 10000
    elif y1 == y2 and m1 > m2:
        return 500 * (m1 - m2)
    elif y1 == y2 and m1 == m2 and d1 > d2:
        return 15 * (d1 - d2)
    else:
        return 0
"""


"""
def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 != y2:
        if y1 < y2:
            return 0
        return 10000
    else:
        if m1 < m2:
            return 0
        return max(0, (m1-m2)*500, (d1-d2)*15)
"""

"""
def libraryFine(d1, m1, y1, d2, m2, y2):
    return max(0, d1-d2)*15*bool(m1==m2)*bool(y1==y2) + max(0, m1-m2)*500*bool(y1==y2) + max(0, y1-y2)*10000
"""

"""
def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        return 10000
    elif y1 == y2 and m1 > m2:
        return (m1-m2) * 500
    elif y1 == y2 and m1 == m2 and d1 > d2:
        return (d1-d2) * 15
    else:
        return 0
"""

"""
def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    if y1>y2:
        return 10000
    elif y1==y2 and m1>m2:
        return (m1-m2)*500
    elif y1==y2 and m1==m2 and d1>d2:
        return (d1-d2)*15
    else:
        return 0
"""

"""
def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    if y1>y2:
        return 10000
    elif y1==y2 and m1>m2:
        return (m1-m2)*500
    elif y1==y2 and m1==m2 and d1>d2:
        return (d1-d2)*15
    else:
        return 0
"""


#********************** Working on this logic ********

"""
first_multiple_input = input().rstrip().split()
d1 = int(first_multiple_input[0])
m1 = int(first_multiple_input[1])
y1 = int(first_multiple_input[2])
second_multiple_input = input().rstrip().split()
d2 = int(second_multiple_input[0])
m2 = int(second_multiple_input[1])
y2 = int(second_multiple_input[2])



def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 <= y2:
        if m1 <=m2:
            if d1>d2:
                print((d1-d2)*15)
            else:
                print("0")
        else:
            print((m2-m1)*500)
    else:
        print("10000")


libraryFine(d1, m1, y1, d2, m2, y2)
"""