# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if root_x < root_y:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dsu = UnionFind()
        for a, b in zip(s1, s2):
            dsu.union(a, b)
        ans = []
        for char in baseStr:
           ans.append(dsu.find(char))
        
        return "".join(ans)
        

        