# Problem: F - Nahom's Array Dilemma - https://codeforces.com/gym/594077/problem/F

from collections import defaultdict, deque, Counter
from itertools import accumulate
import sys, math
 
input = sys.stdin.readline
 
def iin():return int(input())
 
def sin():return input().strip()
 
def lin():return list(map(int, input().split()))
  
def minp(): return map(int, input().split())

def main():
    n = iin()
    arr = lin()
    def is_valid(arr):
        prefix = list(accumulate(arr, initial=0))
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                top = stack.pop()
                if prefix[i] - prefix[top] > 0:
                    return True
            stack.append(i)
        return False
    if is_valid(arr) or is_valid(arr[::-1]):
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    t = iin()
    for i in range(t):
        main()
