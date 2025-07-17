# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

n = int(input())
is_prime = [True] * (n + 1)
 
for p in range(2, int(n**0.5) + 1):
    if is_prime[p]:
        for j in range(p * p, n + 1, p):
            is_prime[j] = False
 
prime = [i for i in range(2, n + 1) if is_prime[i]]
ans = 0
for i in range(1, n + 1):
    count = 0
    for num in prime:
        if i % num == 0:
            count += 1
    if count == 2:
        ans += 1
print(ans)