# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

from collections import defaultdict, deque, Counter
import sys

input = sys.stdin.readline

def inp():
    return int(input())

def inlt():
    return list(map(int, input().split()))

def insr():
    s = input().strip()
    return list(s)

def invr():
    return map(int, input().split())

def main():
    n = inp()
    arr1 = inlt()
    m = inp()
    arr2 = inlt()
 
    if sum(arr1) != sum(arr2):
        return -1
    
    left1 = left2 = 1
    count = 0
    sum1, sum2 = arr1[0], arr2[0]
    arr1.append(0)
    arr2.append(0)
    while left1 <= n and left2 <= m:
        if sum1 == sum2:
            count += 1
            sum1 += arr1[left1]
            sum2 += arr2[left2]
            left1 += 1
            left2 += 1
        elif sum1 < sum2:
            sum1 += arr1[left1]
            left1 += 1
        else:
            sum2 += arr2[left2]
            left2 += 1

    return count
if __name__ == "__main__":
    result = main()
    print(result)