# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        _sum , stack = 0, []
        modulo = 10 ** 9 + 7
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                left = stack[-2] if len(stack) >= 2 else -1
                num_subarrays = (stack[-1] - left) * (i - stack[-1])
                b = arr[stack.pop()]
                _sum += num_subarrays * b 
            stack.append(i)
        left = 0
        for idx in stack:
            _sum += ((idx - left + 1) * (len(arr) - idx)) * arr[idx]
            left = idx + 1
        return _sum % modulo
        