# Problem: B - Anansi and Trip-Photographs - https://codeforces.com/gym/588468/problem/B

from collections import defaultdict, deque, Counter
import sys

input = sys.stdin.readline

def inp():
    return int(input())

def inlt():
    return list(map(int, input().split()))

def insr():
    s = input().strip()
    return list(s)

def invr():
    return map(int, input().split())

def main():
    n, k = invr()
    arr = inlt()
    arr.sort()
    left, right = arr[:n],  arr[n:]
    for i in reversed(range(n)):
        if right[i] - left[i] < k:
            return "NO"
    return "YES"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        result = main()
        print(result)
