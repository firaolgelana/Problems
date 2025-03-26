# Problem: Find Unique Binary String - https://leetcode.com/problems/find-unique-binary-string/description/

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = "".join(str(1 ^ int(nums[i][i])) for i in range(len(nums)))
        return ans
        

        