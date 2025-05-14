# Problem: Minimize XOR - https://leetcode.com/problems/minimize-xor/description/

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count = num2.bit_count()
        new_n1 = num1
        nums = []
        while num1 > 0:
            nums.append(num1 & 1)
            num1 >>= 1
        nums = nums[::-1]
        ans = 0
        if count <= nums.count(1):
            for i in range(len(nums)):
                if nums[i]:
                    ans += 2 ** (len(nums) - i - 1)
                    count -= 1
                if count == 0:
                    break
        else:
            ans += new_n1
            count2 = num2.bit_count() - nums.count(1)
            n = len(nums)
            for i in range(n):
                if nums[n - i - 1] == 0:
                    ans += 2 ** (i)
                    count2 -= 1
                if count2 == 0:
                    break
            while count2 > 0:
                ans += 2 ** n
                n += 1
                count2 -= 1
            
        return ans



        