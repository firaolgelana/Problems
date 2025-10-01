# Problem: Water Bottles - https://leetcode.com/problems/water-bottles/description

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        num = total = numBottles 
        while num >= numExchange:
            total += num // numExchange
            num = (num // numExchange + num % numExchange)

        return total

        