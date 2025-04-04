# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
from math import ceil, floor, pow
import sys
input = sys.stdin.readline
def iin():return int(input())
def sin():return input().strip()
def lin():return list(map(int, input().split()))  
def minp(): return map(int, input().split())
def merge(left_arr, right_arr):
    if left_arr[0] <= right_arr[0]:
        return left_arr + right_arr, 0
    return right_arr + left_arr, 1
def main():
    n = iin()
    arr = lin()
    number_swaps = 0
    def divide_sort(left, right):
        nonlocal number_swaps
        mid = (left + right) // 2
        if left == right:
            return [arr[left]]
        left_arr = divide_sort(left, mid)
        right_arr = divide_sort(mid + 1, right)
        nums, count = merge(left_arr, right_arr)
        number_swaps += count
        return nums
    
    nums = divide_sort(0, n - 1)  
    for i in range(1, n):
        if nums[i-1] > nums[i]:
            print(-1)
            return
    print(number_swaps)

if __name__ == "__main__":
    t = iin()
    # t = 1
    for i in range(t):
        main()
