# Problem: B - Kidus Couldn't Sleep - https://codeforces.com/gym/589822/problem/B

from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
import sys, math
 
input = sys.stdin.readline
 
def iin():return int(input())
 
def sin():return input().strip()
 
def lin():return list(map(int, input().split()))
  
def minp(): return map(int, input().split())

def main():
    n, k = minp()
    arr = lin()
    d = n - k + 1
    _sum = sum(arr[:d])
    total = _sum
    for i in range(n - d):
        _sum -= arr[i]
        _sum += arr[i+d]
        total += _sum
    
    print(total / d)

if __name__ == "__main__":
    t = 1
    for i in range(t):
        main()
