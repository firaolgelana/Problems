# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class UF:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [0] * n
    
    def find(self, u):
        if self.root[u] != u:
            self.root[u] = self.find(self.root[u])
        return self.root[u]
    
    def union(self, u, v):
        rootU, rootV = self.find(u), self.find(v)
        if rootU == rootV:
            return 
        if self.rank[rootU] > self.rank[rootV]:
            self.root[rootV] = rootU
        else:
            self.root[rootU] = rootV
            if self.rank[rootU] == self.rank[rootV]:
                self.rank[rootU] += 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = UF(n)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    dsu.union(i, j)
        
        return len(set(dsu.find(i) for i in range(n)))
            





        