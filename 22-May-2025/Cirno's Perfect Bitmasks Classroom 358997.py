# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

for _ in range(int(input())):
    x = int(input())
    count = 0
    new_x = x
    while x > 0:
        if x & 1:
            break
        count += 1
        x >>= 1
    y = 2 ** count
    if new_x ^ y != 0:
        print(y)
    else:
        count = 0
        while new_x > 0:
            if new_x & 1 == 0:
                break
            count += 1
            new_x >>= 1
        print(y + 2 ** count)
        