# Problem: D - Socialism - https://codeforces.com/gym/589822/problem/D

from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
import sys, math
 
input = sys.stdin.readline
 
def iin():return int(input())
 
def sin():return input().strip()
 
def lin():return list(map(int, input().split()))
  
def minp(): return map(int, input().split())

def main():
    n, x = minp()
    arr = lin()
    arr.sort(reverse=True)
    _sum = 0
    for i in range(n):
        _sum += arr[i]
        if _sum / (i + 1) < x:
            print(i)
            return
    print(n)

if __name__ == "__main__":
    t = iin()
    for i in range(t):
        main()
