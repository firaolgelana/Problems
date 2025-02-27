# Problem: Ways to Make a Fair Array - https://leetcode.com/problems/ways-to-make-a-fair-array/description/

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        totalOdd, totalEven = 0, 0
        
        for i in range(len(nums)):
            if i % 2:
                totalOdd += nums[i]
            else:
                totalEven += nums[i]
        
        count = 0
        prefixOdd = prefixEven = 0
        
        for i in range(len(nums)):
            if i % 2 == 0:  
                totalEven -= nums[i] 
                if prefixOdd + totalEven == prefixEven + totalOdd:
                    count += 1
                prefixEven += nums[i]  
            else: 
                totalOdd -= nums[i]  
                if prefixOdd + totalEven == prefixEven + totalOdd:
                    count += 1
                prefixOdd += nums[i] 
                
        return count
