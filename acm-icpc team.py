"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Write your code here
    #******** Izhar code ******
    max_solved = 0
    team_count = 0

    n = len(topic)
    
    for i in range(n):
        for j in range(i + 1, n):
            combined = int(topic[i], 2) | int(topic[j], 2)
            solved_count = bin(combined).count('1')
            
            if solved_count > max_solved:
                max_solved = solved_count
                team_count = 1
            elif solved_count == max_solved:
                team_count += 1

    return [max_solved, team_count]

    #***** Izhar code ***************

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

"""


"""
def acmTeam(topic):
    max_solved = 0
    team_count = 0

    n = len(topic)
    
    for i in range(n):
        for j in range(i + 1, n):
            combined = int(topic[i], 2) | int(topic[j], 2)
            solved_count = bin(combined).count('1')
            
            if solved_count > max_solved:
                max_solved = solved_count
                team_count = 1
            elif solved_count == max_solved:
                team_count += 1

    return [max_solved, team_count]

"""


"""
topic = [
    "10101",  # Person 1's solved problems
    "11100",  # Person 2's solved problems
    "11010",  # Person 3's solved problems
    "00101"   # Person 4's solved problems
]
def acmTeam(topic):
    max_solved = 0  # to store the maximum number of problems solved by any pair

    n = len(topic)  # number of people (rows)
    m = len(topic[0])  # number of problems (columns)

    # Iterate over all pairs of people
    for i in range(n):
        for j in range(i + 1, n):  # j starts from i+1 to avoid duplicate pairs
            # Combine the solutions of person i and person j using OR
            combined = int(topic[i], 2) | int(topic[j], 2)
            # Count the number of '1's in the combined result
            solved_count = bin(combined).count('1')
            # Track the maximum number of problems solved
            max_solved = max(max_solved, solved_count)

    return max_solved


print(acmTeam(topic))
"""