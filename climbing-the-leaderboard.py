"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    #***** IZHAR CODE *************
    # Remove duplicates and keep the ranking in descending order
    unique_scores = list(dict.fromkeys(ranked))  # Preserves order while removing duplicates
    results = []
    index = len(unique_scores)  # Start from the lowest rank
    
    for score in player:
        # Move up the leaderboard while Alice's score is greater or equal
        while index > 0 and score >= unique_scores[index - 1]:
            index -= 1
        # Alice's rank is index + 1 (since it's 1-based ranking)
        results.append(index + 1)
    
    return results

    #***** IZHAR CODE *************

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

"""
