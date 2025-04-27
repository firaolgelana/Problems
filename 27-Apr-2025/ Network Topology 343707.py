# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
from math import ceil, floor, pow
import sys
input = sys.stdin.readline
def iin():return int(input())
def sin():return input().strip()
def lin():return list(map(int, input().split()))  
def main():
    n, m = lin()
    graph = [[] for _ in range(n)]
    degree = [0] * n
    for _ in range(m):
        u, v = lin()
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
        degree[u - 1] += 1
        degree[v - 1] += 1
    center_node = [i for i in degree if i == n - 1]
    leaf_nodes = [i for i in degree if i == 1]
    if len(center_node) == 1 and len(leaf_nodes) == n - 1:
        print("star topology")
        return
    if all(d == 2 for d in degree):
        print('ring topology')
        return
    if degree.count(1) == 2 and degree.count(2) == n - 2:
        print('bus topology')
        return
    print('unknown topology')

if __name__ == "__main__":
    # t = iin()
    t = 1
    for i in range(t):
        main()
