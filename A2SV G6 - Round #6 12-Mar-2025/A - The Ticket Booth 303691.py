# Problem: A - The Ticket Booth - https://codeforces.com/gym/594077/problem/A

from collections import defaultdict, deque, Counter
import sys, math
 
input = sys.stdin.readline
 
def iin():return int(input())
 
def sin():return input().strip()
 
def lin():return list(map(int, input().split()))
  
def minp(): return map(int, input().split())

def main():
    n, s = minp()
    print(math.ceil(s/n))

if __name__ == "__main__":
    t = 1
    for i in range(t):
        main()
