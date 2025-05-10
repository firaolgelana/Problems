# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

from collections import defaultdict, deque, Counter
from math import ceil, floor, pow
from heapq import *
from bisect import *
import sys
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
input = lambda: sys.stdin.readline().strip()
def iin(): return int(input())
def sin(): return input().strip()
def lin(): return list(map(int, input().split()))
def solve():
    n, m = lin()
    graph = [lin() for _ in range(m)]
    graph.sort(key=lambda x : x[2])
    cost = 0
    dsu = DSU(n + 1)
    for i in range(m):
        if dsu.union(graph[i][0], graph[i][1]):
            cost += graph[i][2]
    print(cost)
    
def main():
    t = 1
    # t = iin()
    for _ in range(t):
        solve()
if __name__ == "__main__":
    main()