# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

from collections import defaultdict, deque, Counter
import sys

input = sys.stdin.readline

def inp():return int(input())

def inlt():return list(map(int, input().split()))

def insr():return list(input().strip())

def invr():return map(int, input().split())

def main():
    n, k, q = invr()
    arr = [0] * (200000 + 2)
    for _ in range(n):
        left, right = invr()
        arr[left] += 1
        arr[right + 1] -= 1
    prefixSum = [0] * (200000 + 1)
    for i in range(200000):
        arr[i+1] += arr[i]
        if arr[i+1] >= k:
            prefixSum[i+1] = 1
    for i in range(200000):
        prefixSum[i+1] += prefixSum[i]
    for _ in range(q):
        a, b = invr()
        count = prefixSum[b] - prefixSum[a - 1]
        print(count)

if __name__ == "__main__":
    main()