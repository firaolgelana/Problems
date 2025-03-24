# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(current):
            if len(current) == 2 * n:
                stack = []
                for p in current:
                    if stack and stack[-1] == "(" and p == ")":
                        stack.pop()
                    else:
                        stack.append(p)
                if not stack:
                    ans.append("".join(current))
                return
                
            for p in "()":
                current.append(p)
                backtrack(current)
                current.pop()
        
        backtrack([])
        return ans
        