###****APPROCHES *********
"""
1. Sort the array
2. Iterate and count
3. Track maximum length
"""


n = int(input().strip())
a = list(map(int, input().rstrip().split()))
def pickingNumbers(a):
    a.sort()
    max_length = 0
    for i in range(len(a)):
        current_subarray = [a[i]]
        for j in range(i+1, len(a)):
            if abs(a[j] - a[i]) <= 1:            
                current_subarray.append(a[i])
            else:
                break

        max_length = max(max_length, len(current_subarray))
    # return max_length
    print(max_length)

pickingNumbers(a)




##********* Logic-2  *************
"""
def pickingNumbers(a):
    maxL = 0
    for e,i in enumerate(a):
      x = []
      x.append(i)
      A = a.copy()
      A.pop(e)
      for j in A:
        if j == x[0] or abs(j - x[0] == 1):
          x.append(j)
      if len(x) > maxL:
        maxL = len(x)
        
    return maxL
"""


##********* Logic-3  *************
"""
from itertools import combinations

def pickingNumbers(a):
    # Write your code here
    elements = set(a)
    combos = [(a,b) for a,b in list(combinations(elements,2)) if abs(a-b) <= 1]
    max_len = 0
    for combo in combos:
        tmp_len = len(list(filter(lambda x: x in combo, a)))
        if tmp_len > max_len:
            max_len = tmp_len
    # Check the case for single element
    for ele in a:
        tmp_len = len([x for x in a if x ==ele])
    if tmp_len > max_len:
        max_len = tmp_len
return max_len

"""

##********* Logic-4  *************
"""
def pickingNumbers(a):
    counter = Counter(a)
    max_counter = float('-inf')
    
    for num in a:
        max_counter = max(max_counter, counter.get(num, 0) + counter.get(num+1, 0))
    return max_counter
"""

##********* Logic-5  *************
"""
from collections import Counter
def pickingNumbers(a):
    count_dic = Counter(a)
    unique_list = sorted(list(set(a)))
    max_list = []
    for i in range(len(unique_list)-1):
        if unique_list[i]+1 == unique_list[i+1]:
            max_list.append(count_dic[unique_list[i]] + count_dic[unique_list[i+1]])
    if max_list:
        return max(max(max_list), max(count_dic.values()))
    else:
        return max(count_dic.values())
"""

##********* Logic-6  *************
"""
from collections import Counter
def pickingNumbers(a):
    constant = 0
    arr = Counter(a)
    keys = list(arr.keys())
    keys.sort()
    for i in range(1, len(keys)):
        if keys[i] == keys[i-1] + 1:
            constant = max(constant, arr[keys[i]] + arr[keys[i-1]])
    for i in arr.values():
        if i > constant:
            constant = i
    return constant
"""


##********* Logic-7  *************
"""
def pickingNumbers(a):
    max_subset = 0
    for num in a:
        same = sum(map(lambda x: 1, filter(lambda x: x==num, a)))
        below = sum(map(lambda x: 1, filter(lambda x: x==num-1, a)))
        above = sum(map(lambda x: 1, filter(lambda x: x==num+1, a)))
        max_subset = max(max_subset, same+below, same+above)
    return max_subset
"""

##********* Logic-8  *************
"""
def pickingNumbers(a):
    # Write your code here
    freq = {}
    for number in a:
        if number in freq:
            freq[number] += 1
        else:
            freq[number] = 1
    
    max_length = 0
    
    for number in freq:
        current_length = freq[number]
        if number + 1 in freq:
            current_length += freq[number + 1]
        
        max_length = max(max_length, current_length)
    
    return max_length
"""

##********* Logic-9  *************
"""
def pickingNumbers(a):
    # Write your code here
    nums = sorted(a)
    nums_dict = Counter(nums)
    in_current = set()
    subs = []
    i = 0
    while len(nums) > 1 and i < len(nums) -1: # 1 1 2 2 2 3 |1,3,3,4,5,6
        in_current.add(nums[i])
        if len(in_current) > 1:
            subs.append(nums_dict(nums[i]))
            nums = nums[i+1:]
            i = 0
            in_current = set()
        elif abs(nums[i] - nums[i + 1]) == 1:
            subs.append(nums_dict[nums[i]] + nums_dict[nums[i+1]])
            until = nums_dict[nums[i+1]]
            nums = nums[i+until + 1:]
            i = 0
            in_current = set()
        elif abs(nums[i] - nums[i + 1]) > 1:
            subs.append(nums_dict[nums[i]])
            nums = nums[i+1:]
            i = 0
            in_current = set()
        else:
            i += 1
    subs.append(nums_dict[nums[0]]) if len(nums) > 0 else None

    return max(subs)
"""

##********* Logic-10  *************
"""
def pickingNumbers(a):
    # Write your code here
    hash_map = {}
    max_len = 0
    for i in a:
        if i in hash_map:
            hash_map[i] += 1
        else:
            hash_map[i] = 1
        # before the number
        if (i-1) in hash_map:       
            max_len = max(max_len, hash_map[i] + hash_map[i-1])
        # after the number
        if (i+1) in hash_map:       
            max_len = max(max_len, hash_map[i] + hash_map[i+1])
        # the exact number
        max_len = max(max_len, hash_map[i])     
    return max_len
"""
