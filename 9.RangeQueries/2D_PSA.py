arr = [[1,3,4,8,6,1,4,2] for _ in range(4)]

PSA = [[] for _ in range(len(arr))]

PSA[0].append(arr[0][0])

for i in range(1,len(arr[0])):
    PSA[0].append(PSA[0][i-1]+arr[0][i])

for i in range(1,len(arr)):
    PSA[i].append(PSA[i-1][0]+arr[i][0])

#print(PSA)

for i in range(1,len(arr)):
    for j in range(1,len(arr[0])):
        PSA[i].append(PSA[i][0]*PSA[0][j])

for i in range(len(PSA)):
    print(PSA[i])

# get Sum of rectangle from (a,b) to (c,d), where c>a, d>b 
# using PSA[c,d] - PSA[c,b] - PSA[b,d] + PSA[a,b]

def sum(a,b,c,d):
    return PSA[c][d] - PSA[c][b] - PSA[b][d] + PSA[a][b]

print(sum(1,1,3,3))