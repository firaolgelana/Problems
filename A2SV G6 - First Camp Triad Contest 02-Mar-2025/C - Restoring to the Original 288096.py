# Problem: C - Restoring to the Original - https://codeforces.com/gym/589822/problem/C

from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
import sys, math
 
input = sys.stdin.readline
 
def iin():return int(input())
 
def sin():return input().strip()
 
def lin():return list(map(int, input().split()))
  
def minp(): return map(int, input().split())

def main():
    n = iin()
    s = sin()
    ones = s.count('n')
    zeros = s.count('r')
    print('1 ' * ones , end="")
    print('0 ' *zeros)

if __name__ == "__main__":
    t = 1
    for i in range(t):
        main()
