# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

from collections import defaultdict, deque, Counter
import sys,math
 
input = sys.stdin.readline
 
def iin():return int(input())
 
def sin():return input().strip()
 
def lin():return list(map(int, input().split()))
  
def min(): return map(int, input().split())
 
def main():
    n, m = min()
    rev = is_snake = True
    for i in range(n):
        snake, empty = "#" * m, "." * (m-1) + "#"
        if is_snake:
            print(snake)
            is_snake = False
        else:
            if rev:
                print(empty)
                rev = False
            else:
                print(empty[::-1])
                rev = True
            is_snake = True

if __name__ == "__main__":
    main()