# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        current_sum = ans = 0
        for num in nums:
            current_sum += num
            ans += count[current_sum - goal]
            count[current_sum] += 1

        return ans
        