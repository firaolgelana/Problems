# Problem: C - Penalty Shootout - https://codeforces.com/gym/596141/problem/C

from collections import defaultdict, deque, Counter
import sys, math
 
input = sys.stdin.readline
 
def iin():return int(input())
 
def sin():return input().strip()
 
def lin():return list(map(int, input().split()))
  
def minp(): return map(int, input().split())

def main():
    s = sin()
    lst = list(s)
    def dfs(idx, lst, s1, s2):
        even = odd = 0
        if idx % 2 == 0:
            even = (10 - idx)//2
            odd = (10 - idx)//2
        else:
            even = (10 - idx)//2
            odd = (10 - idx)//2 + 1
        if s1 >= s2 and s1 > s2 + odd:
            return idx
        if s2 >= s1 and s2 > s1 + even:
            return idx
        if idx >= 10:
            return 10
        if lst[idx].isdigit():
            if idx % 2 == 0:
                s1 += int(lst[idx])  
            else:
                s2 += int(lst[idx])
            return dfs(idx + 1, lst, s1, s2)
        else:
            one = lst[:]
            zeros = lst[:]
            one[idx] = '1'
            zeros[idx] = '0'
            # print(one)
            left = dfs(idx,  one, s1, s2)
            right = dfs(idx,  zeros, s1, s2)
            return  min(left, right)
        
    print(dfs(0, lst, 0, 0)) 

if __name__ == "__main__":
    t = iin()
    for i in range(t):
        main()
