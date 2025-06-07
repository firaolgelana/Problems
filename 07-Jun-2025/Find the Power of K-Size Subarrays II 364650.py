# Problem: Find the Power of K-Size Subarrays II - https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans = []
        stack = deque([nums[k - 1]])
        for i in range(k - 2, -1, -1):
            if nums[i + 1] == nums[i] + 1:
                stack.appendleft(nums[i])
            else:
                break

        if len(stack) == k:
            ans.append(stack[-1])
        else:
            ans.append(-1)
        for i in range(len(nums) - k):
            if len(stack) == k:
                stack.popleft()
            if not stack or stack[-1] + 1 == nums[i + k]:
                stack.append(nums[i + k])
            else:
                stack.clear()
                stack.append(nums[i + k])
            if len(stack) == k:
                ans.append(stack[-1])
            else:
                ans.append(-1)

        return ans



