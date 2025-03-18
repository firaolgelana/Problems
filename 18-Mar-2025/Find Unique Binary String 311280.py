# Problem: Find Unique Binary String - https://leetcode.com/problems/find-unique-binary-string/description/

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        seen = set(nums)
        def find(idx, arr):
            if idx == len(nums):
                bit = "".join(arr[:])
                if bit not in seen:
                    return bit
                return None
            for bit in "01":
                arr.append(bit)
                ans = find(idx + 1, arr)
                if ans:
                    return ans
                arr.pop()

        return find(0, [])
        print(binary)
        

        