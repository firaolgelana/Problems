# Problem: Clear Digits - https://leetcode.com/problems/clear-digits/description/

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and char.isdigit():
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
        