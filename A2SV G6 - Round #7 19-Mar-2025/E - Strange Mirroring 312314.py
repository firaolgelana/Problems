# Problem: E - Strange Mirroring - https://codeforces.com/gym/596141/problem/E

from collections import defaultdict, deque, Counter
from math import floor, ceil, log2
import sys
 
input = sys.stdin.readline
 
def iin():return int(input())
 
def sin():return input().strip()
 
def lin():return list(map(int, input().split()))
  
def minp(): return map(int, input().split())
 
def main():
    s = sin()
    n = iin()
    queries = lin()
    size = len(s)
    def find(k):
        if k <= size:
            return s[k - 1]
        operations = ceil(log2(k/size))
        k -= ((2 ** (operations - 1)) * size)
        return find(k).swapcase()
 
    for query in queries:
        print(find(query), end=" ")
    print()
 
if __name__ == "__main__":
    t = iin()
    for i in range(t):
        main()