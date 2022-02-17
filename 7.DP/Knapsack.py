weights = [0,1,3,3,5]

dp = [False]*(sum(weights)+1)
dp[0] = True

# dp[i] stores whether a sum i can be made with the weights

for i in range(1,len(weights)):
    for j in range(sum(weights),-1,-1):
        if dp[j] and j+weights[i]<len(dp):
            dp[j+weights[i]] = True
print(dp)
print(dp[sum(weights)])