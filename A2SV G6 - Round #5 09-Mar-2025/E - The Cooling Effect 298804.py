# Problem: E - The Cooling Effect - https://codeforces.com/gym/591928/problem/E

from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
import sys, math, heapq
 
input = sys.stdin.readline
 
def iin():return int(input())
 
def sin():return input().strip()
 
def lin():return list(map(int, input().split()))
  
def minp(): return map(int, input().split())

def main():
    input()
    n, k = minp()
    a = lin()
    t = lin()
    prefix , suffix = [float('inf')] * n, [float('inf')] * n
    j = 0
    for i in a:
        prefix[i-1] = t[j]
        suffix[i-1] = t[j]
        j += 1
    
    for i in range(1, n):
        prefix[i] = min(prefix[i-1] + 1, prefix[i])
    for i in range(n - 2, -1, -1):
        suffix[i] = min(suffix[i+1] + 1, suffix[i])

    ans = [0] * n
    for i in range(n):
        ans[i] = min(prefix[i], suffix[i])

    print(*ans)

if __name__ == "__main__":
    t = iin()
    for i in range(t):
        main()
