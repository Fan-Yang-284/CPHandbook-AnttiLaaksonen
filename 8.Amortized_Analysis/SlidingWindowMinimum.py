#find min val in each subarray of given size in an array

from collections import deque
size = 4
arr = [2,1,4,5,3,4,1,2]

l,r, = 0,size

dq = deque()
dq.append((arr[0],0))

for i in range(1,r):
    while dq and arr[i]<dq[-1][0]:
        dq.pop()
    dq.append((arr[i],i))
#print(dq)
print([l,r,dq[0][0]])

while r<len(arr):
    l,r=l+1,r+1
    if dq[0][0]<l:
        dq.popleft()
    while len(dq)!=0 and arr[r-1]<dq[-1][0]:
        dq.pop()
    dq.append((arr[r-1],r-1))
    #print(dq)
    print([l,r,dq[0][0]])