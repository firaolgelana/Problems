# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and char == '*':
                stack.pop()
                continue
            stack.append(char)
        
        return "".join(stack)
        