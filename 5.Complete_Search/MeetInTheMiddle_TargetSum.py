# target sum problem using subsets 
from random import randint

arr = []

for i in range(8):
    arr.append(randint(0,20))

arr.sort()

l,r = 0,len(arr)
mid =(l+r)//2

left = arr[l:mid]
right = arr[mid:r]

leftSubs = []
rightSubs = []

def getPerms(k,length,perm,i):
    if k == length:
        if i == 0:
            leftSubs.append(perm[:])
        else:
            rightSubs.append(perm[:])
    else:
        getPerms(k+1,length,perm,i) # not included in subset

        if i == 0: 
            perm.append(left[k])
        else:
            perm.append(right[k])

        getPerms(k+1,length,perm,i) # included in subset
        perm.pop() # what does this do????

getPerms(0,len(left),[],0)
getPerms(0,len(right),[],1)

leftSubs = sorted(list(map(lambda x:sum(x), leftSubs)))
rightSubs = sorted(list(map(lambda x:sum(x), rightSubs)))

target = 70

def find():
    for i in range(len(leftSubs)):
        x = target - leftSubs[i]

        #binary search
        l, r = 0,len(rightSubs)-1

        while(l<=r):
            mid = (l+r)//2
            if rightSubs[mid] == x:
                return rightSubs[mid]
            elif rightSubs[mid]<x:
                l=mid+1
            else:
                r=mid-1
        
    return -1

found = find()>=0
print(leftSubs)
print(rightSubs)
print(found)


