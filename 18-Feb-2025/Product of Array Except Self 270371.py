# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_product, post_product = [1], [1]
        
        for num in nums:
            pre_product.append(pre_product[-1] * num)

        for num in reversed(nums):
            post_product.append(post_product[-1] * num)
        post_product = post_product[-2::-1]
        product = []

        for pre, post in zip(pre_product, post_product):
            product.append(pre * post)

        return product

        