# Problem: A - Free Ice Cream for the Kids - https://codeforces.com/gym/596141/problem/A

from collections import defaultdict, deque, Counter
import sys, math
 
input = sys.stdin.readline
 
def iin():return int(input())
 
def sin():return input().strip()
 
def lin():return list(map(int, input().split()))
  
def minp(): return map(int, input().split())

def main():
    n, m = minp()
    _sum = m
    count = 0
    for _ in range(n):
        s = sin()
        char, d = s.split()
        d = int(d)
        if _sum < d and char == '-':
            count += 1
        _sum = _sum + d if char == '+' else (_sum - d if d <= _sum else _sum - 0)
        
    print(_sum, count)
        

if __name__ == "__main__":
    t = 1
    for i in range(t):
        main()
