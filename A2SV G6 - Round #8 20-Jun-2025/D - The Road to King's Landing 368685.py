# Problem: D - The Road to King's Landing - https://codeforces.com/gym/599383/problem/D

from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
from math import ceil, floor, pow
import sys
 
input = sys.stdin.readline
 
def iin():return int(input())
 
def sin():return input().strip()
 
def lin():return list(map(int, input().split()))
  
def minp(): return map(int, input().split())

def lin_2d(row): return [lin() for _ in range(row)]

def main():
    n = iin()
    right = 0
    queries =[]
    for _ in range(n):
        l, r = minp()
        right = max(right, r + 1)
        queries.append((l, r))
    def is_possible(x):
        min_num = 0
        max_num = 0
        for l, r in queries:
            min_num = max(l, min_num - x)
            max_num = min(r, max_num + x)
            if max_num < min_num:
                return False
        return True
    
    left = 0
    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            right = mid - 1
        else:
            left = mid + 1

    print(left)
if __name__ == "__main__":
    t = iin()
    # t = 1
    for i in range(t):
        main()
