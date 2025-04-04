# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtrack(idx, current):
            if idx == len(num):
                return len(current) >= 3               
            for i in range(idx, len(num)):
                val = num[idx:i + 1]
                if len(val) >= 2 and val[0] == '0':
                    return False
                if len(current) >= 2 and current[-2] + current[-1] != (int(val)):
                    continue
                current.append(int(val))
                if backtrack(i + 1, current):
                    return True              
                current.pop()
            return False

        return backtrack(0, [])
    
        

        