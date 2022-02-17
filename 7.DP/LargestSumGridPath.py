# find path only moving down and right from top left to bottom right that has the largest sum in grid

grid = [
    [3,7,9,2,7],
    [9,8,3,5,5],
    [1,7,9,8,5],
    [3,8,6,4,10],
    [6,3,9,7,8]
]

dp = [[0]*len(grid) for i in range(len(grid))]

def solve(x,y):
    if dp[x][y]!=0:
        return dp[x][y]

    if x==0 and y==0: #base case
        dp[x][y] = grid[x][y]
        return grid[x][y]

    if x==0: #edge case
        dp[x][y] = solve(x,y-1) + grid[x][y]
        return dp[x][y]
    elif y==0: #edge case
        dp[x][y] = solve(x-1,y) + grid[x][y]
        return dp[x][y]
    
    dp[x][y] = max(solve(x-1,y),solve(x,y-1)) + grid[x][y]
    return dp[x][y]

res = solve(len(grid)-1,len(grid)-1)
print(res)