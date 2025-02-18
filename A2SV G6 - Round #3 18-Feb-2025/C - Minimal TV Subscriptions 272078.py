# Problem: C - Minimal TV Subscriptions - https://codeforces.com/gym/588468/problem/C

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
    n, k, d = invr()
    arr = inlt()
    count = defaultdict(int)
    left, min_len = 0, n + 1
    for right in range(n):
        count[arr[right]] += 1
        while right - left + 1 >= d:
            min_len = min(min_len, len(count))
            count[arr[left]] -= 1
            if count[arr[left]] == 0:
                del count[arr[left]]
            left += 1
            
    return min_len

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        result = main()
        print(result)
