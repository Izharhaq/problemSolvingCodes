"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code here
    #********* IZHAR CODE *********
    arr.sort()
    sticks_cut = []
    while arr:
        sticks_cut.append(len(arr))
        min_length = arr[0]
        # arr = [stick - min_length for stick in arr]
        for i in range(len(arr)):
            arr[i] -= min_length
        arr = [i for i in arr if i > 0]
    return sticks_cut

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

"""

#****************** Logic-1 *****************
"""
n = int(input().strip())
arr = list(map(int, input().rstrip().split()))

def cutTheSticks(arr):
    arr.sort()
    sticks_cut = []
    while arr:
        sticks_cut.append(len(arr))
        min_length = arr[0]
        # arr = [stick - min_length for stick in arr]
        for i in range(len(arr)):
            arr[i] -= min_length
        arr = [i for i in arr if i > 0]
    # return sticks_cut
    print(sticks_cut)

cutTheSticks(arr)
"""


#****************** Logic-2 *****************
"""
def cutTheSticks(arr):
    sticks=[]
    while len(arr)>0:
        sticks.append(len(arr))
        arr=[x-min(arr) for x in arr if x-min(arr)!=0]
        
    return sticks
"""

#****************** Logic-3 *****************
"""
def discard_zero(arr):
    while len(arr) > 0 and arr[0] == 0:
        arr = arr[1:]
    return arr
        

def cutTheSticks(arr):
    res = []
    arr.sort()
    while len(arr) > 0:
        res.append(len(arr))
        x = arr[0]
        for i in range(len(arr)):
            arr[i] = arr[i] - x
        arr = discard_zero(arr)
    return res
"""


#****************** Logic-4 *****************
"""
n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
# arr = [1,2,3,4,3,3,2,1]

def cutTheSticks(arr):
    arr.sort() 
    res=[len(arr)] 
    shortest=arr[-1] 
    while arr: 
        while arr and shortest==arr[-1]: 
            arr.pop() 
            if arr: 
                res.append(len(arr)) 
                shortest=arr[-1] 
        # return res
        print(res)
cutTheSticks(arr)
"""

#****************** Logic-5 *****************
"""
def cutTheSticks(arr):
    while arr:
        yield len(arr)
        cut = min(arr)
        arr = [x-cut for x in arr if x>cut]
"""

#****************** Logic-6 *****************
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def from_list(self, lst):
        self.head = None
        for item in lst:
            self.append(item)

    def sort(self):
        if not self.head or not self.head.next:
            return
        sorted = False
        while not sorted:
            sorted = True
            current = self.head
            while current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    sorted = False
                current = current.next

def cutTheSticks(arr):
    # Write your code here
    linked_list = LinkedList()
    linked_list.from_list(arr)

    linked_list.sort()

    result = []
    while linked_list.head:
        current_length = 0
        current = linked_list.head
        while current:
            current_length += 1
            current = current.next
        result.append(current_length)

        min_value = linked_list.head.data

        prev = None
        current = linked_list.head
        while current:
            current.data -= min_value
            if current.data == 0:
                if prev:
                    prev.next = current.next
                else:
                    linked_list.head = current.next
            else:
                prev = current
            current = current.next

    return result
"""


#****************** Logic-7 *****************
"""
def cutTheSticks(arr):
    sticks = []
    
    while arr:
        sticks.append(len(arr))
        arr = [n for n in map(lambda x: x-min(arr), arr) if n]
        
    return sticks
"""

#****************** Logic-8 *****************
"""
def cutTheSticks(arr):
    # Write your code here
    arr.sort()
    
    # Initialize an empty list to store the number of sticks at each iteration
    result = []
    
    # Continue while there are sticks remaining
    while arr:
        # Append the number of sticks remaining to the result list
        result.append(len(arr))
        
        # Find the length of the shortest stick
        min_length = arr[0]
        
        # Subtract the shortest length from each stick
        arr = [stick - min_length for stick in arr]

        # Remove any sticks with length zero
        arr = [stick for stick in arr if stick > 0]
    
    return result
"""

#****************** Logic-9 *****************
"""
def cutTheSticks(arr):
    # Write your code here
    length = len(arr)
    for x in range(length):
        if len(arr)<1:
            break
        min_1=min(arr)
        print(len(arr))
        arr = [x - min_1 for x in arr]
        arr = [d for d in arr if d > 0]
"""


n = int(input().strip())
arr = list(map(int, input().rstrip().split()))

def cutTheSticks(arr):
    arr.sort()
    sticks_cut = []
    while arr:
        sticks_cut.append(len(arr))
        min_length = arr[0]
        # arr = [stick - min_length for stick in arr]
        for i in range(len(arr)):
            arr[i] -= min_length
        arr = [i for i in arr if i > 0]
    # return sticks_cut
    print(sticks_cut)

cutTheSticks(arr)



