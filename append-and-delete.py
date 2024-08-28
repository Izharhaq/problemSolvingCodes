s = input()
t = input()
k = int(input().strip())

# s = [a,b,c]
# t = [d,e,f]
# k = 6

def appendAndDelete(s, t, k):
    if len(s) + len(t) <= k:
        return 'Yes'
        # print("Yes")
    
    else:
        t = list(t)
        s = list(s)
        for i in range(k):
            if len(t) > len(s):
                t.pop()
            else:
                s.pop()
        if s == t:
            return 'Yes'
            # print("Yes")
        return 'No'
        # print("No")
    
# appendAndDelete(s, t, k)

#******************************************************************



