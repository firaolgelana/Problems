# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points_with_cost = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                d = abs(x2 - x1) + abs(y2 - y1)
                points_with_cost.append((d, i, j))

        points_with_cost.sort()
        dsu = DSU(len(points))
        costs = 0
        for cost, u, v in points_with_cost:
            if dsu.union(u, v):
                costs += cost
            
        return costs



        