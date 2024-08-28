"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    #**** IZHAR CODE *********
    likes = 0
    shared_people = 5
    for i in range(1, n+1):
        likes += shared_people//2
        shared_people= (shared_people//2)*3
    # return likes

    #******* IZHAR CODE ***********


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

"""

n = int(input().strip())
# n = 3
def viralAdvertising(n):
    likes = 0
    shared_people = 5
    for i in range(1, n+1):
        likes += shared_people//2
        shared_people= (shared_people//2)*3
    # return likes
    print(likes)
    
viralAdvertising(n)



"""
def viralAdvertising(n):
    # Write your code here
    slz = 0
    shared = 5
    for i in range(1, n + 1):
        slz += shared // 2
        shared = (shared // 2) * 3
    return slz
"""

"""
def viralAdvertising(n):
    # Write your code here
    liked = [2]
    for i in range(1,n):
        liked.append(math.floor(liked[-1]*3/2))
    return sum(liked)
"""


"""
def viralAdvertising(n):
    liked = 2
    c_start = 5
    c_liked = 2
    for i in range(2, n+1):
        c_start = c_liked*3
        c_liked = c_start//2
        liked += c_liked
    return liked
"""


"""
class People:
    def __init__(self, received):
        self.received = received
        self.liked = 0
    
    def calculate_likes(self):
        self.liked = self.received // 2
        return self.liked
    
    def get_next_day_receivers(self):
        return self.liked * 3


class Day:
    def __init__(self, day_number, received):
        self.day_number = day_number
        self.people = People(received)
    
    def process_day(self):
        likes = self.people.calculate_likes()
        next_day_receivers = self.people.get_next_day_receivers()
        return likes, next_day_receivers


class AdvertisingCampaign:
    def __init__(self, total_days):
        self.total_days = total_days
        self.cumulative_likes = 0
        self.initial_receivers = 5
    
    def run_campaign(self):
        current_receivers = self.initial_receivers
        for day_number in range(1, self.total_days + 1):
            day = Day(day_number, current_receivers)
            likes, next_day_receivers = day.process_day()
            self.cumulative_likes += likes
            current_receivers = next_day_receivers
        return self.cumulative_likes

"""


"""
def viralAdvertising(n):
    l=r=0
    a=5
    for i in range(n):
        r=a//2
        a= r*3
        l+=r    
    return l
"""


"""
def viralAdvertising(n):
    k=5
    d=0
    for i in range(2,n+2):
        d+=k//2
        k=(k//2)*3
    return d
"""