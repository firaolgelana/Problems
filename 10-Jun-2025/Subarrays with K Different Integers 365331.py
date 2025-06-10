# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atleast_k(k):
            maps = defaultdict(int)
            left = ans = 0
            for right in range(len(nums)):
                maps[nums[right]] += 1
                while len(maps) >= k:
                    ans += len(nums) - right
                    maps[nums[left]] -= 1
                    if maps[nums[left]] == 0:
                        del maps[nums[left]]
                    left += 1
            return ans
                
        return atleast_k(k) - atleast_k(k + 1)