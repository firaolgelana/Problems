# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

from collections import defaultdict, deque, Counter
import sys, math
 
input = sys.stdin.readline
 
def iin():return int(input())
 
def sin():return input().strip()
 
def lin():return list(map(int, input().split()))
  
def minp(): return map(int, input().split())

def main():
    n = iin()
    tree = defaultdict(list)
    for _ in range(n - 1):
        vertex = iin()
        tree[vertex].append(_ + 2)
    def dfs(node):
        if not tree[node]:
            return 1
        leaf_count = 0
        for child in tree[node]:
            leaf_count += dfs(child)
        
        if leaf_count < 3:
            print("No")
            exit()
        return 0
    dfs(1)
    print("Yes")

if __name__ == "__main__":
    t = 1
    for i in range(t):
        main()
