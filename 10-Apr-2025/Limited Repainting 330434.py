# Problem: Limited Repainting - https://codeforces.com/contest/2070/problem/C

from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
from math import ceil, floor, pow
import sys
input = sys.stdin.readline
def iin():return int(input())
def sin():return input().strip()
def lin():return list(map(int, input().split()))  
def main():
    n, k = lin()
    colors = sin()
    penality = lin()
    def is_possible_to_paint(x):
        i, count= 0, 0
        while i < n:
            if colors[i] == 'B' and penality[i] > x:
                while i < n and (colors[i] == 'B' or penality[i] <= x):
                    i += 1
                count += 1
            i += 1
        return count <= k
        
    left, right = 0, max(penality)
    while left <= right:
        mid = left + (right - left) // 2
        if is_possible_to_paint(mid):
            right = mid - 1
        else:
            left = mid + 1
    print(left)
if __name__ == "__main__":
    t = iin()
    # t = 1
    for i in range(t):
        main()
