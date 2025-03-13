# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums) -> bool:
        def find_winner(i, j):
            if i == j:
                return nums[i]
            left = nums[i] - find_winner(i + 1, j) 
            right = nums[j] - find_winner(i, j - 1)
            return max(left, right)
        
        return find_winner(0, len(nums) - 1) >= 0
