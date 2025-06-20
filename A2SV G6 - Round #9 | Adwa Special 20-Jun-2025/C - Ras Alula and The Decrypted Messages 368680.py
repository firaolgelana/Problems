# Problem: C - Ras Alula and The Decrypted Messages - https://codeforces.com/gym/601269/problem/C

from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
from math import ceil, floor, pow
import sys
input = sys.stdin.readline
def iin():return int(input())
def sin():return input().strip()
def lin():return list(map(int, input().split()))  
def main():
    n, m = lin()
    s = sin()
    w = sin()
    val_w, val_s = 0, 0
    for si, wi in zip(s, w):
        val_s += ord(si)
        val_w += ord(wi)
    if val_w == val_s:
        print("YES")
        return
    for i in range(m, n):
        val_s -= ord(s[i - m])
        val_s += ord(s[i])
        if val_s == val_w:
            print("YES")
            return
    print("NO")

if __name__ == "__main__":
    t = iin()
    # t = 1
    for i in range(t):
        main()
