# determine number of operations (add,remove or edit letters) that distance two strings

x = "LOVE"
y = "MOVIE"
n,m = len(x),len(y)

def distance(a,b):
    if a == b == -1:
        return 0
    elif a == -1:
        return b+1
    elif b == -1:
        return a+1
    return min(distance(a,b-1)+1,distance(a-1,b)+1,distance(a-1,b-1)+cost(a,b))

def cost(a,b):
    if x[a]==y[b]:
        return 0
    return 1

dist = distance(n-1,m-1)
print(dist)