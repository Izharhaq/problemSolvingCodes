"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    #**** IZHAR CODE *************
    birdsid_count = {} 
    for i in arr: 
        if i in birdsid_count: 
            birdsid_count[i] += 1 
        else: 
            birdsid_count[i] = 1 
        max_ids = max(birdsid_count.values()) 
        max_items = [key for key, value in birdsid_count.items() if value == max_ids] 
            results = min(max_items) 
        return results

    #**** IZHAR CODE *************

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

"""
"""
### Logic - for local testing ****** Working fine ##### 
def migratoryBirds(arr):
    birdsid_count = {} 
    for i in arr: 
        if i in birdsid_count: 
            birdsid_count[i] += 1 
        else: 
            birdsid_count[i] = 1 
    max_ids = max(birdsid_count.values()) 
    max_items = [key for key, value in birdsid_count.items() if value == max_ids] 
            results = min(max_items) 
        # return results
    print(results)
arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))

migratoryBirds(arr)
"""

"""
#### ****** Logic -2 ************* Tested and working fine ********* ######

def migratoryBirds(arr):
    bird_id_count = {}
    max_element = None
    max_count = 0

    for i in arr:
        if i in bird_id_count:
            bird_id_count[i] += 1
        else:
            bird_id_count[i] = 1

        if (bird_id_count[i] > max_count) or (bird_id_count[i] == max_count and (max_element is None or i < max_element)):
            max_count = bird_id_count[i]
            max_element = i
    return bird_id_count, max_element, max_count

arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))

birds_counts, most_frequent_element, most_frequent_count = migratoryBirds(arr)

print(most_frequent_element) # To show return value, may change in case if it ask for return
migratoryBirds(arr)


******************************************
#*********** APPROACHES **********

1. Counts the occurrences of each bird ID in the list arr.
2. Identify the highest count of any bird ID.
3. Collect all bird IDs that have this highest count.
4. Selects the smallest bird ID.
5. Returns this smallest, most frequent bird ID.
"""





###*************************

"""
#### Working on this logic, Need to test ####
def migratoryBirds(arr): 
    ele=list(set(arr)) 
    ele.sort() 
    res=[] 
    for i in ele: 
        res.append(arr.count(i))
        max_count=max(res) 
    return ele[res.index(max_count)]
migratoryBirds(arr)
"""