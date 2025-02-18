# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

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
    n = inp()
    s = input()
    min_remove = float('inf')
    for i in range(26):
        left, right = 0, n - 1
        count = 0
        while left < right:
            if s[left] != s[right]:
                if s[left] == chr(i+97):
                    left += 1
                    count += 1
                elif s[right] == chr(i+97):
                    right -= 1
                    count += 1
                else:
                    count = -1
                    break
            else:
                left += 1
                right -= 1
        if count != -1:
            min_remove = min(min_remove, count)
    return min_remove if min_remove != float('inf') else -1
            

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        result = main()
        print(result)
