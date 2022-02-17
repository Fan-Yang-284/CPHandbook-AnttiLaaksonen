import time
grid = [[0]*4 for i in range(7)] # 4x7 rotated to 7x4 to reduce time complexity

tiles = ["u","d","l","r"] # up,down,left,right

strs = set()

total = 0

def getStrings(n,perm):
    if n==len(grid[0]):
        if checkStr(perm):
            strs.add(perm)
    else:
        for i in tiles:
            getStrings(n+1,perm+i)
        
def checkStr(perm):
    for i in range(len(perm)):
        if perm[i] == "l":
            if i == len(perm)-1:
                return False
            elif perm[i+1]!= "r":
                return False
        if perm[i] == "r":
            if i == 0:
                return False
            elif perm[i-1]!="l":
                return False
    return True

def check(i,j): #i ,j are row strings, where i is in row above j
    for a in range(len(i)):
        if i[a] == "u":
            if j[a] != "d":
                return False
        elif j[a] == "d": #don't check if previous was checked, redundant
            if i[a] !="u":
                return False # only condition is that an up tile must be matched with down tile in row below
    return True

def count(k,x): # denotes the # of ways to construct solution for rows 1->k with a given string x on row k
    if k == 1: # if k is first row, only condition is that no down tile
        if "d" not in x:
            return 1
        return 0
    elif k == len(grid): # if k is last row, cannot have an up tile
        if "u" in x:
            return 0
    num = 0
    for str in strs:
        if check(str,x):
            num+=count(k-1,str) 
            # equals the number of ways to arrange previos k-1 row
            # such that the k-1th row is compatible with the kth row
    
    return num

getStrings(0,"")

start = time.time()

for str in strs:
    total+=count(len(grid),str)

end = time.time()

print(end-start)
print(total)
