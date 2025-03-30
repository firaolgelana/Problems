# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        ans = 0
        for pos in houses:
            ans = max(ans, self.find_radius(pos, heaters))
        return ans
 
    def find_radius(self, num, heaters):
        left, right = 0, len(heaters)-1
        min_radius = float('inf')
        while left <= right:
            mid = left + (right - left)//2
            min_radius = min(min_radius, abs(num - heaters[mid]))
            if heaters[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        return min_radius
        