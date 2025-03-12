# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

from collections import defaultdict, deque, Counter
import sys, math
 
input = sys.stdin.readline
 
def iin():return int(input())
 
def sin():return input().strip()
 
def lin():return list(map(int, input().split()))
  
def minp(): return map(int, input().split())

def main():
    n = iin()
    s = sin()
    ones, zeros = [], []
    result = []
    subsequences = 1
    for char in s:
        if char == '1':
            if zeros:
                top = zeros.pop()
                ones.append(top)
                result.append(top)
            else:
                ones.append(subsequences)
                result.append(subsequences)
                subsequences += 1
        else:
            if ones:
                top = ones.pop()
                zeros.append(top)
                result.append(top)
            else:
                zeros.append(subsequences)
                result.append(subsequences)
                subsequences += 1
    print(max(result))
    print(*result)

if __name__ == "__main__":
    t = iin()
    for i in range(t):
        main()
