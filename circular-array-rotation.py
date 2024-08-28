"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def circularArrayRotation(a, k, queries):
    # Write your code here
    #**********  IZHAR CODE ***********
    result = []
    for i in range(k):
      temp = a[len(a)-1]
      a.pop()
      a.insert(0, temp)
    for i in queries:
      result.append(a[i])
    return result


    #**********  IZHAR CODE ***********

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

"""
# first_multiple_input = input().rstrip().split()
# n = int(first_multiple_input[0])
# k = int(first_multiple_input[1])
# q = int(first_multiple_input[2])
# a = list(map(int, input().rstrip().split()))



# def circularArrayRotation(a, k, queries):
#     rot_array = []
#     # for i in range(k):
#     if k > len(a):
#         k = k% len(a)    
#     return a[-k:] + a[:-k]
        




# circularArrayRotation(a, k, queries)



# first_multiple_input = input().rstrip().split()
# n = int(first_multiple_input[0])
# k = int(first_multiple_input[1])
# q = int(first_multiple_input[2])
# a = list(map(int, input().rstrip().split()))



a = [3,4,5] # 534, 453
k=2
queries=[1,2]

def circularArrayRotation(a, k, queries):

    result = []
    for i in range(k):
      temp = a[len(a)-1]
      a.pop()
      a.insert(0, temp)
    for i in queries:
      result.append(a[i])
    # return result
    print(result)

circularArrayRotation(a, k, queries)


#*************** Logic -2 **********************
"""
def circularArrayRotation(a, k, queries):
    length = len(a)
    for i in queries:
        yield a[i-k%length]
"""


#*************** Logic -3 **********************
"""
n = len(a)
    k = k % n

    def get_rotated_index(i):
        return (i - k + n) % n

    result = []
    for query in queries:
        rotated_index = get_rotated_index(query)
        result.append(a[rotated_index])

    return result
"""


#*************** Logic -4 **********************
"""
numbers = collections.deque(a)
    numbers.rotate(k)
    
    queryValues = [numbers[indexValue] for indexValue in queries]
    return queryValues
"""

#*************** Logic -5 **********************
"""
len_a = len(a)
    rotations = k % len_a
    results = []
    for q_index in queries:
        # Translate the query index to the new item space
        new_q_index = ((q_index + len_a) - rotations) % len_a
        # Retrieve the needed item from the input array
        results.append(a[new_q_index])
    return results
"""


#*************** Logic -6 **********************
"""
l=[]
    for i in range(k):
        s=a.pop()
        a.insert(0,s)
    for i in queries:
        l.append(a[i])
    return l
"""