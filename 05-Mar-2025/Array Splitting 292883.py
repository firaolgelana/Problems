# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

from collections import defaultdict, deque, Counter
import sys, math
 
input = sys.stdin.readline
 
def iin():return int(input())
 
def sin():return input().strip()
 
def lin():return list(map(int, input().split()))
  
def minp(): return map(int, input().split())

def main():
    n, k = minp()
    arr = lin()
    diff = [arr[i] - arr[i-1] for i in range(1, n)]
    diff.sort(reverse=True)
    cost = sum(diff[k-1:])
    print(cost)

if __name__ == "__main__":
    t = 1
    for i in range(t):
        main()
