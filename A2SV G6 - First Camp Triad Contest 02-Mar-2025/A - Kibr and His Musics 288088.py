# Problem: A - Kibr and His Musics - https://codeforces.com/gym/589822/problem/A

from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
import sys, math
 
input = sys.stdin.readline
 
def iin():return int(input())
 
def sin():return input().strip()
 
def lin():return list(map(int, input().split()))
  
def minp(): return map(int, input().split())

def main():
    n, m = minp()
    prefix = [0]
    for _ in range(n):
        c, t = minp()
        prefix.append(prefix[-1] + c * t)
    moment = lin()
    left = 0
    for i in range(m):
        while prefix[left] < moment[i]:
            left += 1
        print(left)

if __name__ == "__main__":
    t = 1
    for i in range(t):
        main()
