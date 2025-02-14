# Problem: Books - https://codeforces.com/contest/279/problem/B

n, t = map(int, input().split())
books = list(map(int, input().split()))

max_books = current_books = left = 0
for right in range(n):
    current_books += books[right]
    while current_books > t and left <= right:
        current_books -= books[left]
        left += 1
    max_books = max(max_books, right - left + 1)

print(max_books)