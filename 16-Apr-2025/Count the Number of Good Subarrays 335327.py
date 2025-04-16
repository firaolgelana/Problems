# Problem: Count the Number of Good Subarrays - https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        left, pairs, ans = 0, 0, 0
        for right in range(len(nums)):
            count[nums[right]] += 1
            freq = count[nums[right]]
            pairs += (freq - 1)
            while pairs >= k:
                ans += len(nums) - right
                new_freq = count[nums[left]]
                count[nums[left]] -= 1
                pairs -= (new_freq - 1)
                left += 1
        
        return ans




        