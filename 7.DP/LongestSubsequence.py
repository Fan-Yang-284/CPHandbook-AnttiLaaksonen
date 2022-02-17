#find longest increasing subsequence in an array of n elements

arr = [6, 2, 5, 1, 7, 4, 8, 3]

length = [0]*len(arr)

for i in range(len(arr)):
    length[i] = 1
    for j in range(i):
        if arr[j]<arr[i]:
            length[i]=max(length[i],length[j]+1)

print(length)