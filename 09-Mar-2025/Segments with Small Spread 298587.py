# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

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
    max_deque, min_deque = deque(), deque()
    left = segments = 0
    for right in range(n):
        while max_deque and arr[max_deque[-1]] <= arr[right]:
            max_deque.pop()
        max_deque.append(right)
        while min_deque and arr[min_deque[-1]] >= arr[right]:
            min_deque.pop()
        min_deque.append(right)
        while arr[max_deque[0]] - arr[min_deque[0]] > k:
            left += 1
            if min_deque[0] < left:
                min_deque.popleft()
            if max_deque[0] < left:
                max_deque.popleft()
        segments += right - left + 1
    return segments


if __name__ == "__main__":
    result = main()
    print(result)
