# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        stack = []
        for char in paths:
            if char == '.':
                continue
            if char == '..':
                if stack:
                    stack.pop()
                continue
            if char:
                stack.append(char)

        valid_path = '/' + '/'.join(stack)
        return valid_path        