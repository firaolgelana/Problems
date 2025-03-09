# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for char in s:
            if char == ')':
                if stack[-1] != '(':
                    num = 0
                    while stack[-1] != '(':
                        num += stack.pop()
                    stack.pop()
                    stack.append(num * 2)
                else:
                    stack.pop()
                    stack.append(1)
            else:
                stack.append(char)

        return sum(stack)
