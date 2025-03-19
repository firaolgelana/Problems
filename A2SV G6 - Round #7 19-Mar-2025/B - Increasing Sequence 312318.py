# Problem: B - Increasing Sequence - https://codeforces.com/gym/596141/problem/B

from collections import defaultdict, deque, Counter
import sys, math
 
input = sys.stdin.readline
 
def iin():return int(input())
 
def sin():return input().strip()
 
def lin():return list(map(int, input().split()))
  
def minp(): return map(int, input().split())

def main():
    n = iin()
    arr = lin()
    b = 0
    for i in range(n):
        b += 1
        while arr[i] == b:
            b += 1
            
    print(b)
        

if __name__ == "__main__":
    t = iin()
    for i in range(t):
        main()
