"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'primeXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def primeXor(a):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        result = primeXor(a)

        fptr.write(str(result) + '\n')

    fptr.close()

"""


#*******************************88




"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the primeXor function below.
prime = [True] * (8192) 
  
def SieveOfEratosthenes(n):  
    prime[1] = False
    p = 2  
    while p * p <= n: 
        if prime[p]:   
            for i in range(p * 2, n + 1, p):  
                prime[i] = False          
        p += 1

def primeXor(a):
    SieveOfEratosthenes(8191)
    MOD = 10 ** 9 + 7
    count = 0
    c = Counter(a)
    M = 8192     
    dp = [0 for i in range(M)]
    dp[0] = 1 # XOR value for any empty set is 1
    for num in c.keys():
        even, odd = (c[num] // 2 + 1), ((c[num] + 1) // 2)
        dp = [(dp[ctr] * even + dp[ctr ^ num] * odd) % MOD for ctr in range(M)]
    for num in range(1, M):
        if prime[num]:
            count += dp[num]
            if count >= MOD:
                count %= MOD
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        n = int(input())
        a = list(map(int, input().rstrip().split()))
        result = primeXor(a)
        fptr.write(str(result) + '\n')
    fptr.close()
"""


