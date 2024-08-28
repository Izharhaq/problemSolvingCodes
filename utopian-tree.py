#************logic-1 ********** Working fine*********
"""
t = int(input().strip())
for t_itr in range(t):
    n = int(input().strip())
def utopianTree(n):
    height = 1
    for p in range(1, n+1):
        if p % 2 == 0:
            height += 1
        else:
            height *= 2

    # return height
    print(height)

utopianTree(n)
"""

#***********logic-2***********Working fine********
"""
t = int(input().strip())
for t_itr in range(t):
    n = int(input().strip())
def utopianTree(n):
    count=0 
    for i in range(n+1): 
        if i==0: 
            count+=1 
        elif i%2==0 or i==1: 
            count+=1 
        elif i%2==1: 
            count*=2
    # return count
    print(count)
utopianTree(n)
"""


#************ Logic-3 ************working fine *********8
"""
t = int(input().strip())
for t_itr in range(t):
    n = int(input().strip())
def utopianTree(n):
    height = 1
    for p in range(1, n+1):
        if p % 2 == 0:
            height += 1
        else:
            height *= 2

    return height
"""

#************ Logic-4 **********Working fine *******
"""
t = int(input().strip())
for t_itr in range(t):
    n = int(input().strip())
def utopianTree(n):
    height = 0
    for i in range(n+1):
        if i == 0:
            height += 1
        elif i%2==0 or i==1:
            height += 1
        elif i%2==1:
            height *= 2 
    # return height    
    print(height)

utopianTree(n)
"""