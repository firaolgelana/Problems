# Problem: Continuous Subarrays - https://leetcode.com/problems/continuous-subarrays/

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans, left = 0, 0
        max_queue, min_queue = deque(), deque()
        for right, num in enumerate(nums):
            while max_queue and max_queue[-1] < num:
                max_queue.pop()
            max_queue.append(num)
            while min_queue and min_queue[-1] > num:
                min_queue.pop()
            min_queue.append(num)
            while max_queue[0] - min_queue[0] > 2:
                if max_queue[0] == nums[left]:
                    max_queue.popleft()
                elif min_queue[0] == nums[left]:
                    min_queue.popleft()
                left += 1
            ans += right - left + 1

        return ans
