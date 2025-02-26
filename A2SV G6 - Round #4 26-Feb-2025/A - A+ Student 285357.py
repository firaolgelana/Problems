# Problem: A - A+ Student - https://codeforces.com/gym/590053/problem/A

from collections import defaultdict, deque, Counter
import sys

input = sys.stdin.readline

def iin():return int(input())

def sin():return input().strip()

def lin():return list(map(int, input().split()))

def stol():return list(input().strip)

def minp(): return map(int, input().split())

def main():
    a, b, c = minp()
    max_s = max(a, b, c)
    if a == b == c:
        print(1, 1, 1)
    elif a == b == max_s:
        print(1, 1, max_s - c + 1)
    elif a == c == max_s:
        print(1, max_s - b + 1, 1)
    elif b == c == max_s:
        print(max_s - a + 1, 1, 1)
    elif a == max_s:
        print(0, max_s - b + 1, max_s - c + 1)
    elif b == max_s:
        print(max_s - a + 1, 0, max_s - c + 1)
    else:
        print(max_s - a + 1, max_s - b + 1, 0)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        main()
