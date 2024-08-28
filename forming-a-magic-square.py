def formingMagicSquare(s):
    patterns = [
        [[8,1,6],[3,5,7],[4,9,2]],
        [[6,1,8],[7,5,3],[2,9,4]],
        [[4,9,2],[3,5,7],[8,1,6]],
        [[2,9,4],[7,5,3],[6,1,8]],
        [[8,3,4],[1,5,9],[6,7,2]],
        [[4,3,8],[9,5,1],[2,7,6]],
        [[6,7,2],[1,5,9],[8,3,4]],
        [[2,7,6],[9,5,1],[4,3,8]],
        ]
    
    # collect all the cost
    costList = []
    
    for data in patterns:
        gap1 = abs(s[0][0] - data[0][0])
        gap2 = abs(s[0][1] - data[0][1])
        gap3 = abs(s[0][2] - data[0][2])
        gap4 = abs(s[1][0] - data[1][0])
        gap5 = abs(s[1][1] - data[1][1])
        gap6 = abs(s[1][2] - data[1][2])
        gap7 = abs(s[2][0] - data[2][0])
        gap8 = abs(s[2][1] - data[2][1])
        gap9 = abs(s[2][2] - data[2][2])
        
        # count all cost
        cost = gap1 + gap2 + gap3 + gap4 + gap5 + gap6 + gap7 + gap8 + gap9
        costList.append(cost)
    
    # return the minimal cost
    return min(costList)



"""
magic_squares = [ 
    [8,1,6,3,5,7,4,9,2], 
    [6,1,8,7,5,3,2,9,4], 
    [4,9,2,3,5,7,8,1,6], 
    [2,9,4,7,5,3,6,1,8], 
    [8,3,4,1,5,9,6,7,2], 
    [4,3,8,9,5,1,2,7,6], 
    [6,7,2,1,5,9,8,3,4], 
    [2,7,6,9,5,1,4,3,8], 
    ] 
    s_flat = [s[i][j] 
    for i in range(3) for j in range(3)] min_cost = float('inf') for magic in magic_squares: 
        cost = sum(abs(s_flat[i] - magic[i]) for i in range(9)) if cost < min_cost: 
        min_cost = cost  return min_cost
"""


"""
magic_squares = [
    [8, 1, 6, 3, 5, 7, 4, 9, 2],
    [6, 1, 8, 7, 5, 3, 2, 9, 4],
    [4, 9, 2, 3, 5, 7, 8, 1, 6],
    [2, 9, 4, 7, 5, 3, 6, 1, 8],
    [8, 3, 4, 1, 5, 9, 6, 7, 2],
    [4, 3, 8, 9, 5, 1, 2, 7, 6],
    [6, 7, 2, 1, 5, 9, 8, 3, 4],
    [2, 7, 6, 9, 5, 1, 4, 3, 8]
]
input = [number for row in s for number in row]
mincost = float('inf')

for square in magic_squares:
    cost = sum(abs(a - b) for a,b in zip(input, square))
    if cost < mincost:
        mincost = cost
return mincost
"""