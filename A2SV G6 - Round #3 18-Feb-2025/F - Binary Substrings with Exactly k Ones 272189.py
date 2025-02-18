# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

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
    k = inp()
    s = input().strip()
    count = Counter({0:1})
    current_sum, num_substrings = 0, 0
    for char in s:
        current_sum += int(char)
        num_substrings += count[current_sum - k]
        count[current_sum] += 1

    return num_substrings

if __name__ == "__main__":
    result = main()
    print(result)
