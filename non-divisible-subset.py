"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    #****** IZHAR CODE *******
    freq_s = [0] * k
    for num in s:
        freq_s[num %k] += 1

    result = min(freq_s[0], 1)

    for i in range(1, k//2 + 1):
        if i != k - i:
            result += max(freq_s[i], freq_s[k - i])
        else:
            result += 1
    return result

    #******* IZHAR CODE ********

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()

"""
# k = 3
# s = [1,7,2,4]
# k = 4
# s = [19,10,12,10,24,25,22]
# def nonDivisibleSubset(k, s):
#     new_s = []
#     for i in range(len(s)):
#         for j in range(i+1, len(s)):
#             if (s[i]+s[j])%k != 0:
#                 new_s.append((s[i], s[j]))
#     # return len(new_s)
#     print(len(new_s))


# nonDivisibleSubset(k, s)

#**********************************
k = 3
s = [1,7,2,4]
def nonDivisibleSubset(k, s):
    freq_s = [0] * k 
    for num in s: 
        freq_s[num%k] += 1

    result = min(freq_s[0], 1)

    for i in range(1, k//2 + 1):
        if i != k - i:
            result += max(freq_s[i], freq_s[k - i])
        else:
            result += 1
    # return result
    print(result)

nonDivisibleSubset(k,s)

"""
def nonDivisibleSubset(k, s):
    # Write your code here
    d=defaultdict(int)
    ans=0
    for i in s:
        d[i%k]+=1
    if d[0]>0:
        ans=1
    for i in range(1,k):
        if d[i]==0:
            continue
        if i+i==k:
            ans+=1
        else:
            ans+=max(d[i],d[k-i])
            d[k-i]=0
            d[i]=0
    return ans
"""


"""
def nonDivisibleSubset(k, s):
    remainder = [num % k for num in s]
    remainderCount = [remainder.count(i) for i in range(0, k)]
    length = 0
    for i in range(1, (k+1)//2):
        if remainderCount[i] > remainderCount[k-i]:
            length += remainderCount[i]
        else:
            length += remainderCount[k-i]
    if remainderCount[0] > 0:
        length += 1
    if k % 2 == 0 and remainderCount[int(k/2)] > 0:
        length += 1
    return length
"""


"""
def nonDivisibleSubset(k, s):
    # Write your code here
    remainder_count = [0] * k

    for number in s:
        remainder_count[number % k] += 1

    max_subset_size = min(remainder_count[0], 1)

    for r in range(1, (k // 2) + 1):
        if r != k - r:
            max_subset_size += max(remainder_count[r], remainder_count[k - r])
        else:
            max_subset_size += min(remainder_count[r], 1)

    return max_subset_size
"""


"""
def nonDivisibleSubset(k, s):
    reminderList = []
    for el in s:
        reminderList.append(el%k)
    result = 0
    freqDict = {}
    if reminderList.count(0) >0:
        result+=1
    if k%2 ==0:
        if reminderList.count(k/2) > 0:
            result+=1
    for i in range(1,k):
        if i == k/2:
            continue
        freqDict[i] = reminderList.count(i)
    for i in range(1, k//2 +1):
        if i == k/2:
            continue
        if freqDict[i] > freqDict[k-i]:
            result += freqDict[i]
        else:
            result += freqDict[k-i]
    return result
"""


"""
def nonDivisibleSubset(k, s):
    # Write your code here
    lst = [0]*(k+1)
    res = 0
    
    for num in s:
        lst[num % k] += 1
    
    print(lst)
    for num in range(math.ceil(len(lst)/2)):
        if num == 0 or num == k-num:
            res += min(lst[num], 1)
        else:
            res += max(lst[num], lst[k-num])
        print(res)
    return res
"""


"""
def nonDivisibleSubset(k, s): 
    freq_s = [0] * k 
    for num in s: 
        freq_s[num%k] += 1

    result = min(freq_s[0], 1)

    for i in range(1, k//2 + 1):
        if i != k - i:
            result += max(freq_s[i], freq_s[k - i])
        else:
            result += 1
    return result
"""

"""
def nonDivisibleSubset(k, s):
    remainder_counts = {}
    for i in s:
        remainder = i % k
        remainder_counts[remainder] = remainder_counts.get(remainder,0) + 1
    
    # 0 and k/2 remainders can't be duplicate
    subset_size = 0
    if 0 in remainder_counts:
        subset_size += 1
        del remainder_counts[0]
    if k%2 == 0 and k/2 in remainder_counts:
        subset_size += 1
        del remainder_counts[k//2]
    
    to_remove = set()
    for remainder in remainder_counts.keys():
        if remainder in to_remove:
            continue
        complement = k - remainder
        if complement not in remainder_counts or complement in to_remove:
            continue
        if remainder_counts[remainder] > remainder_counts[complement]:    
            to_remove.add(complement)
        else:                   
            to_remove.add(remainder)
    for remainder in to_remove:
        del remainder_counts[remainder]
      
    return subset_size + sum(remainder_counts.values())
"""

"""
from collections import defaultdict
def nonDivisibleSubset(k, s):
    # Write your code here
    freqs = defaultdict(int)
    for n in s:
        freqs[n % k] += 1
    result = min(freqs[0], 1)
    for i in range(1, k//2 +1):
        if i==k-i:
            result+=1
        else:
            result+=max(freqs[i],freqs[k-i])
    return result
"""


"""
def nonDivisibleSubset(k, s):
    rc= {}
    rl= []
    rcl = []
    for x in s:
        r=x % k
        if r in rc:
            rc[r]+=1
        else:
            rc[r]= 1
    sr=sorted(rc.items(), key=lambda x: x[1], reverse=True)
    for rem, c in sr:
        if rem == 0 or (k % 2 == 0 and rem == k // 2):
            rcl.append(1)
        elif k - rem not in rl:
            rl.append(rem)
            rcl.append(c)
    return sum(rcl)
"""

"""
def nonDivisibleSubset(k, s):
    # Write your code here
    remainderArr = [0]*k
    for i in s:
        remainderArr[i%k] += 1
    
    maxLength = 0
    maxLength += min(remainderArr[0],1)
    
    if k%2==0:
        maxLength += min(remainderArr[k//2],1)
    
    for i in range(1,k//2+1):
        if i != k-i:
            maxLength += max(remainderArr[i],remainderArr[k-i])
    
    return maxLength
"""

"""
def nonDivisibleSubset(k, s):
    # Write your code here
    
    freq_of_rem=[0 for i in range(k)]
    for num in s:
        freq_of_rem[(num%k)]+=1
    print(freq_of_rem)
    result=0
    
    if(freq_of_rem[0]>=1):
        result+=1
    if(k%2==0):
        for i in range(1,(k//2)):
            result+=max(freq_of_rem[i],freq_of_rem[(k-i)])
        result+=min(1,freq_of_rem[k//2])
    else:
        for i in range(1,(k//2)+1):
            result+=max(freq_of_rem[i],freq_of_rem[(k-i)])
        
        
    print(result)
    return result
"""


