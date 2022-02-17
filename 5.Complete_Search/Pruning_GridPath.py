#find number of non-intersecting unique paths in a nxn grid
import time

class gridPath:
    def __init__(self,n):
        self.n = n

        self.count1 = 0
        self.count2 = 0
        self.count3 = 0
        self.count4 = 0
        self.count5 = 0

        self.length = self.n**2
        self.target = (self.n-1,self.n-1)

        self.visited = set([(0,0),(0,1)])
        self.path = [(0,0),(0,1)]

    def getNeighbours(self):
        neighbours = []
        cell = self.path[-1]
        for i in range(cell[0]-1,cell[0]+2):
            if i<0 or i>=self.n:
                continue
            for j in range(cell[1]-1, cell[1]+2):
                if j<0 or j>=self.n:
                    continue
                if abs(i-cell[0])+abs(j-cell[1])!=1:
                    continue
                if (i,j) not in self.visited:
                    neighbours.append((i,j))
        return neighbours
                
    def getPaths1(self,path): #basic algorithm
        if len(path) == self.n**2: 
            if path[-1] == (self.n-1,self.n-1):
                self.count1+=1
            return
        elif path[-1] == (self.n-1,self.n-1):
            return
        for n in self.getNeighbours(path):
            path.append(n)
            self.getPaths1(path)
            path.pop()
            

    def getPaths2(self,path): #optimization 1: symmetry
        if len(path) == self.n**2: 
            if path[-1] == (self.n-1,self.n-1):
                self.count2+=1
            return
        elif path[-1] == (self.n-1,self.n-1):
            return
        for n in self.getNeighbours(path[-1]):
            path.append(n)
            self.getPaths2(path)
            path.pop()

    def getPaths3():
        pass

    def getPaths4():
        pass

    def getPaths5(self):   
        if self.path[-1] == self.target:
            if len(self.path) == self.n**2:
                self.count5+=1
            return

        neighbours = []

        cell = self.path[-1]
        for i in range(cell[0]-1,cell[0]+2):
            if i<0 or i>=self.n:
                continue
            for j in range(cell[1]-1, cell[1]+2):
                if j<0 or j>=self.n:
                    continue
                if abs(i-cell[0])+abs(j-cell[1])!=1:
                    continue
                if (i,j) not in self.visited:
                    neighbours.append((i,j))

        if len(neighbours)==2:
            c1,c2 = neighbours[0],neighbours[1]
            if abs(c1[0]-c2[0])==2 or abs(c1[1]-c1[1])==2:
                return

        for n in neighbours:
            self.path.append(n)
            self.visited.add(n)
            self.getPaths5()
            self.count4+=1
            self.path.pop()
            self.visited.remove(n)


test = gridPath(7)
start = time.time()
test.getPaths5()
end = time.time()
print(end-start)
print(test.count5*2)
print(test.count4)
"""
start = time.time()
test.getPaths2([(0,0),(0,1)])
end = time.time()
print(test.count2*2)
print(end-start)
"""