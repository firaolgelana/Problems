# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

from collections import defaultdict, deque, Counter
import sys, math

input = sys.stdin.readline

def iin(): return int(input())

def sin(): return input().strip()

def lin(): return list(map(int, input().split()))

def minp(): return map(int, input().split())

def main():
    n = iin()
    arr = lin()
    i = count = 0
    while i < n - 1:
        if arr[i] > arr[i+1]:
            i += 1
            count += 1
        i += 1
    print(count)

if __name__ == "__main__":
    t = iin()
    for _ in range(t):
        main()