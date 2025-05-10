# Problem: People are leaving - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A

from collections import defaultdict, deque, Counter
from math import ceil, floor, pow
from heapq import *
from bisect import *
import sys, threading
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

input = lambda: sys.stdin.readline().strip()
def iin(): return int(input())
def sin(): return input().strip()
def lin(): return list(map(int, input().split()))
def solve():
    n, m = lin()
    dsu = DSU(n + 1)
    for _ in range(m):
        s = sin()
        command, val = s.split()
        val = int(val)
        if command == '?':
            print(dsu.find(val))
        else:
            if val == n:
                dsu.parent[val] = -1
            else:
                dsu.parent[val] = dsu.find(val + 1)

def main():
    t = 1
    # t = iin()
    for _ in range(t):
        solve()
if __name__ == "__main__":    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
