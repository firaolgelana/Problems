# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        nums = []
        for num, start, end in trips:
            nums.append((start, num))
            nums.append((end, -num))
        
        nums.sort()
        occupied = 0
        for status, num in nums:
            occupied += num
            if occupied > capacity:
                return False
                
        return True
        