# Problem: Running Miles - https://codeforces.com/problemset/problem/1826/D

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
    prefix, suffix = [0] * n , [0] * n
    for i in range(n):
        prefix[i] = arr[i] + i
        suffix[i] = arr[i] - i
    for i in range(1, n):
        prefix[i] = max(prefix[i], prefix[i-1])
    for i in range(n - 2, -1, -1):
        suffix[i] = max(suffix[i], suffix[i+1])
    max_beauty = 0
    for i in range(1, n - 1):
        max_beauty = max(max_beauty, arr[i] + prefix[i-1] + suffix[i+1])
    
    print(max_beauty)

if __name__ == "__main__":
    t = iin()
    for i in range(t):
        main()
