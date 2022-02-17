arr = [1,3,4,8,6,1,4,2]

psa = [arr[0]]

for i in range(1,len(arr)):
    psa.append(psa[i-1]+arr[i])

print(psa)

#to determine sum(a,b): psa[b] - psa[a-1]

def sum(a,b):
    if a == 0:
        return psa[b]
    return psa[b]-psa[a-1]

print(sum(0,7))
print(sum(3,6))