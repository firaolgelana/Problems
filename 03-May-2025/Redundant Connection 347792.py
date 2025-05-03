# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class UF:
    def __init__(self, n):
        self.root = list(range(n + 1))
        self.rank = [0] * (n + 1)
    
    def find(self, u):
        if self.root[u] != u:
            self.root[u] = self.find(self.root[u])
        return self.root[u]
    
    def union(self, u, v):
        rootU, rootV = self.find(u), self.find(v)
        if rootU == rootV:
            return False
        if self.rank[rootU] > self.rank[rootV]:
            self.root[rootV] = rootU
        else:
            self.root[rootU] = rootV
            if self.rank[rootU] == self.rank[rootV]:
                self.rank[rootU] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges):
        dsu = UF(len(edges))
        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]
        
        return []
