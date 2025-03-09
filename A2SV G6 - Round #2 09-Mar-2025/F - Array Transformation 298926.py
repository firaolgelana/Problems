# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import Counter
t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(n) for n in input().split()]
    count = Counter(arr)
    freq = sorted(count.values(), reverse=True)
    num = freq[0]
    for i in range(1, len(freq)):
        left = freq[i] * (i + 1)
        num = max(left, num)
    print(n - num)

