# Problem: Unforgivable Curse (hard version) - https://codeforces.com/contest/1800/problem/E2

from collections import defaultdict, deque, Counter
from math import ceil, floor, pow
from heapq import *
from bisect import *
import sys
input = lambda: sys.stdin.readline().strip()
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
    
def iin(): return int(input())
def sin(): return input().strip()
def lin(): return list(map(int, input().split()))
def solve():
    n, m = lin()
    s = sin()
    t = sin()
    dsu = DSU(n)
    for i in range(n - m):
        x = i + m
        y = i + m + 1
        dsu.union(i, x)
        if y < n:
            dsu.union(i, y)
    group = defaultdict(list)
    for i in range(n):
        root = dsu.find(i)
        group[root].append(i)
    for val in group.values():
        s_g = [s[i] for i in val]
        t_g = [t[i] for i in val]
        if Counter(s_g) != Counter(t_g):
            print("NO")
            return
            
    print("YES")

def main():
    t = 1
    t = iin()
    for _ in range(t):
        solve()
if __name__ == "__main__":
    main()