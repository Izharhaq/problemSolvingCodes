"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    # Write your code here
    f_b=0 #front back
    t_b=0 #top bottom
    l_r=0 # left right
    
    #top and bottom surface area
    t_b = H * W * 2

    
    #Front and Back surface area
    if H==1:
        for j in range(W):
            f_b+=A[0][j]*2
    else:
        for i in range(H):
            for j in range(W):
                if i == H-1:
                    f_b+=A[i][j]
                    f_b+=(abs(A[i][j]-A[i-1][j]))
                elif i != 0:
                    f_b+=(abs(A[i][j]-A[i-1][j]))
                else:
                    f_b+=A[i][j]  
    
    
    #left and right surface area
    if W == 1:
        for i in range(H):
            l_r+=A[i][0]*2
    else:
        for j in range(W):
            for i in range(H):
                if j == W-1:
                    l_r+=A[i][j]
                    l_r+=(abs(A[i][j]-A[i][j-1]))
                elif j !=0:
                    l_r+=(abs(A[i][j]-A[i][j-1]))
                else:
                    l_r+=A[i][j]
    
    return f_b + l_r + t_b
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()

"""


"""
f_b=0 #front back
    t_b=0 #top bottom
    l_r=0 # left right
    
    #top and bottom surface area
    t_b = H * W * 2

    
    #Front and Back surface area
    if H==1:
        for j in range(W):
            f_b+=A[0][j]*2
    else:
        for i in range(H):
            for j in range(W):
                if i == H-1:
                    f_b+=A[i][j]
                    f_b+=(abs(A[i][j]-A[i-1][j]))
                elif i != 0:
                    f_b+=(abs(A[i][j]-A[i-1][j]))
                else:
                    f_b+=A[i][j]  
    
    
    #left and right surface area
    if W == 1:
        for i in range(H):
            l_r+=A[i][0]*2
    else:
        for j in range(W):
            for i in range(H):
                if j == W-1:
                    l_r+=A[i][j]
                    l_r+=(abs(A[i][j]-A[i][j-1]))
                elif j !=0:
                    l_r+=(abs(A[i][j]-A[i][j-1]))
                else:
                    l_r+=A[i][j]
    
    return f_b + l_r + t_b
"""