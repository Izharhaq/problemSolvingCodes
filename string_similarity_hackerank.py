###### ***** This code is okay but in few test case it was failing because of less optimization ****888

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stringSimilarity' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def stringSimilarity(s):
    # Write your code here
    ###*******IZHAR CODE ****************
    total_similarity = 0
    n = len(s)

    for i in range(n):
        suffix = s[i:]
        common_length = 0

        for j in range(len(suffix)):
            if s[j] == suffix[j]:
                common_length += 1
            else:
                break


        total_similarity += common_length

    return total_similarity
    
    ###*******IZHAR CODE ****************

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = stringSimilarity(s)

        fptr.write(str(result) + '\n')

    fptr.close()


##################################
## **** For More Otimization in few test case I used Z- Algorithm *****
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stringSimilarity' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def stringSimilarity(s):
    # Write your code here
    ###*******IZHAR CODE ****************

    n = len(s)
    Z = [0] * n
    l, r, K = 0, 0, 0
    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and s[r] == s[r - l]:
                r += 1
            Z[i] = r - l
            r -= 1
        else:
            K = i - l
            if Z[K] < r - i + 1:
                Z[i] = Z[K]
            else:
                l = i
                while r < n and s[r] == s[r - l]:
                    r += 1
                Z[i] = r - l
                r -= 1

    total_similarity = n + sum(Z)
    return total_similarity

    ###*******IZHAR CODE ****************
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = stringSimilarity(s)

        fptr.write(str(result) + '\n')

    fptr.close()


'''