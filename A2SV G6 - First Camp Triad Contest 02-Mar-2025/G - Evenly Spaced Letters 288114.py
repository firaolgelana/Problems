# Problem: G - Evenly Spaced Letters - https://codeforces.com/gym/589822/problem/G

from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
import sys, math
 
input = sys.stdin.readline
 
def iin():return int(input())
 
def sin():return input().strip()
 
def lin():return list(map(int, input().split()))
  
def minp(): return map(int, input().split())

def main():
    s = sin()
    count_s = Counter(s)
    ans = [(key* value) for key, value in count_s.items()]
    print("".join(ans))

if __name__ == "__main__":
    t = iin()
    for i in range(t):
        main()
