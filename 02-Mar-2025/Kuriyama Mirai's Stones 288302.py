# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

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
    costs = lin()
    pref = [0]
    for cost in costs:
        pref.append(pref[-1] + cost)
    costs.sort()
    cheapest = [0]
    for cost in costs:
        cheapest.append(cheapest[-1] + cost)
    
    m = iin()
    for _ in range(m):
        t, l, r = minp()
        print(pref[r] - pref[l-1] if t == 1 else cheapest[r] - cheapest[l-1])

if __name__ == "__main__":
    t = 1
    for i in range(t):
        main()
