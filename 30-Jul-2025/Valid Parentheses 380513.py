# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = Counter({'(':')', '[':']', '{':'}'})
        stack = []
        for bracket in s:
            if stack and brackets[stack[-1]] == bracket:
                stack.pop()
                continue
            stack.append(bracket)

        return not stack 
        