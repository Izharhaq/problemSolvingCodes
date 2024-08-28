
n = int(input().strip())
ar = list(map(int, input().rstrip().split()))
def sockMerchant(n, ar): 
    # Write your code here
    # Here we need key value pair so we use dict.
    color_dic={} 
    count=0 
    for i in ar: 
        if i in color_dic.keys(): 
            color_dic[i]+=1 
        else: 
            color_dic[i]=1
    for i in color_dic: 
        count+=color_dic[i]//2
    print(count)
    # return count
    
sockMerchant(n, ar)




#*********** Logic-2 ************
"""
import math
n = int(input().strip())
ar = list(map(int, input().rstrip().split()))

def sockMerchant(n, ar):
    hashmap = dict()
    pairs = 0
    for sock in ar:
        if sock in hashmap:
            hashmap[sock] +=1
        else:
            hashmap[sock] = 1
    for key in hashmap.keys():
        pairs += math.floor(hashmap[key]/2)

    # return int(pairs)
    print(int(pairs))
sockMerchant(n, ar)
"""



##********** Logic -3 **********

"""
n = int(input().strip())
ar = list(map(int, input().rstrip().split()))

def sockMerchant(n, ar):
    total = 0
    ar.sort()
    dic = {}
    for i in ar:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in dic.values():
        total += i // 2
    # return total
    print(total)
sockMerchant(n, ar)
"""

###****** APPROACHES ************