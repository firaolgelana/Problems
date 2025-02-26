# Problem: Contiguous Array - https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count, max_len = 0, 0
        prefix = defaultdict(int)
        prefix[0] = -1
        for i in range(len(nums)):
            count += 1 if nums[i] else -1
            if count in prefix:
                max_len = max(max_len, i - prefix[count])
            else:
                prefix[count] = i

        return max_len