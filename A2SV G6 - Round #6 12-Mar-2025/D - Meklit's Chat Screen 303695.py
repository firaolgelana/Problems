# Problem: D - Meklit's Chat Screen - https://codeforces.com/gym/594077/problem/D

from collections import defaultdict, deque, Counter
import sys, math
 
input = sys.stdin.readline
 
def iin():return int(input())
 
def sin():return input().strip()
 
def lin():return list(map(int, input().split()))
  
def minp(): return map(int, input().split())

def main():
    n, m = minp()
    chats = lin()
    seen = set()
    stack = deque()
    for num in chats:
        if num in seen:
            continue
        elif len(stack) < m:
            stack.appendleft(num)
            seen.add(num)
        else:
            seen.discard(stack.pop())
            seen.add(num)
            stack.appendleft(num)

    print(len(stack))
    print(*stack)


if __name__ == "__main__":
    t = 1
    for i in range(t):
        main()
