# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

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
            return False
        self.parent[root_y] = root_x
        return True

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        dsu = UnionFind()
        for eq in equations:
            if eq[1] == '=':
                dsu.union(eq[0], eq[-1])
        for eq in equations:
            if eq[1] == '!' and dsu.find(eq[0]) == dsu.find(eq[-1]):
                return False

        return True

        