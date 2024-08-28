############### APPROCHES *************
"""
1. find the max heights
2. compare with given height k
    2(a). If  k<height....abs(max_height - k)
    2(b). If k>= max height..... return 0

"""
######*************
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
height = list(map(int, input().rstrip().split()))
def hurdleRace(k, height):

    max_height=max(height)
    if max_height>k:
        # return max_height-k
        print(max_height-k)
    if max_height<=k:
        # return 0
        print("0")
            
hurdleRace(k, height)


"""
def hurdleRace(k, height):
    a=max(height)
    if a>k:
        return a-k
    if a<=k:
        return 0
"""


"""
def hurdleRace(k, height):
    if k > max(height):
        return 0
    return max(height) - k

"""

"""
def hurdleRace(k, height):
    return max(0, max(height)-k)
"""


"""
def hurdleRace(k, height):
    # Write your code here
    return max(height) - k if (max(height) - k) > 0 else 0
"""

"""
def hurdleRace(k, height):
    return 0 if k>=max(height) else  max(height)-k
"""

"""
def hurdleRace(k, height):
    return max(height)-k if max(height)>k else 0
"""

"""
def hurdleRace(k, height):
    # Write your code here
    height.sort()
    if k<height[-1]:
        return height[-1]-k
    else:
        return 0
"""