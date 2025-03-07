# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def removed(string):
            stack = []
            for char in string:
                if char == '#':
                    if stack:
                        stack.pop() 
                else:
                    stack.append(char)
            return stack

        return removed(s) == removed(t)