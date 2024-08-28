
q = int(input())

for q_itr in range(q):
    xyz = input().split()
    x = int(xyz[0])
    y = int(xyz[1])
    z = int(xyz[2])


def catAndMouse(x, y, z):
    if abs(z-x) < abs(z-y):
        print("Cat A")
    elif abs(z-x) > abs(z-y):
        print("Cat B")
    else:
        print("Mouse C")


catAndMouse(x, y, z)


"""
def catAndMouse(x, y, z): 
    if abs(x-z)>abs(y-z): 
        return "Cat B" 
    elif abs(x-z)==abs(y-z): 
        return "Mouse C" 
    else: 
        return "Cat A"
"""