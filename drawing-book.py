n = int(input().strip())
p = int(input().strip())

def pageCount(n, p):
    no_front = p//2
    # print(no_front)
    if n % 2 ==0:
        no_back = (n-p+1)//2
        # print(no_back)
    else:
        no_back = (n-p)//2
        # print(no_back)

    # print(min(no_front, no_back))
    return min(no_front, no_back)


pageCount(n, p)

