# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

from collections import defaultdict, deque, Counter
from itertools import accumulate
import sys, math
 
input = sys.stdin.readline
 
def iin():return int(input())
 
def sin():return input().strip()
 
def lin():return list(map(int, input().split()))
  
def minp(): return map(int, input().split())

def main():
    n = iin()
    r = lin()
    m = iin()
    b = lin()
    prefix_r = list(accumulate(r, initial=0))
    prefix_b = list(accumulate(b, initial=0))
    print(max(prefix_b) + max(prefix_r))
        
if __name__ == "__main__":
    t = iin()
    for i in range(t):
        main()
