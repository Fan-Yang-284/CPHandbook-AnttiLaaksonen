# determine if in arr there exists a subarray that sums to target sum

from random import randint


arr = [1,3,2,5,1,1,2,3]
target = randint(0,sum(arr))
print(target)
l,r = 0,0
found = False
while l<len(arr):
    while r+1<=len(arr) and sum(arr[l:r+1])<=target:
        r+=1
    if sum(arr[l:r]) == target:
        found = True
        break
    l+=1

print(found)
print((l,r))