# Problem: Cellular Network - https://codeforces.com/contest/702/problem/C

n, m = map(int, input().split())
cities = list(map(int, input().split()))
towers = list(map(int, input().split()))

max_distance = float('-inf')
for i in range(n):
    left, right = 0, m - 1
    while left <= right:
        mid = left + (right - left) // 2
        if towers[mid] < cities[i]:
            left = mid + 1
        else:
            right = mid - 1

    left = m - 1 if left >= m else left
    right = 0 if right < 0 else right

    left_distance = abs(cities[i] - towers[left])
    right_distance = abs(cities[i] - towers[right])
    distance = left_distance if left_distance < right_distance else right_distance
    max_distance = max(max_distance, distance)

print(max_distance)
