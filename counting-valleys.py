# steps = 8
# path = "UUDDUDUU"

steps = int(input().strip())
path = input()

def countingValleys(steps, path):
    sea_level = 0
    current_level = 0
    valleys = 0

    for i in path:
        if i == 'U':
            current_level += 1
        elif i == 'D':
            current_level -= 1
        
        if current_level == 0 and i == 'U': # Check if just came up to sea level from a valley
            valleys += 1
    
    # return valleys
    print(valleys)

countingValleys(steps, path)

##*********** Logic-2 *****************

"""
def countingValleys(steps, path): 
    level = 0 
    previouslevel = 0 
    valley = 0 
    for i in range(steps): 
        if path[i] == 'U': 
            level = level + 1 
        if path[i] == 'D': 
            level = level - 1 
        if previouslevel < 0 and level >= 0: 
            valley = valley + 1 
            previouslevel = level 
    return valley
"""


####***** Logic-3 ***********
"""
def countingValleys(steps, path):
    sea_level = 0
    is_in_valley = False
    valleys = 0
    for p in path:
        if p == 'D':
            sea_level -= 1
            if sea_level < 0 and not is_in_valley:
                is_in_valley = True
                valleys += 1
        else:
            sea_level += 1
            if sea_level >= 0:
                is_in_valley = False   
    return valleys
"""