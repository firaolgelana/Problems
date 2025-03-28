# Problem: Skibidus and Fanum Tax (hard version) - http://codeforces.com/problemset/problem/2065/C2

from collections import defaultdict, deque, Counter
import sys, math
 
input = sys.stdin.readline
 
def iin():return int(input())
 
def sin():return input().strip()
 
def lin():return list(map(int, input().split()))
  
def minp(): return map(int, input().split())
 
def main():
    n, m = minp()
    a = lin()
    b = lin()
    b.sort()
    prev = float('-inf')
    for i in range(n):
        left, right = 0, m - 1
        while left <= right:
            mid = left + (right - left) // 2
            if b[mid] - a[i] < prev:
                left = mid + 1
            else:
                right = mid - 1
        if a[i] >= prev:
            if left < m:
                a[i] = min(a[i], b[left] - a[i])
        elif left == m:
            print("NO")
            return
        else:
            a[i] = b[left] - a[i]
        prev = a[i]

    print("YES")
 
if __name__ == "__main__":
    t = iin()
    for i in range(t):
        main()