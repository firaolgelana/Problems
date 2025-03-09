# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from collections import Counter, defaultdict
t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    left, right = defaultdict(int), Counter(s)
    count = 0
    for i in range(n):
        left[s[i]] += 1
        right[s[i]] -= 1
        if right[s[i]] == 0:
            del right[s[i]]
        count = max(count, len(left) + len(right))
    print(count)