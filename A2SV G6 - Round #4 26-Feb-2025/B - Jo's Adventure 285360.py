# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

from collections import defaultdict, deque, Counter
import sys

input = sys.stdin.readline

def iin():return int(input())

def sin():return input().strip()

def lin():return list(map(int, input().split()))

def stol():return list(input().strip)

def minp(): return map(int, input().split())

def main():
    n, m = minp()
    arr = lin()
    pf = [0]
    queries = []
    for i in range(m):
        l, r = minp()
        queries.append((l, r))
    for i in range(n - 1):
        if arr[i] > arr[i+1]:
            pf.append(pf[-1] + arr[i] - arr[i + 1])
        else:
            pf.append(pf[-1])
    posf = [0]
    for i in range(n - 1):
        if arr[i] < arr[i+1]:
            posf.append(posf[-1] + arr[i+1] - arr[i ])
        else:
            posf.append(posf[-1])
    for l, r in queries:
        if l <= r:
            print(pf[r -  1] - pf[l-1])
        else:
            print(posf[l - 1] - posf[r - 1])

if __name__ == "__main__":
    # t = int(input())
    t = 1
    
    for _ in range(t):
        main()
