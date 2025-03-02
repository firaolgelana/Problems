# Problem: I - The Odd Challenge - https://codeforces.com/gym/589822/problem/I

from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
import sys, math
 
input = sys.stdin.readline
 
def iin():return int(input())
 
def sin():return input().strip()
 
def lin():return list(map(int, input().split()))
  
def minp(): return map(int, input().split())

def main():
    n, m = minp()
    arr = lin()
    prefix = [0]
    for num in arr:
        prefix.append(prefix[-1] + num)
    for _ in range(m):
        l, r, k = minp()
        _sum = prefix[-1] - (prefix[r] - prefix[l-1] + k * (r - l + 1))
        print("YES" if _sum % 2 else "NO")

if __name__ == "__main__":
    t = iin()
    for i in range(t):
        main()
