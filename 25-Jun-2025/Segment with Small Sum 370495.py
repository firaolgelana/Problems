# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n, s = map(int, input().split())
arr = [int(n) for n in input().split()]
left, right = 0, 0
max_sum, current_sum = 0, 0
while right < n:
    current_sum += arr[right]
    if current_sum > s:
        current_sum -= arr[left]
        left += 1

    max_sum = max(max_sum, right - left + 1)
    right += 1

print(max_sum)