# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = defaultdict(int)
left, right = 0, 0
i = 0
for j in range(n):
    count[arr[j]] += 1
    while len(count) > k:
        count[arr[i]] -= 1
        if count[arr[i]] == 0:
            del count[arr[i]]
        i += 1

    if j - i > right - left:
        left, right = i, j

print(left + 1, right + 1)
