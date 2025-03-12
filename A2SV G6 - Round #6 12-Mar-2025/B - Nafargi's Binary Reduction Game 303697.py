# Problem: B - Nafargi's Binary Reduction Game - https://codeforces.com/gym/594077/problem/B

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
    stack = []
    for char in s:
        if stack and stack[-1] != char:
            stack.pop()
        else:
            stack.append(char)
    print(len(stack))

if __name__ == "__main__":
    t = 1
    for i in range(t):
        main()
