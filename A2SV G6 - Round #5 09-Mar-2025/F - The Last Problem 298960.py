# Problem: F - The Last Problem - https://codeforces.com/gym/591928/problem/F

import sys

input = sys.stdin.readline

def iin(): return int(input())
def lin(): return list(map(int, input().split()))

def main():
    n = iin()
    a = lin()
    b = lin()

    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + a[i - 1] * b[i - 1]

    max_sum = prefix[n] 

    for i in range(n):
        l, r = i - 1, i + 1
        mult = a[i] * b[i]
        while l >= 0 and r < n:
            mult += a[l] * b[r] + a[r] * b[l]
            max_sum = max(max_sum, prefix[l] + mult + (prefix[n] - prefix[r+1]))
            l -= 1
            r += 1

    for i in range(n - 1):
        l, r = i, i + 1
        mult = 0
        while l >= 0 and r < n:
            mult += a[l] * b[r] + a[r] * b[l]
            max_sum = max(max_sum, prefix[l] + mult + (prefix[n] - prefix[r+1]))
            l -= 1
            r += 1

    print(max_sum)

if __name__ == "__main__":
    t = 1
    for _ in range(t):
        main()
