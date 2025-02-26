# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

from collections import defaultdict, deque, Counter
import sys

input = sys.stdin.readline

def iin():return int(input())

def sin():return input().strip()

def lin():return list(map(int, input().split()))

def stol():return list(input().strip)

def minp(): return map(int, input().split())

def main():
    n = iin()
    arr = lin()
    arr.sort()
    print(arr[(n-1)//2])
    
if __name__ == "__main__":
    # t = int(input())
    t = 1
    for _ in range(t):
        main()
