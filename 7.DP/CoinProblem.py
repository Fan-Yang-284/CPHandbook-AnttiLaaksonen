# determine min number of coins needed to make given number n

import time

coins = [1,2,5,10,25,50,100,500]

class coinProblem:
    def __init__(self,n):
        self.memo = [0]*(n+1)
        self.first = [""]*(n+1)
        self.n = n
        self.solve(self.n)

    def solve(self,n):
        for i in range(1, n+1):
            self.memo[i] = float('inf')
            for c in coins:
                if i-c>=0 and self.memo[i-c]+1<self.memo[i]:
                    self.memo[i] = self.memo[i-c]+1
                    self.first[i] = c
                
    def getSolution(self,n):
        print(self.memo[n])
        res = ""
        while n>0:
            res+=str(self.first[n]) +" "
            n-=self.first[n]
        print(res)

start = time.time()
test = coinProblem(1000)
end = time.time()
test.getSolution(test.n)
print(end-start)