# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C

from collections import defaultdict, deque, Counter
import sys,math
 
input = sys.stdin.readline
 
def iin():return int(input())
 
def sin():return input().strip()
 
def lin():return list(map(int, input().split()))
  
def min(): return map(int, input().split())

def main():
  n = iin()
  a = sin()
  b = sin()
  rev = False
  ones = a.count('1')
  zeros = n - ones
  for i in reversed(range(n)):
    if not rev and  a[i] != b[i]:
       if ones != zeros:
          return "NO"
       rev = True
    if rev  and a[i] != b[i]:
        pass
    if rev and a[i] == b[i]:
       if ones != zeros:
          return "NO"
       rev = False
    ones -= a[i] == '1'
    zeros -= a[i] == '0'
  return "YES"


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        result = main()
        print(result)