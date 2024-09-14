"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    list_of_max_words = []
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for i in word:
        index = alphabets.index(i)
        list_of_max_words.append(h[index])
    return max(list_of_max_words)*len(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()

"""



####****** APPROCHES *********
# 1. Iterate to read letter index from given letter dictionary.
# 2. With the help of that dictionary, read height from the given list.
# 3. Find the max height of the given word
# 4. Find length of the given word
# 5. Calculate the area and rerurn it.

#######************ Logic-1 **********
h = [1,3,1,3,1,4,1,3,2,5,5,5,5,1,1,5,5,1,5,2,5,5,5,5,5,5]
word = "python"

def designerPdfViewer(h, word):
    list_of_max_words = []
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for i in word:
        index = alphabets.index(i)
        list_of_max_words.append(h[index])
    # return max(list_of_max_words)*len(word)
    print(max(list_of_max_words)*len(word))

designerPdfViewer(h, word)




########******** Logic -2 ************


# h = list(map(int, input().rstrip().split()))
# word = input()
# h = [1,3,1,3,1,4,1,3,2,5,5,5,5,1,1,5,5,1,5,2,5,5,5,5,5,5]
# word = "python"

# def designerPdfViewer(h, word):
#     na=[]
#     s='abcdefghijklmnopqrstuvwxyz'
#     for i in word:
#         a=s.index(i)
#         na.append(h[a])
#     # return max(na)*len(word)
#     print(max(na)*len(word))
# designerPdfViewer(h, word)



#*******************Logic - 3 **************
"""
def designerPdfViewer(h, word):
    true_index = [(ord(i)-97) for i in word]
    x = list(map((lambda j: h[j]), true_index))
    return max(x)*len(word)
"""
