# Problem: A - Nth Digit in Sequence - https://codeforces.com/gym/588468/problem/A

n = int(input())
arr = [str(n) for n in range(1, 1000 + 1)]
s = "".join(arr)
print(s[n-1])