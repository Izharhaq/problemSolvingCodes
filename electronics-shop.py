bnm = input().split()
b = int(bnm[0])
n = int(bnm[1])
m = int(bnm[2])
keyboards = list(map(int, input().rstrip().split()))
drives = list(map(int, input().rstrip().split()))

# 10 2 3
# 3 1
# 5 2 8


def getMoneySpent(keyboards, drives, b):
    items=[]
    for i in keyboards:
        for j in drives:
            if (i+j)<=b:
                items.append(i+j)
    if len(items) != 0:
        # return max(items)
        print(max(items))
    else:
        # return -1
        print("-1")

getMoneySpent(keyboards, drives, b)
