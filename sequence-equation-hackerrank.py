"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    # Write your code here
    #*******IZHAR CODE **********************
    res = []
    for i in range(1, len(p)+1):
        item_location = p.index(i)+1        # adding 1 because it results index from 0.
        item_location_value = p.index(item_location)+1
        res.append(item_location_value)
    return res

    #*******IZHAR CODE **************



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

"""


n = int(input().strip())
p = list(map(int, input().rstrip().split()))

# n = 5
# p =[5,2,1,3,4] # [3,2,4,5,1]...........[4,2,5,1,3]

def permutationEquation(p):
    res = []
    for i in range(1, len(p)+1):
        item_location = p.index(i)+1       # adding 1 because it results index from 0.
        item_location_value = p.index(item_location)+1
        res.append(item_location_value)
    # return res
    print(res)

permutationEquation(p)



#************ Logic-2 ****************
"""
def permutationEquation(p):
    ans=[]
    for i in range(1,len(p)+1):
        ans.append(p.index(p.index(i)+1)+1)
    return ans
"""

#************ Logic-3 ****************
"""
def permutationEquation(p):
    np=p.copy()
    np.sort()
    ai=[]
    for i in np:
        x=p.index(i)+1
        ai.append(p.index(x)+1)
    return ai

"""

#************ Logic-4 ****************
"""
def permutationEquation(p):
    return [p.index(p.index(i)+1)+1 for i in range(1, len(p)+1)]
"""


#************ Logic-5 ****************
"""
def permutationEquation(p):
    length = len(p)
    results = {p[p[i-1]-1]:i for i in range(1, length+1)}
    for i in range(1, length+1):
        if result := results.get(i):
            yield result

"""

"""
def permutationEquation(p):
    values_index = {}
    y = []

    for x in range(1, len(p) + 1):
        values_index[p[x - 1]] = x

    for x in range(1, len(p) + 1):
        y.append(values_index[values_index[x]])

    return y
"""


"""
def permutationEquation(p):
    p.insert(0, 0)
    return [p.index(p.index(x)) for x in range(1, len(p))]
"""

"""
def permutationEquation(p=[]):
    return [p.index(p.index(n)+1)+1 for n in range(1, len(p)+1)]
"""


"""
#******** It results Runtime Error *****************

def permutationEquation(p):
    result=[]
    for indice in range(1, len(p) +1):
        for item in p:
            if indice == item:
                locationOfItem = p.index(item)+1
                locationOfItemValue = p.index(locationOfItem)+1
                result.append(locationOfItemValue)
    return result

"""