# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefixSum = [0]
        for n in nums:
            if n%2:
                prefixSum.append(prefixSum[-1]+1)
            else:
                prefixSum.append(prefixSum[-1])
        prefixCounter = {0:1}
        result = 0
        del prefixSum[0]
        for i in prefixSum:
            diff = i - k
            result += prefixCounter.get(diff,0)
            prefixCounter[i] = 1+prefixCounter.get(i,0)
        return result
        