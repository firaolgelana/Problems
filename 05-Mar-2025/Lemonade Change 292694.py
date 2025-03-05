# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for bill in bills:
            five += bill == 5
            ten += bill == 10
            if bill == 10:
                if five <= 0:
                    return False
                five -= 1
            if bill == 20:
                if ten >= 1 and five >= 1:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        
        return True
                
        