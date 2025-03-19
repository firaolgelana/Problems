# Problem: D - Creating an a-Good String - https://codeforces.com/gym/596141/problem/D

from collections import defaultdict, deque, Counter
import sys, math
 
input = sys.stdin.readline
 
def iin():return int(input())
 
def sin():return input().strip()
 
def lin():return list(map(int, input().split()))
  
def minp(): return map(int, input().split())

def main():
    n = iin()
    s = sin()
    c = "a"
    move = 0
    def count(mid, c):
        cnt = Counter(mid)
        return len(mid) - cnt[c]
    def dfs(s, c):
        if len(s) <= 1:
            return 0 if s == c else 1
        
        mid = len(s) // 2
        cnt1 = count(s[:mid], c)
        cnt2 = count(s[mid:], c)
        left = dfs(s[:mid], chr((ord(c) - 97 + 1) % 26 + 97))
        right = dfs(s[mid:], chr((ord(c) - 97 + 1) % 26 + 97))
        return min(left + cnt2, right + cnt1)

    print(dfs(s, c))


if __name__ == "__main__":
    t = iin()
    for i in range(t):
        main()
