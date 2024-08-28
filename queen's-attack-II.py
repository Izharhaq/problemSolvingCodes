"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()

"""
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
second_multiple_input = input().rstrip().split()
r_q = int(second_multiple_input[0])
c_q = int(second_multiple_input[1])
obstacles = []
for _ in range(k):
    obstacles.append(list(map(int, input().rstrip().split())))



def queensAttack(n, k, r_q, c_q, obstacles):
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1), # vertical and horizontal directions
        (-1, -1), (-1, 1), (1, -1), (1, 1) # diagonal directions
    ]
    
    obstacle_set = set(obstacles)
    attack_count = 0

    for dr, dc in directions:
        new_row, new_col = r_q + dr, c_q + dc
        while 1 <= new_row <= n and 1 <= new_col <= n:
            if (new_row, new_col) in obstacle_set:
                break
            attack_count += 1
            new_row += dr
            new_col += dc

    # return attack_count
    print(attack_count)

queensAttack(n, k, r_q, c_q, obstacles)









"""
def queensAttack(n, k, r_q, c_q, obstacles): 
    sum_attack_queen = 0 
    obstacles_set = set(tuple(obstacle) for obstacle in obstacles)
    

def count_attacks(dx, dy):
    count = 0
    x, y = r_q + dx, c_q + dy
    while 1 <= x <= n and 1 <= y <= n:
        if (x, y) in obstacles_set:
            break
        count += 1
        x += dx
        y += dy
    return count

# Directions (dx, dy)
directions = [
    (1, 0),   # up
    (-1, 0),  # down
    (0, 1),   # right
    (0, -1),  # left
    (1, 1),   # up-right
    (1, -1),  # up-left
    (-1, 1),  # down-right
    (-1, -1)  # down-left
]

for dx, dy in directions:
    sum_attack_queen += count_attacks(dx, dy)

return sum_attack_queen
"""

"""
# Define constants for directions
LEFT_INDEX = 0
DIAGONAL_LT_INDEX = 1
TOP_INDEX = 2
DIAGONAL_RT_INDEX = 3
RIGHT_INDEX = 4
DIAGONAL_RB_INDEX = 5
BOTTOM_INDEX = 6
DIAGONAL_LB_INDEX = 7

ROW_INDEX = 0
COLUMN_INDEX = 1

def queensAttack(n, k, r_q, c_q, obstacles):
    # Initialize the attack counter
    attack_slot_counter = 0

    # Make the default obstacles outside the board in 8 directions
    queen_obstacles = [
        [0, c_q],  # LEFT
        [(0 if (c_q + r_q) <= (n + 1) else (c_q + r_q - (n + 1))),
         (c_q + r_q if (c_q + r_q) <= (n + 1) else (n + 1))],  # LT
        [r_q, n + 1],  # TOP
        [(n + 1 if r_q >= c_q else n + 1 - (c_q - r_q)),
         (n + 1 if c_q >= r_q else n + 1 - (r_q - c_q))],  # RT
        [n + 1, c_q],  # RIGHT
        [(c_q + r_q if (c_q + r_q) <= (n + 1) else (n + 1)),
         (0 if (c_q + r_q) <= (n + 1) else (c_q + r_q - (n + 1)))],  # RB
        [r_q, 0],  # BOTTOM
        [(0 if c_q >= r_q else r_q - c_q),
         (0 if r_q >= c_q else c_q - r_q)]  # LB
    ]

    # Check if there are obstacles closer than those stored in queen_obstacles
    for obstacle in obstacles:
        row_o, col_o = obstacle
        
        if col_o == c_q:
            if row_o < r_q:  # LEFT
                if row_o > queen_obstacles[LEFT_INDEX][ROW_INDEX]:
                    queen_obstacles[LEFT_INDEX][ROW_INDEX] = row_o
            elif row_o > r_q:  # RIGHT
                if row_o < queen_obstacles[RIGHT_INDEX][ROW_INDEX]:
                    queen_obstacles[RIGHT_INDEX][ROW_INDEX] = row_o
        
        elif row_o == r_q:
            if col_o < c_q:  # BOTTOM
                if col_o > queen_obstacles[BOTTOM_INDEX][COLUMN_INDEX]:
                    queen_obstacles[BOTTOM_INDEX][COLUMN_INDEX] = col_o
            elif col_o > c_q:  # TOP
                if col_o < queen_obstacles[TOP_INDEX][COLUMN_INDEX]:
                    queen_obstacles[TOP_INDEX][COLUMN_INDEX] = col_o

        elif abs(row_o - r_q) == abs(col_o - c_q):  # Diagonal
            if row_o < r_q and col_o > c_q:  # LT
                if row_o > queen_obstacles[DIAGONAL_LT_INDEX][ROW_INDEX]:
                    queen_obstacles[DIAGONAL_LT_INDEX][ROW_INDEX] = row_o
                    queen_obstacles[DIAGONAL_LT_INDEX][COLUMN_INDEX] = col_o
            elif row_o > r_q and col_o > c_q:  # RT
                if row_o < queen_obstacles[DIAGONAL_RT_INDEX][ROW_INDEX]:
                    queen_obstacles[DIAGONAL_RT_INDEX][ROW_INDEX] = row_o
                    queen_obstacles[DIAGONAL_RT_INDEX][COLUMN_INDEX] = col_o
            elif row_o > r_q and col_o < c_q:  # RB
                if row_o < queen_obstacles[DIAGONAL_RB_INDEX][ROW_INDEX]:
                    queen_obstacles[DIAGONAL_RB_INDEX][ROW_INDEX] = row_o
                    queen_obstacles[DIAGONAL_RB_INDEX][COLUMN_INDEX] = col_o
            elif row_o < r_q and col_o < c_q:  # LB
                if row_o > queen_obstacles[DIAGONAL_LB_INDEX][ROW_INDEX]:
                    queen_obstacles[DIAGONAL_LB_INDEX][ROW_INDEX] = row_o
                    queen_obstacles[DIAGONAL_LB_INDEX][COLUMN_INDEX] = col_o
    
    # Calculate the differences between obstacles and the queen's position
    attack_slot_counter += r_q - queen_obstacles[LEFT_INDEX][ROW_INDEX] - 1
    attack_slot_counter += queen_obstacles[RIGHT_INDEX][ROW_INDEX] - r_q - 1
    attack_slot_counter += queen_obstacles[TOP_INDEX][COLUMN_INDEX] - c_q - 1
    attack_slot_counter += c_q - queen_obstacles[BOTTOM_INDEX][COLUMN_INDEX] - 1
    attack_slot_counter += queen_obstacles[DIAGONAL_LT_INDEX][COLUMN_INDEX] - c_q - 1
    attack_slot_counter += queen_obstacles[DIAGONAL_RT_INDEX][COLUMN_INDEX] - c_q - 1
    attack_slot_counter += c_q - queen_obstacles[DIAGONAL_RB_INDEX][COLUMN_INDEX] - 1
    attack_slot_counter += c_q - queen_obstacles[DIAGONAL_LB_INDEX][COLUMN_INDEX] - 1
    
    return attack_slot_counter

"""


"""
def queensAttack(n, k, r_q, c_q, obstacles):
    # Initialize maximum distances the queen can move in all 8 directions
    left = c_q - 1
    right = n - c_q
    up = n - r_q
    down = r_q - 1
    up_left = min(up, left)
    up_right = min(up, right)
    down_left = min(down, left)
    down_right = min(down, right)

    # Adjust the maximum distances based on the positions of obstacles
    for obstacle in obstacles:
        row_o, col_o = obstacle

        # Same column (vertical direction)
        if col_o == c_q:
            if row_o < r_q:  # Obstacle below the queen
                down = min(down, r_q - row_o - 1)
            elif row_o > r_q:  # Obstacle above the queen
                up = min(up, row_o - r_q - 1)

        # Same row (horizontal direction)
        elif row_o == r_q:
            if col_o < c_q:  # Obstacle to the left of the queen
                left = min(left, c_q - col_o - 1)
            elif col_o > c_q:  # Obstacle to the right of the queen
                right = min(right, col_o - c_q - 1)

        # Diagonal directions
        elif abs(row_o - r_q) == abs(col_o - c_q):
            if row_o < r_q and col_o < c_q:  # Obstacle in the bottom-left diagonal
                down_left = min(down_left, r_q - row_o - 1)
            elif row_o < r_q and col_o > c_q:  # Obstacle in the bottom-right diagonal
                down_right = min(down_right, r_q - row_o - 1)
            elif row_o > r_q and col_o < c_q:  # Obstacle in the top-left diagonal
                up_left = min(up_left, row_o - r_q - 1)
            elif row_o > r_q and col_o > c_q:  # Obstacle in the top-right diagonal
                up_right = min(up_right, row_o - r_q - 1)

    # Sum up all possible moves
    return left + right + up + down + up_left + up_right + down_left + down_right

"""