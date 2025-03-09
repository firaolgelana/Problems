# Problem: A - Make the Product Zero - https://codeforces.com/gym/586960/problem/A

n = int(input())
arr = [abs(int(n)) for n in input().split()]
min_num = min(arr)
print(min_num)