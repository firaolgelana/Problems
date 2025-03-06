# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            '*':lambda x, y : x * y,
            '+':lambda x, y : x + y, 
            '-':lambda x, y : x - y,
            '/':lambda x, y : math.trunc(x / y)
        }
        stack = []
        for char in tokens:
            if char.lstrip('-').isdigit():
                stack.append(int(char))
            else:
                y = stack.pop()
                x = stack.pop()
                cal = operations[char](x, y)
                stack.append(cal)
            
        return stack[0]

        