# Problem: F - Covered Points Count - https://codeforces.com/gym/589822/problem/F

from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
import sys, math
 
input = sys.stdin.readline
 
def iin():return int(input())
 
def sin():return input().strip()
 
def lin():return list(map(int, input().split()))
  
def minp(): return map(int, input().split())

def main():
    n = iin()
    segments = defaultdict(int)
    for _ in range(n):
        start, end = minp()
        segments[start] += 1
        segments[end + 1] -= 1

    keys = sorted(segments.keys())
    coverage = [0] * (n + 1)
    pt = 0
    for i in range(len(keys) - 1):
        pt += segments[keys[i]]
        coverage[pt] += keys[i+1] - keys[i]
    
    print(*coverage[1:])


if __name__ == "__main__":
    t = 1
    for i in range(t):
        main()
