# number of ways possible to solve queens on chessboard problem, on a nxn board
import time
class backtrackQueens:
    def __init__(self,n):
        self.count = 0
        self.n = n
        self.cols = [[] for i in range(n)]
        self.diag1 = [[] for i in range(n)]
        self.diag2 = [[] for i in range(n)]

        #creating board / queen controls
        #cols,diag1
        for i in range(n):
            for j in range(n):
                self.cols[i].append(j)
                self.diag1[i].append(i+j)

        #diag2
        for i in range(n-1,-1,-1):
            for j in range(n):
                self.diag2[i].append(n-1-i+j)
        
        self.column = [0]*n
        self.diagonal1 = [0]*(n*2-1)
        self.diagonal2 = [0]*(n*2-1)

    def search(self,y):
        if y == self.n:
            self.count+=1
            return
        for i in range(self.n):
            if self.column[i] or self.diagonal1[i+y] or self.diagonal2[i-y+self.n-1]:
                continue
            self.column[i] = 1
            self.diagonal1[i+y] = 1
            self.diagonal2[i-y+self.n-1] = 1

            self.search(y+1)

            self.column[i] = 0
            self.diagonal1[i+y] = 0
            self.diagonal2[i-y+self.n-1] = 0

test = backtrackQueens(16)

start = time.time()
test.search(0)
end = time.time()
print(test.count)
print(end-start)