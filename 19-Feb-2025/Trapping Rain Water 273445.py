# Problem: Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        stack, trap = [], 0
        for i in range(len(height)):
            while len(stack) >= 2 and height[i] > height[stack[-1]]:
                heights = min(height[stack[-2]], height[i])
                width = i - stack[-2] - 1 
                trap += (heights - height[stack[-1]]) * width
                stack.pop()

            if stack and height[i] > height[stack[-1]]:
                stack.pop()
                
            stack.append(i)

        return trap

        