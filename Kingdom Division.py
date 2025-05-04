"""
#!/bin/python3

import math
import os
import random
import re
import sys
sys.setrecursionlimit(10**6)

MOD = 10**9 + 7

#
# Complete the 'kingdomDivision' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY roads
#

def kingdomDivision(n, roads):
    # Write your code here
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    roads = []

    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))

    result = kingdomDivision(n, roads)

    fptr.write(str(result) + '\n')

    fptr.close()

"""

#!/bin/python3

import math
import os
import random
import re
import sys
sys.setrecursionlimit(10**6)

MOD = 10**9 + 7

#
# Complete the 'kingdomDivision' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY roads
#

sys.setrecursionlimit(100000)

modulus = 10**9 + 7

# Return the number of ways that this subtree can be allocated if its root
#   has 1. the opposite assignment as its parent and 2. the same assignment
def ways(node, parent, edges):
    # children are all neighbors except the parent
    children = edges[node]
    if parent:
        children.remove(parent)
    
    # we keep track of "lonely_ways", the number of ways that all subtree can
    #   be assigned with opposite root assignments
    #   (because if they're all opposite, this node must be the same as its parent)
    lonely_ways = 1
    # keep track of the total number of ways: product of # of ways for subtrees
    total_ways = 1
    
    for child in children:
        (diff, same) = ways(child, node, edges)
        lonely_ways = (lonely_ways * diff) % modulus
        total_ways = (total_ways * (same + diff)) % modulus
    
    # if we're different from our parent, we cannot include cases where we're
    #   also different from all of our children
    return (total_ways - lonely_ways, total_ways)

def kingdomDivision(n, roads):
    # Write your code here
    edges = dict()
    for a, b in roads:
        edges.setdefault(a, set()).add(b)
        edges.setdefault(b, set()).add(a)

    # Depth-first recurssion of the tree rooted at 1 (root has None parent)
    (diff, same) = ways(1, None, edges)
    
    # "diff" is the now number of ways to assign the whole tree without a lonely
    #   root, given a root of a fixed assignment.
    # Multiply by 2 for # of root assignments
    return (2 * diff) % modulus
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    roads = []

    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))

    result = kingdomDivision(n, roads)

    fptr.write(str(result) + '\n')

    fptr.close()



"""
sys.setrecursionlimit(100000)

modulus = 10**9 + 7

# Return the number of ways that this subtree can be allocated if its root
#   has 1. the opposite assignment as its parent and 2. the same assignment
def ways(node, parent, edges):
    # children are all neighbors except the parent
    children = edges[node]
    if parent:
        children.remove(parent)
    
    # we keep track of "lonely_ways", the number of ways that all subtree can
    #   be assigned with opposite root assignments
    #   (because if they're all opposite, this node must be the same as its parent)
    lonely_ways = 1
    # keep track of the total number of ways: product of # of ways for subtrees
    total_ways = 1
    
    for child in children:
        (diff, same) = ways(child, node, edges)
        lonely_ways = (lonely_ways * diff) % modulus
        total_ways = (total_ways * (same + diff)) % modulus
    
    # if we're different from our parent, we cannot include cases where we're
    #   also different from all of our children
    return (total_ways - lonely_ways, total_ways)

def kingdomDivision(n, roads):
    edges = dict()
    for a, b in roads:
        edges.setdefault(a, set()).add(b)
        edges.setdefault(b, set()).add(a)

    # Depth-first recurssion of the tree rooted at 1 (root has None parent)
    (diff, same) = ways(1, None, edges)
    
    # "diff" is the now number of ways to assign the whole tree without a lonely
    #   root, given a root of a fixed assignment.
    # Multiply by 2 for # of root assignments
    return (2 * diff) % modulus

"""