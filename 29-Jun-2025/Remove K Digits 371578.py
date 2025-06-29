# Problem: Remove K Digits - https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        while k > 0:
            stack.pop()
            k -= 1
        i = 0
        while i < len(stack):
            if stack[i] != '0':
                break
            i += 1

        return "".join(stack[i:]) if stack[i:] else '0'
